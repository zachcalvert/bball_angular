var React = require('react')
var ReactDOM = require('react-dom')
// var LeaguesList = require('./leagues-list')

class LikeButton extends React.Component {
  constructor() {
    super();
    this.state = {
      liked: false
    };
    this.handleClick = this.handleClick.bind(this);
  }
  handleClick() {
    this.setState({liked: !this.state.liked});
  }
  render() {
    const text = this.state.liked ? 'liked' : 'haven\'t liked';
    return (
      <div onClick={this.handleClick}>
        You {text} this. Click to toggle.
      </div>
    );
  }
}

var LeaguesList = React.createClass({
    loadLeaguesFromServer: function(){
        $.ajax({
            url: this.props.url,
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
                    this.props.pollInterval)
    }, 
    render: function() {
        if (this.state.data) {
            console.log('DATA!')
            var leagueNodes = this.state.data.map(function(league){
                return <li> {league.name} </li>
            })
        }
        return (
            <div>
                <h1>Hello React!</h1>
                <ul>
                    {leagueNodes}
                </ul>
            </div>
        )
    }
})

ReactDOM.render(<LeaguesList url='/api/v1/leagues/?format=json' pollInterval={10000} />, 
    document.getElementById('container'))

ReactDOM.render(
  <LikeButton />,
  document.getElementById('button')
);


// ReactDOM.render(<App/>, document.getElementById('react-app'))
