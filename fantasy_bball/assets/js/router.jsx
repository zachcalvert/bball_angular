import React from 'react';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';

// Layouts
import MainLayout from './components/main-layout';
import SearchLayout from './components/search-layout';

// Pages
import Home from './components/home';
import LeagueListContainer from './components/containers/league-list-container';
import LeagueProfileContainer from './components/containers/league-profile-container';
import PlayerList from './components/player-list';

export default (
  <Router history={browserHistory}>
    <Route component={MainLayout}>
      <Route path="/" component={Home} />

      <Route path="leagues">
        <Route component={SearchLayout}>
          <IndexRoute component={LeagueListContainer} />
        </Route>
        <Route path=":leagueId" component={LeagueProfileContainer} />
      </Route>

      <Route path="players">
        <Route component={SearchLayout}>
          <IndexRoute component={PlayerList} />
        </Route>
      </Route>

    </Route>
  </Router>
);