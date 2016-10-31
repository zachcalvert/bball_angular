import React from 'react';
import { Link } from 'react-router';

export default function(props) {
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
              <div className="rTableCell">{props.avg_pts}</div>
              <div className="rTableCell">{props.avg_rebs}</div>
              <div className="rTableCell">{props.avg_asts}</div>
              <div className="rTableCell">{props.avg_stls}</div>
              <div className="rTableCell">{props.avg_blks}</div>
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
            <div className="rTableCell">{props.total_pts}</div>
            <div className="rTableCell">{props.total_rebs}</div>
            <div className="rTableCell">{props.total_asts}</div>
            <div className="rTableCell">{props.total_stls}</div>
            <div className="rTableCell">{props.total_blks}</div>
            <div className="rTableCell">{props.total_fgm}</div>
            <div className="rTableCell">{props.total_fga}</div>
            <div className="rTableCell">{props.fgpct}</div>
            <div className="rTableCell">{props.total_ftm}</div>
            <div className="rTableCell">{props.total_fta}</div>
            <div className="rTableCell">{props.ftpct}</div>
            <div className="rTableCell">{props.total_threesm}</div>
            <div className="rTableCell">{props.total_threesa}</div>
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
            <div className="rTableCell">{props.avg_pts}</div>
            <div className="rTableCell">{props.avg_rebs}</div>
            <div className="rTableCell">{props.avg_asts}</div>
            <div className="rTableCell">{props.avg_stls}</div>
            <div className="rTableCell">{props.avg_blks}</div>
            <div className="rTableCell">{props.avg_fgm}</div>
            <div className="rTableCell">{props.avg_fga}</div>
            <div className="rTableCell">{props.fgpct}</div>
            <div className="rTableCell">{props.avg_ftm}</div>
            <div className="rTableCell">{props.avg_fta}</div>
            <div className="rTableCell">{props.ftpct}</div>
            <div className="rTableCell">{props.avg_threesm}</div>
            <div className="rTableCell">{props.avg_threesa}</div>
            <div className="rTableCell">{props.threespct}</div>
          </div>
        </div>
      </div>



    </div>

  );
}
