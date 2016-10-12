angular.
  module('leagueList').
  component('leagueList', {
    templateUrl: 'league-list/league-list.template.html',
    controller: function LeagueListController($http) {
      var self = this;
      self.orderProp = 'id';

      $http.get('leagues/leagues.json').then(function(response) {
        self.leagues = response.data;
      });
    }
  });