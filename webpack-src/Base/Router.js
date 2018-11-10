import {default as Base} from './App'
import {default as Video} from './components/Video'
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { ApolloProvider } from 'react-apollo';
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
