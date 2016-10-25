import React from 'react';
import { Link } from 'react-router';

const LeagueLayout = React.createClass({
  render: function() {
    return (
      <div className="league-layout">
        <header className="league-header">
          <ul>
              <li><Link to={"/leagues/" + this.props.params.leagueId} activeClassName="active">League Home</Link></li>
              <li><Link to={"/leagues/" + this.props.params.leagueId + "/players"} activeClassName="active">Free Agents</Link></li>
              <li><Link to={"/leagues/" + this.props.params.leagueId + "/matchups"} activeClassName="active">Matchups</Link></li>
              <li><Link to={"/leagues/" + this.props.params.leagueId + "/standings"} activeClassName="active">Standings</Link></li>
              <li><Link to={"/leagues/" + this.props.params.leagueId + "/schedule"} activeClassName="active">Schedule</Link></li>
            </ul>
        </header>
        <aside className="primary-aside"></aside>
        <div className="main">
          {this.props.children}
        </div>
      </div>
    );
  }
});

export default LeagueLayout;
