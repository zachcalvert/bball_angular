var LeagueList = React.createClass({
  render: function() {
    console.log(this.props)
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