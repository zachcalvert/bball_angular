import React from 'react';
import TeamProfile from '../views/team-profile';
import * as teamApi from '../../api/team-api';

const TeamProfileContainer = React.createClass({

	getInitialState: function() {
		return {
			id: null,
			leagueId: null,
			name: null,
			owner: null,
			record: null,
			players: []
		}
	},

	componentDidMount: function() {
		let teamId = this.props.params.teamId
		teamApi.getTeam(teamId).then(team => {
			this.setState({
				id: team.id,
				leagueId: team.leagueId,
				name: team.name,
				owner: team.owner,
				record: team.record,
				players: team.players
			});
		});
	},

	render: function () {
		return (
			<TeamProfile {...this.state} />
		);
  	}
});

export default TeamProfileContainer;