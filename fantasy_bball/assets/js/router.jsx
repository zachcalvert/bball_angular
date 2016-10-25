import React from 'react';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';

// Layouts
import MainLayout from './components/main-layout';
import SearchLayout from './components/search-layout';
import LeagueLayout from './components/league-layout';

// Pages
import Home from './components/home';
import LeagueListContainer from './components/containers/league-list-container';
import LeagueProfileContainer from './components/containers/league-profile-container';

import TeamProfileContainer from './components/containers/team-profile-container';

import PlayerListContainer from './components/containers/player-list-container';
import PlayerProfileContainer from './components/containers/player-profile-container';
import LeagueMatchupsContainer from './components/containers/league-matchups-container';


export default (
  <Router history={browserHistory}>
    <Route component={MainLayout}>
      <Route path="/" component={Home} />

        <Route path="leagues">
          <IndexRoute component={LeagueListContainer} />

          <Route component={LeagueLayout}>
            <Route path=":leagueId" component={LeagueProfileContainer}>
              <Route path="players" component={PlayerListContainer} />
              <Route path="matchups" component={LeagueMatchupsContainer} />
            </Route>
           </Route>
        </Route>

        <Route path="leagues/:leagueId/teams/:teamId" component={TeamProfileContainer} />
        <Route path="players/:playerId" component={PlayerProfileContainer} />
        

      <Route path="players">
        <IndexRoute component={PlayerListContainer} />
      </Route>

    </Route>
  </Router>
);