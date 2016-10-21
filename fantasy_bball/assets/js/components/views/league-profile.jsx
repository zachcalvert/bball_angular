import React from 'react';

export default function(props) {
  return (
    <div className="league-profile">
      <img src={props.imageUrl} />
      <div className="details">
        <h1>{props.name}</h1>
        <p>Manager: {props.manager_id}</p>
        <p>Public: {props.is_public}</p>
        <h3>Teams:</h3>
          <ul className="repos">

            {props.teams.map(team => {

              return (<li key={team.id}><a href={team.url}>{team.name}</a></li>);

            })}

          </ul>
      </div>
    </div>
  );
}
