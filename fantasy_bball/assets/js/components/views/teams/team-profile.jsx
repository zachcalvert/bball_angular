import React from 'react';
import { Link } from 'react-router';
import Reactable from 'reactable';
var Table = Reactable.Table,
    Thead = Reactable.Thead,
    Th = Reactable.Th,
    Td = Reactable.Td,
    Tr = Reactable.Tr;

export default function(props) {
  return (
    <div className="team-profile">
      <header className="league-header">
        <ul>
          <li><Link to={"/leagues/" + props.leagueId} activeClassName="active">League Home</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/players"} activeClassName="active">Free Agents</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/matchups"} activeClassName="active">Matchups</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/standings"} activeClassName="active">Standings</Link></li>
          <li><Link to={"/leagues/" + props.leagueId + "/schedule"} activeClassName="active">Schedule</Link></li>
        </ul>
      </header>

      <img src={props.imageUrl} />
      <div className="details">
        <h1>{props.name}</h1>
        <p>Manager: {props.owner}</p>
        <p>Record: {props.record}</p>

        <Table className="table" 
          sortable={['recent_form', 'fgpct', 'ftpct', 'pts', 'threesm', 'rebs', 'asts', 'stls', 'blks', 'tos']} 
          defaultSort={{column: 'recent_form', direction: 'desc'}} 
          defaultSortDescending>
          <Thead>
            <Th className="player-header-name" column="name">Name</Th>
            <Th column="recent_form">Form</Th>
            <Th column="fgpct">FGPCT</Th>
            <Th column="ftpct">FTPCT</Th>
            <Th column="pts">PPG</Th>
            <Th column="threesm">3PG</Th>
            <Th column="rebs">RPG</Th>
            <Th column="asts">APG</Th>
            <Th column="stls">SPG</Th>
            <Th column="blks">BPG</Th>
            <Th column="tos">TOPG</Th>
          </Thead>
          
          {props.players.map((player, i) => {
            return (
              <Tr>
                <Td column="name">
                  <li><Link to={'/players/' + player.id}>{player.name}</Link> {player.position} {player.nba_team}</li>
                </Td>
                <Td column="recent_form">
                  {player.recent_form}
                </Td>
                <Td column="fgpct">
                  {player.fgpct}
                </Td>
                <Td column="ftpct">
                  {player.ftpct}
                </Td>
                <Td column="pts">
                  {player.pts}
                </Td>
                <Td column="threesm">
                  {player.threesm}
                </Td>
                <Td column="rebs">
                  {player.rebs}
                </Td>
                <Td column="asts">
                  {player.asts}
                </Td>
                <Td column="stls">
                  {player.stls}
                </Td>
                <Td column="blks">
                  {player.blks}
                </Td>
                <Td column="tos">
                  {player.tos}
                </Td>
              </Tr>
            );
          })}  

        </Table>

      </div>
    </div>
  );
}
