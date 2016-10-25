import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="data-list">
      <h1>Leagues</h1>

      {props.leagues.map(league => {

        return (
          <div key={league.id} className="data-list-item">
            <div className="details">
              <Link to={'/leagues/' + league.id}>{league.name}</Link>
            </div>
          </div>
        );
      })}
    </div>
  );
}
