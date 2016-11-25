import React from 'react';
import { Link } from 'react-router';

export default function(props) {
  return (
    <div className="league-matchups">

      {props.matchups.this_week.map(matchup => {

        return (
          <div key={matchup.home_id} className="league-matchup">
            <div className="league-matchup-home">
              <Link to={'/leagues/' + matchup.league_id + '/teams/' + matchup.home_id}>{matchup.home_team}</Link>
            </div>

            <div className="league-matchup-away">
              <Link to={'/leagues/' + matchup.league_id + '/teams/' + matchup.away_id}>{matchup.away_team}</Link>
            </div>
          </div>
        );
      })}
    </div>
  );
}
