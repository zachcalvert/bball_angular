import React from 'react';
import _ from 'lodash';
import LeagueList from '../views/league-list';

const LeagueListContainer = React.createClass({
  loadLeaguesFromServer: function(){
        $.ajax({
            url: '/api/v1/leagues/?format=json',
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadLeaguesFromServer();
        setInterval(this.loadLeaguesFromServer, 
                    50000)
    }, 
    render: function() {
        return (<LeagueList leagues={this.state.data} />);
  }
});

export default LeagueListContainer;