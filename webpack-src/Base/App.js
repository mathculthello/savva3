import 'particles.js';


import React from "react";
import ReactDOM from "react-dom";
import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { ApolloProvider } from 'react-apollo';
import YouTube from 'react-youtube';
import { Query } from "react-apollo";

const client = new ApolloClient({
  // By default, this client will send queries to the
  //  `/graphql` endpoint on the same host
  // Pass the configuration option { uri: YOUR_GRAPHQL_API_URL } to the `HttpLink` to connect
  // to a different host
  link: new HttpLink(),
  cache: new InMemoryCache(),
});

// Запросы к GraphQL

import Areas from './components/Areas';
import Set from './components/Set';






class App extends React.Component {

constructor(props) {
  super(props);
  this.state = {tag: null, area:null};
  this.onAreaSelected=this.onAreaSelected.bind(this);
}

onAreaSelected({target}) {
  console.log(target.id);
  this.setState(()=>({area: target.id}))
}

render() {
  return(
    <ApolloProvider client={client}>
      <div className="row">
        <div className="col-md-3">
        <Areas area={this.state.area} change={this.onAreaSelected}/>
        </div>
        <div className="col-md-9">
        <Set area={this.state.area} />
        </div>
      </div>
    </ApolloProvider>
  )
}
};





export default App
