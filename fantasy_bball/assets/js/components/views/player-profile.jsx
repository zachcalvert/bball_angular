import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="player-profile">
      <img src={props.imageUrl} />
      <div className="details">
        <h1>{props.name}</h1>
        <p>Team: {props.nba_team}</p>
        <p>Position: {props.position}</p>
      </div>
    </div>
  );
}
