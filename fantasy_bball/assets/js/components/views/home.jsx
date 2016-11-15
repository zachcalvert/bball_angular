import React from 'react';
import { Link } from 'react-router';

export default function(props) {

  return (
      <div className="home-page">
        
        <div className="top-performers">
          <h4>Top Performers from {props.yesterday}</h4>
          {props.top_performers.map((statline) => {
            return (

              <div className="top-performer" key={statline.id}>
                <strong>Game score: {statline.game_score}</strong><br />
                <p>{statline.game}</p>

                <div className="top-performace-player-details">
                  <Link to={'/players/' + statline.player.id}><img src={statline.player.image_url} /></Link>
                  <p>{statline.player.name}</p>
                  <p>{statline.player.position} &#8226; {statline.player.nba_team}</p>
                </div>

                <div className="top-performace-game-details">
                  <ul className="statline-stats">
                    <li>PTS: {statline.pts}</li>
                    <li>FG: {statline.fgm}/{statline.fga}</li>
                    <li>FT: {statline.ftm}/{statline.fta}</li>
                    <li>3PT: {statline.threesm}/{statline.threesa}</li>
                    <li>RBS: {statline.rebs}</li>
                    <li>ASTS: {statline.asts}</li>
                    <li>STLS: {statline.stls}</li>
                    <li>BLKS: {statline.blks}</li>
                    <li>TOS: {statline.tos}</li>
                  </ul>
                </div>
              </div>
            );
          })}
        </div>

      </div>
    );
}