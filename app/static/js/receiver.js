paste_locky_app.controller('receiver_controller',['$scope','$timeout','$http',
    function($scope,$timeout,$http)
    {
        $scope.init = function(message)
        {
            if (message.protected)
            {
                $scope.message_json = message
                if (message.message)
                {
                    $scope.message = $scope.message_json.message
                }
            }
            else
            {
                $scope.error_message = 'URL is not correct'
            }
        }

        $scope.receive_sender_data = function()
        {
            var sender_params = {'key': $scope.key,
                                 'encrypted_data': $scope.message_json.encrypted_data
                                  }
            var req = {
                method: 'POST',
                url: '/decode_sender_data',
                headers: {
                    'Content-Type': false
                },
                data: sender_params
            }
            $http(req).then(function successCallback(response) {
                if(response.data.response == 'success')
                {
                    $scope.message = response.data.message
                    $scope.message_json.message = $scope.message
                }
            }, function errorCallback(response) {
                console.log('Failure');

            });
        }
    }])