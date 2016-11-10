import React from 'react';
import { Link } from 'react-router';
import {Line} from 'react-chartjs-2';

export default function(props) {
  var gameChartData = {
    "labels": ['Games'],
    "datasets": [
      {
        "label": 'My First dataset',
        "fill": false,
        "lineTension": 0.1,
        "backgroundColor": 'rgba(75,192,192,0.4)',
        "borderColor": 'rgba(75,192,192,1)',
        "borderCapStyle": 'butt',
        "borderDash": [],
        "borderDashOffset": 0.0,
        "borderJoinStyle": 'miter',
        "pointBorderColor": 'rgba(75,192,192,1)',
        "pointBackgroundColor": '#fff',
        "pointBorderWidth": 1,
        "pointHoverRadius": 5,
        "pointHoverBackgroundColor": 'rgba(75,192,192,1)',
        "pointHoverBorderColor": 'rgba(220,220,220,1)',
        "pointHoverBorderWidth": 2,
        "pointRadius": 1,
        "pointHitRadius": 10,
        "data": props.recent_games
      }
    ]
  }

  return (
    <div className="player-profile">

      <div className="player-info">
        
        <div className="player-image">
          <img src={props.imageUrl} />
        </div>
        
        <h4>{props.name}</h4>
        <p>{props.nbaTeam}  &#8226; {props.position}</p>
      </div>

      <div className="player-details">
        <div className="player-quick-stats">
          <strong>2016-17</strong>
          <div className="rTable">
            <div className="rTableRow">
              <div className="rTableHead"><strong>PTS</strong></div>
              <div className="rTableHead"><strong>REBS</strong></div>
              <div className="rTableHead"><strong>ASTS</strong></div>
              <div className="rTableHead"><strong>STLS</strong></div>
              <div className="rTableHead"><strong>BLKS</strong></div>
            </div>
            <div className="rTableRow">
              <div className="rTableCell">{props.averages.pts}</div>
              <div className="rTableCell">{props.averages.rebs}</div>
              <div className="rTableCell">{props.averages.asts}</div>
              <div className="rTableCell">{props.averages.stls}</div>
              <div className="rTableCell">{props.averages.blks}</div>
            </div>
          </div>
        </div>
        <strong>Recent Notes</strong>
        <div className="player-notes">
          <p>{props.date}</p>
          <p>{props.report}</p>
          <p>{props.impact}</p>
        </div>
      </div>

      <div className="player-stats">
        <strong>Totals</strong>
        <div className="rTable">
          <div className="rTableRow">
            <div className="rTableHead"><strong>PTS</strong></div>
            <div className="rTableHead"><strong>REBS</strong></div>
            <div className="rTableHead"><strong>ASTS</strong></div>
            <div className="rTableHead"><strong>STLS</strong></div>
            <div className="rTableHead"><strong>BLKS</strong></div>
            <div className="rTableHead"><strong>FGM</strong></div>
            <div className="rTableHead"><strong>FGA</strong></div>
            <div className="rTableHead"><strong>FGPCT</strong></div>  
            <div className="rTableHead"><strong>FTM</strong></div>
            <div className="rTableHead"><strong>FTA</strong></div>
            <div className="rTableHead"><strong>FTPCT</strong></div>
            <div className="rTableHead"><strong>3PTM</strong></div>
            <div className="rTableHead"><strong>3PTA</strong></div>
            <div className="rTableHead"><strong>3PCT</strong></div>
          </div>
          <div className="rTableRow">
            <div className="rTableCell">{props.totals.pts}</div>
            <div className="rTableCell">{props.totals.rebs}</div>
            <div className="rTableCell">{props.totals.asts}</div>
            <div className="rTableCell">{props.totals.stls}</div>
            <div className="rTableCell">{props.totals.blks}</div>
            <div className="rTableCell">{props.totals.fgm}</div>
            <div className="rTableCell">{props.totals.fga}</div>
            <div className="rTableCell">{props.fgpct}</div>
            <div className="rTableCell">{props.totals.ftm}</div>
            <div className="rTableCell">{props.totals.fta}</div>
            <div className="rTableCell">{props.ftpct}</div>
            <div className="rTableCell">{props.totals.threesm}</div>
            <div className="rTableCell">{props.totals.threesa}</div>
            <div className="rTableCell">{props.threespct}</div>
          </div>
        </div>
      </div>

      <div className="player-stats">
        <strong>Averages</strong>
        <div className="rTable">
          <div className="rTableRow">
            <div className="rTableHead"><strong>PTS</strong></div>
            <div className="rTableHead"><strong>REBS</strong></div>
            <div className="rTableHead"><strong>ASTS</strong></div>
            <div className="rTableHead"><strong>STLS</strong></div>
            <div className="rTableHead"><strong>BLKS</strong></div>
            <div className="rTableHead"><strong>FGM</strong></div>
            <div className="rTableHead"><strong>FGA</strong></div>
            <div className="rTableHead"><strong>FGPCT</strong></div>  
            <div className="rTableHead"><strong>FTM</strong></div>
            <div className="rTableHead"><strong>FTA</strong></div>
            <div className="rTableHead"><strong>FTPCT</strong></div>
            <div className="rTableHead"><strong>3PTM</strong></div>
            <div className="rTableHead"><strong>3PTA</strong></div>
            <div className="rTableHead"><strong>3PCT</strong></div>
          </div>

          <div className="rTableRow">
            <div className="rTableCell">{props.averages.pts}</div>
            <div className="rTableCell">{props.averages.rebs}</div>
            <div className="rTableCell">{props.averages.asts}</div>
            <div className="rTableCell">{props.averages.stls}</div>
            <div className="rTableCell">{props.averages.blks}</div>
            <div className="rTableCell">{props.averages.fgm}</div>
            <div className="rTableCell">{props.averages.fga}</div>
            <div className="rTableCell">{props.fgpct}</div>
            <div className="rTableCell">{props.averages.ftm}</div>
            <div className="rTableCell">{props.averages.fta}</div>
            <div className="rTableCell">{props.ftpct}</div>
            <div className="rTableCell">{props.averages.threesm}</div>
            <div className="rTableCell">{props.averages.threesa}</div>
            <div className="rTableCell">{props.threespct}</div>
          </div>
        </div>
      </div>

      <div className="player-game-chart">
        <h2>Line Example</h2>
        <Line data={gameChartData} />
      </div>

    </div>

  );
}
