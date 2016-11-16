import axios from 'axios';

export function getPlayers(leagueId) {
  if (leagueId) {
    return axios.get('http://localhost:8001/api/v2/leagues/' + leagueId + '/free_agents.json')
      .then(response => response.data);
    }
  return axios.get('http://localhost:8001/api/v2/players/all.json')
    .then(response => response.data);
}

export function getPlayer(playerId) {

  let player = {};

  // Get the league data from our local django api
  return axios.get('http://localhost:8001/api/v2/players/' + playerId + '.json')
    .then(response => {

      let player = response.data;
      player.id = player.id
      player.name = player.name;
      player.position = player.position;
      player.nbaTeam = player.nba_team; 
      player.imageUrl = player.image_url;
      
      player.averages = player.stats.averages;
      player.totals = player.stats.totals;
      
      player.chart_games = player.chart_data.games;
      player.chart_scores = player.chart_data.player_scores;
      player.notes = player.notes

      return player
      
    });
}
