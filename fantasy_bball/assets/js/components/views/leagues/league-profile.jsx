import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="league-profile">
      <img src={props.imageUrl} />
      
      <div className="details">
        <h1>{props.name}</h1>
        <p>Manager: {props.manager_id}</p>
        <p>Public: {props.is_public}</p>
        <h3>Teams:</h3>
          <ul className="teams">

            {props.teams.map(team => {

              return (
                <div key={team.id} className="data-list-item">
                  <div className="details">
                    <Link to={'/leagues/' + props.id + '/teams/' + team.id}>{team.name}</Link>
                  </div>
                </div>
              );
            })}

          </ul>
      </div>
    </div>
  );
}
