function TeamListController(TeamService) {  
  var that = this;

  /* Stored team objects. */
  that.teams = [];

  /**
   * Initialize the team list controller.
   */
  that.init = function() {
    return TeamService.getTeams().then(function(teams) {
      that.teams = teams;
    });
  };
}


angular.module("Team")  
  .controller("TeamListController", [
    "TeamService",
    TeamListController
  ]);