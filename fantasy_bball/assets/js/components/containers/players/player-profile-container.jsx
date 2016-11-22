import React from 'react';
import PlayerProfile from '../../views/players/player-profile';
import * as playerApi from '../../../api/player-api';

const PlayerProfileContainer = React.createClass({

	getInitialState: function() {
		return {
			id: null,
			name: null,
			position: null,
			nbaTeam: null,
			imageUrl: null,
			date: null,
			report: null,
			impact: null,
			chart_games: [],
			chart_scores: [],
			totals: [],
			averages: [],
			recent_games: [],
			season_form: null
		}
	},

	componentDidMount: function() {
		let playerId = this.props.params.playerId
		playerApi.getPlayer(playerId).then(player => {
			this.setState({
				id: player.id,
				name: player.name,
				position: player.position,
				nbaTeam: player.nbaTeam,
				imageUrl: player.imageUrl,
				
				date: player.notes.date,
				report: player.notes.report,
				impact: player.notes.impact,

				totals: player.totals,
				averages: player.averages,
				chart_games: player.chart_games,
				chart_scores: player.chart_scores,
				recent_games: player.recent_games,
				season_form: player.season_form
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