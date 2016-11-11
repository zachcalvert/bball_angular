import React from 'react';
import { Link } from 'react-router';
import Reactable from 'reactable';
var Table = Reactable.Table,
    Thead = Reactable.Thead,
    Th = Reactable.Th;

export default function(props) {

  return (
       <Table filterable={['short_name']} 
              sortable={[
                {
                  column: 'recent_form',
                  direction: 'desc'
                },
                {
                  column: 'pts',
                  direction: 'desc'
                },
                {
                  column: 'rebs',
                  direction: 'desc'
                },
                {
                  column: 'asts',
                  direction: 'desc'
                },
                {
                  column: 'stls',
                  direction: 'desc'
                },
                {
                  column: 'blks',
                  direction: 'desc'
                },
            ]} defaultSort={{column: 'recent_form', direction: 'desc'}} defaultSortDescending

      className="table" data={props.players} 
       itemsPerPage={50} pageButtonLimit={5}>
        <Thead>
          <Th column="short_name">Name</Th>
          <Th column="recent_form">Form</Th>
          <Th column="pts">PPG</Th>
          <Th column="rebs">RPG</Th>
          <Th column="asts">APG</Th>
          <Th column="stls">SPG</Th>
          <Th column="blks">BPG</Th>
        </Thead>
        </Table>
  );
}