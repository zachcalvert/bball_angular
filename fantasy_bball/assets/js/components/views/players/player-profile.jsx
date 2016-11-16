import React from 'react';
import { Link } from 'react-router';
import {Line} from 'react-chartjs-2';

export default function(player) {
  var gameChartData = {
    "labels": player.chart_games,
    "datasets": [
      {
        "label": 'Recent Form',
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
        "data": player.chart_scores
      }
    ]
  }

  var gameChartOptions = {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true,
                    max: 10,
                    steps: 1
                }
            }]
        }
    }

  return (<div className="player-profile">

      <div className="player-info">
        
        <div className="player-image">
          <img src={player.imageUrl} />
        </div>
        
        <h4>{player.name}</h4>
        <p>{player.nbaTeam}  &#8226; {player.position}</p>
      </div>

      <div className="player-details">
        <div className="player-quick-stats">
          <strong>2016-17</strong>
          <div className="rTable">
            <div className="rTableRow">
              <div className="rTableHead"><strong>FG%</strong></div>
              <div className="rTableHead"><strong>FT%</strong></div>
              <div className="rTableHead"><strong>PTS</strong></div>
              <div className="rTableHead"><strong>REBS</strong></div>
              <div className="rTableHead"><strong>ASTS</strong></div>
              <div className="rTableHead"><strong>STLS</strong></div>
              <div className="rTableHead"><strong>BLKS</strong></div>
            </div>
            <div className="rTableRow">
              <div className="rTableCell">{player.averages.fgpct}</div>
              <div className="rTableCell">{player.averages.ftpct}</div>
              <div className="rTableCell">{player.averages.pts}</div>
              <div className="rTableCell">{player.averages.rebs}</div>
              <div className="rTableCell">{player.averages.asts}</div>
              <div className="rTableCell">{player.averages.stls}</div>
              <div className="rTableCell">{player.averages.blks}</div>
            </div>
          </div>
        </div>

        <strong>Recent Notes</strong>
        <div className="player-notes">
          <p>{player.date}</p>
          <p>{player.report}</p>
          <p>{player.impact}</p>
        </div>
      </div>

      <div className="player-game-chart">
        <Line data={gameChartData} options={gameChartOptions} />
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
            <div className="rTableCell">{player.totals.pts}</div>
            <div className="rTableCell">{player.totals.rebs}</div>
            <div className="rTableCell">{player.totals.asts}</div>
            <div className="rTableCell">{player.totals.stls}</div>
            <div className="rTableCell">{player.totals.blks}</div>
            <div className="rTableCell">{player.totals.fgm}</div>
            <div className="rTableCell">{player.totals.fga}</div>
            <div className="rTableCell">{player.averages.fgpct}</div>
            <div className="rTableCell">{player.totals.ftm}</div>
            <div className="rTableCell">{player.totals.fta}</div>
            <div className="rTableCell">{player.averages.ftpct}</div>
            <div className="rTableCell">{player.totals.threesm}</div>
            <div className="rTableCell">{player.totals.threesa}</div>
            <div className="rTableCell">{player.averages.threespct}</div>
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
            <div className="rTableCell">{player.averages.pts}</div>
            <div className="rTableCell">{player.averages.rebs}</div>
            <div className="rTableCell">{player.averages.asts}</div>
            <div className="rTableCell">{player.averages.stls}</div>
            <div className="rTableCell">{player.averages.blks}</div>
            <div className="rTableCell">{player.averages.fgm}</div>
            <div className="rTableCell">{player.averages.fga}</div>
            <div className="rTableCell">{player.averages.fgpct}</div>
            <div className="rTableCell">{player.averages.ftm}</div>
            <div className="rTableCell">{player.averages.fta}</div>
            <div className="rTableCell">{player.averages.ftpct}</div>
            <div className="rTableCell">{player.averages.threesm}</div>
            <div className="rTableCell">{player.averages.threesa}</div>
            <div className="rTableCell">{player.averages.threespct}</div>
          </div>
        </div>
      </div>
    </div>
  );
}
