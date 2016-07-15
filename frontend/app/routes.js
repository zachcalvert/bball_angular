function routesConfig($routeProvider) {  
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/home/home.html",
      label: "Home"
    })
    .when("/leagues", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/league/list/league-list.html",
      label: "Leagues"
    })
    .when("/teams", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/team/list/team-list.html",
      label: "Teams"
    })
    .when("/players", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/player/list/player-list.html",
      label: "Players"
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig;