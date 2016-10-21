import axios from 'axios';

export function deleteTeam(teamId) {
  return axios.delete('http://localhost:8001/api/v1/teams/' + teamId);
}

export function getTeam(teamId) {

  let team = {};

  // Get the league data from our local django api
  return axios.get('http://localhost:8001/api/v1/teams/' + teamId + '/?format=json')
    .then(response => {

      let team = response.data;
      team.name = team.name;
      team.owner = team.owner;
      team.record = team.record;
      team.leagueId = team.league;
      team.players = team.players;

      return team;

    });

}
