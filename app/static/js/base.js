var paste_locky_app = angular.module('pastelocky', [])
paste_locky_app.controller('paste_locky_controller',['$scope','$timeout','$http',
    function($scope,$timeout,$http)
    {
        $scope.init = function()
        {
        }
    }])

paste_locky_app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);