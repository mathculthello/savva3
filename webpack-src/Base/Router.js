import {default as Base} from './App'
import {default as Video} from './components/Video'
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import { ApolloClient } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import React from "react";
import ReactDOM from "react-dom";



import client from './client';



const AppRouter = () => (
      <ApolloProvider client={client}>
      <Router>

<Switch>
        <Route path="/base/video/:id" component={Video} />
        <Route component={Base} />
        </Switch>
        </Router>

      </ApolloProvider>
);


export default AppRouter;
