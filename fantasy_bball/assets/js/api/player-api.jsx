import axios from 'axios';

export function getPlayers() {
  return axios.get('http://localhost:8001/api/v1/players/?format=json')
    .then(response => response.data);
}

export function getPlayer(playerId) {

  let player = {};

  // Get the league data from our local django api
  return axios.get('http://localhost:8001/api/v1/players/' + playerId + '/?format=json')
    .then(response => {

      let player = response.data;
      player.id = player.id
      player.name = player.name;
      player.nba_team = player.nba_team;
      player.position = player.position;

      return player;
      
    });
}
