

var LeagueSummary = React.createClass({
  render: function () {
    var league = this.props.league;
    var name = league.name;

    return (
      <div className="league-summary">{name}</div>
    );
  }
});

var LeaguesList = React.createClass({
  render: function () {
    var leagues = this.state.data;
    console.log(leagues)

    return (
      <div className="league-list">
      {
        leagues.map(function (league) {
          return (
            <LeagueSummary key={league.id} league={league}/>
          );
        })
      }
      </div>
    );
  }
});