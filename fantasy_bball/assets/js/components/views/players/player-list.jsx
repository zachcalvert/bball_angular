import React from 'react';
import { Link } from 'react-router';
import Reactable from 'reactable';
var Table = Reactable.Table,
    Thead = Reactable.Thead,
    Th = Reactable.Th;

export default function(props) {

  return (
        <Table filterable={['short_name']} 
              sortable={['recent_form', 'fgpct', 'ftpct', 'pts', 'threesm', 'rebs', 'asts', 'stls', 'blks', 'tos']} 
              defaultSort={{column: 'recent_form', direction: 'desc'}} 
              defaultSortDescending
              className="table" data={props.players} 
              itemsPerPage={25} pageButtonLimit={10}
              previousPageLabel="Prev">

          <Thead>
            <Th className="player-list-name" column="short_name">Name</Th>
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

        </Table>
  );
}