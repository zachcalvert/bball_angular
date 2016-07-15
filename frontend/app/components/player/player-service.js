function PlayerService($resource) {  
  /**
   * @name PlayerService
   *
   * @description
   * A service providing player data.
   */

  var that = this;

  that.PlayerResource = $resource(_urlPrefixes.API + "players/:player_id/");

  that.getPlayers = function(params) {
    return that.PlayerResource.query(params).$promise;
  };
}

angular.module("Player")  
  .service("PlayerService", ["$resource", PlayerService]);