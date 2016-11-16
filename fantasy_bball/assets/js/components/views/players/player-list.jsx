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
    <Table className="table" 
      filterable={['just_name', 'rebs']}
      sortable={['recent_form', 'fgpct', 'ftpct', 'pts', 'threesm', 'rebs', 'asts', 'stls', 'blks', 'tos']} 
      defaultSort={{column: 'recent_form', direction: 'desc'}} 
      defaultSortDescending
      itemsPerPage={100} pageButtonLimit={5}>>
      <Thead>
        <Th column="name">Name</Th>
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
        <Th column="" className="hidden">Just Name</Th> 
      </Thead>
      
      {props.players.map((player) => {
        return (
          <Tr key={player.id}>
            <Td column="name">
              <div><Link to={'/players/' + player.id}>{player.name}</Link> {player.position} {player.nba_team}</div>
            </Td>
            <Td column="recent_form">
              {player.recent_form}
            </Td>
            <Td column="fgpct">
              {player.stats.fgpct}
            </Td>
            <Td column="ftpct">
              {player.stats.ftpct}
            </Td>
            <Td column="pts">
              {player.stats.pts}
            </Td>
            <Td column="threesm">
              {player.stats.threesm}
            </Td>
            <Td column="rebs">
              {player.stats.rebs}
            </Td>
            <Td column="asts">
              {player.stats.asts}
            </Td>
            <Td column="stls">
              {player.stats.stls}
            </Td>
            <Td column="blks">
              {player.stats.blks}
            </Td>
            <Td column="tos">
              {player.stats.tos}
            </Td>
            <Td column="just_name" className="hidden">
              {player.name} {player.position} {player.nba_team}
            </Td>
          </Tr>
        );
      })}  

    </Table>
  );
}