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

var LeagueSummary = React.createClass({
  render: function () {
    var league = this.props.league;
    var name = league.name;
    var teams = league.teams;

    return (
      <div className="league-summary">
      	<h4>{name}</h4>

	    {teams.map(function(team, i){
	        return <TeamSummary team={team} key={i} />;
	    })}

      </div>
    );
  }
});


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

var LeaguesList = React.createClass({
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
        if (this.state.data) {
            console.log(this.state.data)
            var leagueNodes = this.state.data.map(function(league){
                return <li> {league.name} </li>
            })
        }
        return (
            <div>
                <h1>Leagues</h1>
                <ul>
                    {leagueNodes}
                </ul>
            </div>
        )
    }
})

var Players  = React.createClass({
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
            console.log(this.state.data)
            var playerNodes = this.state.data.map(function(player){
                return <li> {player.name} </li>
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
         <Route path = "leagues" component = {LeaguesList}>
         	<Route path="blah" component={LeagueSummary}/>
		 </Route>
         <Route path = "players" component = {Players} />
      </Route>
   </Router>
	
), document.getElementById('container'))


