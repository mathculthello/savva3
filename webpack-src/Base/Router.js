import {default as Base} from './App'
import {default as Video} from './Video'
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import { ApolloClient } from 'apollo-client';
import { ApolloProvider } from 'react-apollo';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import React from "react";
import ReactDOM from "react-dom";

const client = new ApolloClient({
  // By default, this client will send queries to the
  //  `/graphql` endpoint on the same host
  // Pass the configuration option { uri: YOUR_GRAPHQL_API_URL } to the `HttpLink` to connect
  // to a different host
  link: new HttpLink(),
  cache: new InMemoryCache(),
});



const AppRouter = () => (
  <Router>
      <ApolloProvider client={client}>
        <Route path="/base/" exact component={Base} />
        <Route path="/base/:id" exact component={Video} />
      </ApolloProvider>
  </Router>
);


export default AppRouter;
