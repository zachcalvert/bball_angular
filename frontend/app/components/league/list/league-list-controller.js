function LeagueListController(LeagueService) {  
  var that = this;

  /* Stored league objects. */
  that.leagues = [];

  /**
   * Initialize the league list controller.
   */
  that.init = function() {
    return LeagueService.getLeagues().then(function(leagues) {
      that.leagues = leagues;
    });
  };
}


angular.module("League")  
  .controller("LeagueListController", [
    "LeagueService",
    LeagueListController
  ]);