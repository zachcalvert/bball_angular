import React from 'react';

const PlayerList = React.createClass({
   loadPlayersFromServer: function(){
        $.ajax({
            url: '/api/v1/players/?format=json',
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
        this.loadPlayersFromServer();
    }, 
    render: function() {
        if (this.state.data) {
            var playerNodes = this.state.data.map(function(player){
                return <li key={player.id}> {player.name} </li>
            })
        }
        return (
            <div>
                <h1>Players</h1>
                <ul>
                    {playerNodes}
                </ul>
            </div>
        )
    }
})

export default PlayerList;