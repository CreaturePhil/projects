(function() {
  var app = angular.module('store', []);

  app.controller('StoreController', function () {
    this.product = kit;
  });

  var kit = {
    name: 'Coal',
    price: 5.00
  };
})();
