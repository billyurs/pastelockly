from django.shortcuts import render_to_response, redirect, render, Http404, HttpResponse
import base64
import json
import traceback
from app.models import MessageDetails


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')

def sender(request):
    if request.method == "GET":
        return render(request, 'sender.html')

def receiver(request):
    try:
        key = request.GET.get('key')
        msg_obj = MessageDetails.objects.get(encrypted_data=key)
        response_recv = {}
        if msg_obj:
            response_recv['protected'] = msg_obj.protected
            response_recv['encrypted_data'] = key
            if response_recv.get('protected') == 'True':
                response_recv['message'] = ''
            else:
                response_recv['message'] = msg_obj.message_data
        return render(request, 'receiver.html', {'message': json.dumps(response_recv)})
    except Exception as e:
        formatted_lines = traceback.format_exc().splitlines()
        print formatted_lines
        return render(request, 'receiver.html', {'message': {}})

def save_sender_data(request):
    sender_params = json.loads(request.body)
    key = sender_params.get('key', '')
    protect_key = False
    if not key:
        key = 'demo key'
    else:
        protect_key = True
    message = sender_params.get('message', '')
    encr_msg  = encode(key, message)
    msg_obj = MessageDetails(key = key, message_data = message, \
                             protected = protect_key, encrypted_data=encr_msg)
    msg_obj.save()
    return HttpResponse(json.dumps({'response': 'success',
                                    'shareable_url': encr_msg}))


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def decode_sender_data(request):
    decode_params = json.loads(request.body)
    encrypted_key = decode_params.get('encrypted_data')
    key = decode_params.get('key')
    msg_obj = MessageDetails.objects.filter(encrypted_data=encrypted_key, key=key)
    response_recv = {}
    if msg_obj:
        msg_obj = msg_obj[0]
        response_recv['protected'] = msg_obj.protected
        response_recv['encrypted_data'] = key
        if response_recv.get('protected'):
            response_recv['message'] = ''
        else:
            response_recv['message'] = msg_obj.message_data
        return HttpResponse(json.dumps({'response': 'success',
                                        'message': msg_obj.message_data}
                                       ))
    else:
        return HttpResponse(json.dumps({'response': 'failure',
                                        'message': {}}))
