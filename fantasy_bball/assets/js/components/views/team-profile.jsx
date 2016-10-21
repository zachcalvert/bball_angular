import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="team-profile">
      <header className="league-header">
        <ul>
          <li><Link to={"/leagues/" + props.leagueId} activeClassName="active">League Home</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/players"} activeClassName="active">Free Agents</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/matchups"} activeClassName="active">Matchups</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/standings"} activeClassName="active">Standings</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/schedule"} activeClassName="active">Schedule</Link></li>
        </ul>
      </header>

      <img src={props.imageUrl} />
      <div className="details">
        <h1>{props.name}</h1>
        <p>Manager: {props.owner}</p>
        <p>Record: {props.record}</p>
        <h3>Roster:</h3>
          <ul className="roster">

            {props.players.map(player => {

              return (
                <div key={player.id} className="data-list-item">
                  <div className="details">
                    <Link to={'/players/' + player.id}>{player.name}</Link> {player.position} {player.nba_team}
                  </div>
                </div>
              );
            })}

          </ul>
      </div>
    </div>
  );
}
