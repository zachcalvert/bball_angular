import axios from 'axios';

export function getHome() {
  return axios.get('http://localhost:8001/api/v2/home.json')
    .then(response => {

      let home = response.data;
      home.yesterday = home.yesterday;
      home.top_performers = home.top_performers;
      home.goat_performances = home.goat_performances;
      return home
	});
}