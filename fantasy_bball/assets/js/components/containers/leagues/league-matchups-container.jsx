import React from 'react';
import _ from 'lodash';
import LeageMatchups from '../../views/leagues/league-matchups';
import * as leagueApi from '../../../api/league-api';

const LeagueMatchupsContainer = React.createClass({

    getInitialState: function() {
        return {
            matchups: []
        };
    },

    componentDidMount: function() {
        let leagueId = this.props.params.leagueId
        leagueApi.getLeagueMatchups(leagueId).then(matchups => {
          this.setState({matchups: matchups})
        });
    },

    render: function() {
        console.log('here')
        return (
            <LeagueMatchups matchups={this.state.matchups} />
        );
    }
});

export default LeagueMatchupsContainer;