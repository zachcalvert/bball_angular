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
			wins: null,
			ties: null,
			losses: null,
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
				wins: team.wins,
				ties: team.ties,
				losses: team.losses,
				players: team.players
			});
		});
	},

	render: function () {
		console.log(this.state)
		return (
			<TeamProfile {...this.state} />
		);
  	}
});

export default TeamProfileContainer;