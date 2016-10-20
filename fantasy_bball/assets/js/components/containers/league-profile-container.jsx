import React from 'react';
import LeagueProfile from '../views/league-profile';

const LeagueProfileContainer = React.createClass({
	loadLeagueFromServer: function(){
		var league = this.props.league;
		var id = league.id;

	    $.ajax({
	        url: '/api/v1/leagues/' + id + '?format=json',
	        datatype: 'json',
	        cache: false,
	        success: function(data) {
	            this.setState({data: data});
	        }.bind(this)
	    })
	},
	getInitialState: function() {
	    return {
	    	data: [],
	    	isSelected: false
	    };
	},
	componentDidMount: function() {
	    this.loadLeagueFromServer().then(league );
	    let leagueId = this.props.params.leagueId

	}, 
	render: function () {
		return (
			<LeagueProfile {...this.state} />
		);
  	}
});

export default LeagueProfileContainer;