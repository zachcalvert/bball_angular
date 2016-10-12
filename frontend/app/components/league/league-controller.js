function LeagueController(LeagueService) {  
  var that = this;

  /* Stored league objects. */
  that.league = [];

  /**
   * Initialize the league list controller.
   */
  that.init = function() {
    return LeagueService.getLeague().then(function(league) {
      console.log("djajdgahdjfgahkdghja");
      console.log(league);
      that.league = league;
    });
  };
}


angular.module("League")  
  .controller("LeagueController", [
    "LeagueService",
    LeagueController
  ]);