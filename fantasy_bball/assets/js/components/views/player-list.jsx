import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="data-list">
      <h1>Players</h1>

      {props.players.map(player => {

        return (
          <div key={player.id} className="data-list-item">
            <div className="details">
              <Link to={'/players/' + player.id}>{player.name}</Link>
            </div>
          </div>
        );
      })}
    </div>
  );
}
