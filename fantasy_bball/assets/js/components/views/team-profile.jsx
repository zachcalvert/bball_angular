import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="team-profile">
      <img src={props.imageUrl} />
      <div className="details">
        <h4><Link to={'/leagues/' + props.leagueId}>back to league view</Link></h4>
        <h1>{props.name}</h1>
        <p>Manager: {props.owner}</p>
        <p>Record: {props.wins} - {props.losses} - {props.ties}</p>
        <h3>Roster:</h3>
          <ul className="roster">

            {props.players.map(player => {

              return (
                <div key={player.id} className="data-list-item">
                  <div className="details">
                    <Link to={'/players/' + player.id}>{player.name}</Link>
                  </div>
                </div>
              );
            })}

          </ul>
      </div>
    </div>
  );
}
