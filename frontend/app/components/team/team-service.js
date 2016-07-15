function TeamService($resource) {  
  /**
   * @name TeamService
   *
   * @description
   * A service providing team data.
   */

  var that = this;

  /**
   * A resource for retrieving team data.
   */
  that.TeamResource = $resource(_urlPrefixes.API + "teams/:team_id/");

  that.getTeams = function(params) {
    return that.TeamResource.query(params).$promise;
  };
}

angular.module("Team")  
  .service("TeamService", ["$resource", TeamService]);