import React from 'react';
import _ from 'lodash';
import LeageMatchups from '../views/league-matchups';
import * as leagueApi from '../../api/league-api';

const LeagueMatchupsContainer = React.createClass({

    getInitialState: function() {
        return {
            matchups: []
        };
    },

    componentDidMount: function() {
        leagueApi.getMatchups().then(matchups => {
          this.setState({matchups: matchups})
        });
    },

    render: function() {
        return (
            <LeagueMatchups matchups={this.state.matchups} />
        );
    }
});

export default LeagueMatchupsContainer;