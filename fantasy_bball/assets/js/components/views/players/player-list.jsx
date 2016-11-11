import React from 'react';
import { Link } from 'react-router';
import Reactable from 'reactable';
var Table = Reactable.Table;

export default function(props) {
  return (
       <Table sortable={true} className="table" data={props.players} />
  );
}