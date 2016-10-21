import React from 'react';
import _ from 'lodash';
import LeagueList from '../views/league-list';
import * as leagueApi from '../../api/league-api';

const LeagueListContainer = React.createClass({

    getInitialState: function() {
        return {
            leagues: []
        };
    },

    componentDidMount: function() {
        leagueApi.getLeagues().then(leagues => {
          this.setState({leagues: leagues})
        });
    },

    render: function() {
        return (
            <LeagueList leagues={this.state.leagues} />
        );
    }
});

export default LeagueListContainer;