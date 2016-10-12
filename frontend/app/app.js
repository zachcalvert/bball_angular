/* Libs */
require("angular/angular");  
require("angular-route/angular-route");  
require("angular-resource/angular-resource");

/* Globals */
_ = require("lodash");  
_urlPrefixes = {  
  API: "api/v1/",
  TEMPLATES: "static/app/"
};

/* Components */
require("./components/home/home");
require("./components/league/league");
require("./components/team/team");
require("./components/player/player");

/* App Dependencies */
angular.module("fantasyBBallApp", [ 
  "ngResource",
  "ngRoute",
  "angular.filter",
  "Home",
  "League",
  "Team",
  "Player",
]);

/* Config Vars */
var routesConfig = require("./routes");

/* App Config */
angular.module("fantasyBBallApp").config(routesConfig);  