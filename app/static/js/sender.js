paste_locky_app.controller('sender_controller',['$scope','$timeout','$http',
    function($scope,$timeout,$http)
    {
        $scope.init = function()
        {

        }

        $scope.save_sender_data = function()
        {
            var sender_params = {'key': $scope.key,
                                   'message': $scope.message}
            var req = {
                method: 'POST',
                url: '/save_sender_data',
                headers: {
                    'Content-Type': false
                },
                data: sender_params
            }
            $http(req).then(function successCallback(response) {
                if(response.data.response == 'success')
                {
                    $scope.shareable_url = 'http://127.0.0.1:8000/receiver?key='+response.data.shareable_url
                }
            }, function errorCallback(response) {
                console.log('Failure');

            });
        }

        $scope.reset_sender_data = function()
        {
            $scope.key = ''
            $scope.message = ''
            $scope.shareable_url  = ''
        }
    }])