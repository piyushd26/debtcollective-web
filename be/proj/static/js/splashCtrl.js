app.controller('splashCtrl', function ($scope, $http, util_svc, $document, $timeout) {

    $scope.email = null;
    $scope.username = null;
    $scope.location = null;
    $scope.debtType = null;
    $scope.amount = null;
    $scope.showForm = false;

    $http.get('/points/').then(function (resp) {
        $scope.cities = resp.data
    });

    $scope.bannerFadeInTimeout = false;
    $timeout(function () {
        $scope.bannerFadeInTimeout = true;
    }, 500)

    $scope.scrollClick = function () {
        var someElement = angular.element(document.getElementById('mapdiv'));
        $document.scrollToElement(someElement, 0, 18000);
    }

    $scope.formValid = function () {
        return $scope.location != null && $scope.email != null
            && $scope.amount != null;
    }

    $scope.formVisible = function () {
        return $scope.showForm == true;
    }

    $scope.emailFocus = function () {
        $scope.showForm = true;
        el = document.getElementById("email");
        el.placeholder =  'enter your email...';
    }

    $scope.onSubmitClick = function () {
        $scope.username = util_svc.generateUUID();

        // temporarily, email is the password
        // so that we can protect anonymity of our users.
        // campaign monitor handles mailing lists

        amount = parseFloat($scope.amount.replace(',', ''));
        data = {
            'username': $scope.username,
            'password': $scope.email,
            'point': $scope.location.id,
            //'kind': $scope.debtType.name,
            'amount': amount
        }

        $http.post('/signup/', data).then(function (resp) {
            $scope.formSubmitted = true;
            $scope.showForm = true;
        });
    }
});
