import React from 'react';
import LeagueProfile from '../../views/leagues/league-profile';
import * as leagueApi from '../../../api/league-api';

const LeagueProfileContainer = React.createClass({

	getInitialState: function() {
		return {
			name: null,
			manager_id: null,
			is_public: null,
			teams: []
		}
	},

	componentDidMount: function() {
		let leagueId = this.props.params.leagueId
		leagueApi.getLeague(leagueId).then(league => {
			this.setState({
				id: league.id,
				name: league.name,
				manager_id: league.manager_id,
				is_public: league.is_public,
				teams: league.teams
			});
		});
	},

	render: function () {
		console.log(this.state)
		return (
			<LeagueProfile {...this.state} />
		);
  	}
});

export default LeagueProfileContainer;