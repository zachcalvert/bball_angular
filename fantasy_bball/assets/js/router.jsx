import React from 'react';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';

// Layouts
import MainLayout from './components/main-layout';
import SearchLayout from './components/search-layout';
import LeagueLayout from './components/league-layout';

// Pages
import HomeContainer from './components/containers/home-container';
import LeagueListContainer from './components/containers/leagues/league-list-container';
import LeagueProfileContainer from './components/containers/leagues/league-profile-container';
import LeagueMatchupsContainer from './components/containers/leagues/league-matchups-container';

import TeamProfileContainer from './components/containers/teams/team-profile-container';

import PlayerListContainer from './components/containers/players/player-list-container';
import PlayerProfileContainer from './components/containers/players/player-profile-container';


export default (
  <Router history={browserHistory}>
    <Route component={MainLayout}>
      <Route path="/" component={HomeContainer} />

        <Route path="leagues">
          <IndexRoute component={LeagueListContainer} />


          <Route component={LeagueLayout}>
            <Route path=":leagueId" component={LeagueProfileContainer}>
              <Route path="matchups" component={LeagueMatchupsContainer} />
            </Route>
           </Route>
        </Route>

        <Route path="leagues/:leagueId/teams/:teamId" component={TeamProfileContainer} />
        <Route path="leagues/:leagueId/free_agents" component={PlayerListContainer} />
        <Route path="players/:playerId" component={PlayerProfileContainer} />
        

      <Route path="players">
        <IndexRoute component={PlayerListContainer} />
        <Route path=":playerId" component={PlayerProfileContainer} />
      </Route>

    </Route>
  </Router>
);