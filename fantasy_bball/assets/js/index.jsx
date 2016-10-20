var React = require('react')
var ReactDOM = require('react-dom')

import { Router, Route, Link, IndexLink, browserHistory, IndexRoute } from 'react-router'


var TeamSummary = React.createClass({
	loadTeamInfo: function(id){
		$.ajax({
		    url: '/api/v1/teams/' + id + '?format=json',
		    datatype: 'json',
		    cache: false,
		    success: function(data) {
		        this.setState({data: data});
		    }.bind(this)
		})
	},

	render: function () {
		var team = this.props.team;
		var id = team.id;
		var name = team.name;
		var record = team.record;
		var players = team.players;

		return (
		  <div className="team-summary">
		  	<b>{name}</b> - {record}
		  </div>
		);
	}
});

// var TeamsList = React.createClass({
// 	loadTeamsFromServer: function(){
// 		$.ajax({
// 		    url: this.props.url,
// 		    datatype: 'json',
// 		    cache: false,
// 		    success: function(data) {
// 		        this.setState({data: data});
// 		    }.bind(this)
// 		})
// 	},

// 	getInitialState: function() {
// 		return {data: []};
// 	},

// 	componentDidMount: function() {
// 		this.loadTeamsFromServer();
// 		setInterval(this.loadTeamsFromServer, 
// 		            this.props.pollInterval)
// 	}, 

// 	render: function () {
// 		var teams = this.state.data;

// 		return (
// 			<div className="team-list">
// 			{
// 				teams.map(function (team) {
// 			  		return (
// 			    		<TeamSummary key={team.id} team={team}/>
// 			  		);
// 				})
// 			}
// 			</div>
// 		);
// 	}
// });


class App extends React.Component {
   render() {
      return (
         <div className="content">
            <ul className="nav-menu">
               <li><IndexLink to="/" activeClassName="active">Home</IndexLink></li>
               <li><Link to="/leagues" activeClassName="active">Leagues</Link></li>
               <li><Link to="/players" activeClassName="active">Players</Link></li>
            </ul>
				
           {this.props.children}
         </div>
      )
   }
}

export default App;

class Home extends React.Component {
   render() {
      return (
         <div>
            <h1>Home...</h1>
         </div>
      )
   }
}

var LeagueListContainer = React.createClass({
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
})

var LeagueList = React.createClass({
  render: function() {
    return (
      <ul className="league-list">
        {this.props.leagues.map(this.createLeagueItem)}
      </ul>
    );
  },

  createLeagueItem: function(league) {
    return (
      <li key={league.id}>
        <Link to="{'/leagues/' + league.id}">{league.name}</Link>
      </li>
    );
  }
});

var LeagueSummary = React.createClass({
	getComponent: function(index) {
        $(this.getDOMNode()).find('li:nth-child(' + index + ')').css({
            'background-color': '#ccc'
        });
    },

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
	handleClick: function() {
        this.setState({
            isSelected: true
        })
    },
	componentDidMount: function() {
	    this.loadLeagueFromServer();
	    setInterval(this.loadLeagueFromServer, 
	                50000)
	}, 
	render: function () {
		var isSelected = this.state.isSelected;
		var style = {
            'background-color': ''
        };
		var league = this.props.league;
		var name = league.name;
		var teams = league.teams;

		if (isSelected) {
            style = {
                'background-color': '#ccc'
            };
        }

		return (
		  <div className="league-summary">
		  	<h4>{name}</h4>

		    {teams.map(function(team, i){
		        return <li onClick={this.handleClick} style={style} key={team.id}> {team.name} </li>;
		    }, this)}
		  </div>
	);
  }
});

var Players = React.createClass({
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
        setInterval(this.loadPlayersFromServer, 
                    50000)
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

ReactDOM.render((
   <Router history = {browserHistory}>
      <Route path = "/" component = {App}>
         <IndexRoute component = {Home} />
         <Route path = "home" component = {Home} />
         <Route path = "leagues" component = {LeagueListContainer}>
         	<Route path="blah" component={LeagueSummary}/>
		 </Route>
         <Route path = "players" component = {Players} />
      </Route>
   </Router>
	
), document.getElementById('container'))
