import React from 'react';
import { Link } from 'react-router';

const MainLayout = React.createClass({
  render: function() {
    return (
      <div className="app">
        <header className="primary-header">
          <ul>
            <li><Link to="/" activeClassName="active">Home</Link></li>
            <li><Link to="/leagues" activeClassName="active">Leagues</Link></li>
            <li><Link to="/players" activeClassName="active">Players</Link></li>
          </ul>
        </header>
        <aside className="primary-aside"></aside>
        <div className="main">
          {this.props.children}
        </div>
      </div>
    );
  }
});

export default MainLayout;
