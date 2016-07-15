function PlayerListController(PlayerService) {  
  var that = this;

  /* Stored player objects. */
  that.players = [];

  /**
   * Initialize the player list controller.
   */
  that.init = function() {
    return PlayerService.getPlayers().then(function(players) {
      that.players = players;
    });
  };
}


angular.module("Player")  
  .controller("PlayerListController", [
    "PlayerService",
    PlayerListController
  ]);