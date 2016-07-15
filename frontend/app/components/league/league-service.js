function LeagueService($resource) {  
  /**
   * @name LeagueService
   *
   * @description
   * A service providing league data.
   */

  var that = this;

  /**
   * A resource for retrieving league data.
   */
  that.LeagueResource = $resource(_urlPrefixes.API + "leagues/:league_id/");

  /**
   * A convenience method for retrieving League objects.
   * Retrieval is done via a GET request to the ../leagues/ endpoint.
   * @param {object} params - the query string object used for a GET request to ../leagues/ endpoint
   * @returns {object} $promise - a promise containing league-related data
   */
  that.getLeagues = function(params) {
    return that.LeagueResource.query(params).$promise;
  };
}

angular.module("League")  
  .service("LeagueService", ["$resource", LeagueService]);