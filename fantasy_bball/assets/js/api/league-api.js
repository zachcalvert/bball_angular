import axios from 'axios';

export function getLeagues() {
  return axios.get('http://localhost:8001/api/v2/leagues.json')
    .then(response => response.data);
}

export function deleteLeague(leagueId) {
  return axios.delete('http://localhost:8001/api/v2/leagues/' + leagueId + '.json')
}

export function getLeague(leagueId) {

  let league = {};

  // Get the league data from our local django api
  return axios.get('http://localhost:8001/api/v2/leagues/' + leagueId + '.json')
    .then(response => {

      let league = response.data;
      league.name = league.name;
      league.manager_id = league.manager;
      league.is_public = league.is_public;
      league.teams = league.teams;

      return league;
      
    });
}
