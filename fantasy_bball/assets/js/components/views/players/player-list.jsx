import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="data-list">
      <h1>Players</h1>
      <div className="player-list-stats">
        <strong>2016-17</strong>
        <div className="rTable">
          <div className="rTableRow">
            <div className="rTableHead name"><strong>NAME</strong></div>
            <div className="rTableHead"><strong>PTS</strong></div>
            <div className="rTableHead"><strong>REBS</strong></div>
            <div className="rTableHead"><strong>ASTS</strong></div>
            <div className="rTableHead"><strong>STLS</strong></div>
            <div className="rTableHead"><strong>BLKS</strong></div>
          </div>

        {props.players.map(player => {
          if (player.stats.averages) {
            return (
              <div className="rTableRow" key={player.id}>
                <div className="rTableCell"><Link to={'/players/' + player.id}>{player.name}</Link></div>
                <div className="rTableCell">{player.stats.averages.pts}</div>
                <div className="rTableCell">{player.stats.averages.rebs}</div>
                <div className="rTableCell">{player.stats.averages.asts}</div>
                <div className="rTableCell">{player.stats.averages.stls}</div>
                <div className="rTableCell">{player.stats.averages.blks}</div>
              </div>
            );
          } 
          else {
            return (
              <div className="rTableRow" key={player.id}>
                <div className="rTableCell"><Link to={'/players/' + player.id}>{player.name}</Link></div>
                <div className="rTableCell">0.0</div>
                <div className="rTableCell">0.0</div>
                <div className="rTableCell">0.0</div>
                <div className="rTableCell">0.0</div>
                <div className="rTableCell">0.0</div>
              </div>
            );
          }
        })}
      </div>
    </div>
    </div>
  );
}