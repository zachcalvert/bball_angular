import React from 'react';
import PlayerProfile from '../../views/players/player-profile';
import * as playerApi from '../../../api/player-api';

const PlayerProfileContainer = React.createClass({

	getInitialState: function() {
		return {
			id: null,
			name: null,
			position: null,
			nba_team: null
		}
	},

	componentDidMount: function() {
		let playerId = this.props.params.playerId
		playerApi.getPlayer(playerId).then(player => {
			this.setState({
				id: player.id,
				name: player.name,
				position: player.position,
				nba_team: player.nba_team
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