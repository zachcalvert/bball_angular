import React from 'react';
import PlayerProfile from '../../views/players/player-profile';
import * as playerApi from '../../../api/player-api';

const PlayerProfileContainer = React.createClass({

	getInitialState: function() {
		return {
			id: null,
			name: null,
			position: null,
			nba_team: null,
			date: null,
			report: null,
			impact: null,
			recent_games: [],
			totals: [],
			averages: []
		}
	},

	componentDidMount: function() {
		let playerId = this.props.params.playerId
		playerApi.getPlayer(playerId).then(player => {
			this.setState({
				id: player.id,
				name: player.name,
				position: player.position,
				nbaTeam: player.nba_team,
				imageUrl: player.image_url,
				
				date: player.notes.date,
				report: player.notes.report,
				impact: player.notes.impact,
				
				totals: player.stats.totals,
				averages: player.stats.averages,
				fgpct: player.stats.averages.fgpct,
				ftpct: player.stats.averages.ftpct,
				threespct: player.stats.averages.threespct,

				recent_games: player.recent_games,
				
			});
		});
	},

	render: function () {
		return (
			<PlayerProfile {...this.state} />
		);
  	}
});

export default PlayerProfileContainer;