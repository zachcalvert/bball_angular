function HomeController() {  
  var that = this;
  that.foo = "Foo!";
  console.log(that);
}

angular.module("Home")  
  .controller("HomeController", [
    HomeController
  ]);