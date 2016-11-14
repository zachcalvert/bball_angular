import React from 'react';
import _ from 'lodash';
import Home from '../views/home';
import * as homeApi from '../../api/home-api';

const HomeContainer = React.createClass({

    getInitialState: function() {
        return {
            yesterday: null,
            top_performers: []
        };
    },

    componentDidMount: function() {
        homeApi.getHome().then(home => {
          this.setState({
            yesterday: home.yesterday,
            top_performers: home.top_performers
          })
        });
    },

    render: function() {
        console.log(this.state)
        return (
            <Home {...this.state} />
        );
    }
});

export default HomeContainer;