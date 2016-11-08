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
			recent_games: []
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
				
				total_pts: player.stats.totals.pts,
				total_rebs: player.stats.totals.rebs,
				total_asts: player.stats.totals.asts,
				total_blks: player.stats.totals.blks,
				total_stls: player.stats.totals.stls,
				total_fgm: player.stats.totals.fgm,
				total_fga: player.stats.totals.fga,
				total_ftm: player.stats.totals.ftm,
				total_fta: player.stats.totals.fta,
				total_threesm: player.stats.totals.threesm,
				total_threesa: player.stats.totals.threesa,

				avg_pts: player.stats.averages.pts,
				avg_rebs: player.stats.averages.rebs,
				avg_asts: player.stats.averages.asts,
				avg_blks: player.stats.averages.blks,
				avg_stls: player.stats.averages.stls,
				avg_fgm: player.stats.averages.fgm,
				avg_fga: player.stats.averages.fga,
				avg_ftm: player.stats.averages.ftm,
				avg_fta: player.stats.averages.fta,
				avg_threesm: player.stats.averages.threesm,
				avg_threesa: player.stats.averages.threesa,

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