import axios from 'axios';

export function deleteTeam(teamId) {
  return axios.delete('http://localhost:8001/api/v2/leagues/teams/' + teamId + '.json')
}

export function getTeam(teamId) {

  let team = {};

  // Get the league data from our local django api
  return axios.get('http://localhost:8001/api/v2/teams/' + teamId + '.json')
    .then(response => {

      let team = response.data;
      team.name = team.name;
      team.owner = team.owner;
      team.record = team.record;
      team.leagueId = team.league_id;
      team.players = team.players;

      return team;

    });

}
