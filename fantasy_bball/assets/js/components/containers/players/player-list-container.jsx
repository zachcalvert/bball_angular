import React from 'react';
import _ from 'lodash';
import PlayerList from '../../views/players/player-list';
import * as playerApi from '../../../api/player-api';

const PlayerListContainer = React.createClass({

    getInitialState: function() {
        return {
            players: []
        };
    },

    componentDidMount: function() {
        playerApi.getPlayers(this.props.routeParams.leagueId).then(players => {
          this.setState({players: players})
        });
    },

    render: function() {
        return (
            <PlayerList players={this.state.players} />
        );
    }
});

export default PlayerListContainer;