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

import { Container, Row, Col } from 'reactstrap';





class App extends React.Component {

state = {'area':''}

constructor(props){
  super(props);
  this.handleSelect=this.handleSelect.bind(this);
}

handleSelect(area){
  this.setState({'area':area});
}

render() {
  return(
    <ApolloProvider client={client}>
      <Row>
        <Col md="3">
          <Areas onSelect={this.handleSelect}/>
        </Col>
        <Col md="9">
          <Set area={this.state.area}/>
        </Col>
      </Row>
    </ApolloProvider>
  )
}
};





export default App
