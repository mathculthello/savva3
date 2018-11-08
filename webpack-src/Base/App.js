import 'particles.js';


import React from "react";
import ReactDOM from "react-dom";
import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { ApolloProvider } from 'react-apollo';
import YouTube from 'react-youtube';
import { Query } from "react-apollo";
import gql from "graphql-tag";

const client = new ApolloClient({
  // By default, this client will send queries to the
  //  `/graphql` endpoint on the same host
  // Pass the configuration option { uri: YOUR_GRAPHQL_API_URL } to the `HttpLink` to connect
  // to a different host
  link: new HttpLink(),
  cache: new InMemoryCache(),
});


const SET_QUERY = gql`
query myQuery ($areas: [ID]) {
  allUrls (areas: $areas){
    edges {
      node {
        id
        url
        title
      }
    }
  }
}
`;

const AREAS_QUERY = gql`
  {
    allAreas {
      edges {
        node {
          id
          title
        }
      }
    }
  }
`;




class Areas extends React.Component {


  render() {
    return(


  <Query
    query={AREAS_QUERY}
  >
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;



      return (
        <div>
        {data.allAreas.edges.map(item=>(
            <div
            key={item.node.id}
            id={item.node.id}
            onClick={this.props.change}
            className="btn btn-light">
            {item.node.title}
            </div>
          ))}
        </div>
      );
    }}
  </Query>



)}


};




class Set extends React.Component {


  render() {
    return(


  <Query
    query={SET_QUERY}
    variables={ {"areas": this.props.areas} }
  >
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;



      return (
        <div>
        {data.allUrls.edges.map(item=>(
            <div key={item.node.id}>
            <a href={item.node.url}>
            {item.node.title}
            </a>
            </div>
          ))}
        </div>
      );
    }}
  </Query>



)}


};




class App extends React.Component {

constructor(props) {
  super(props);
  this.state = {tag: null, area:null}
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
        <Areas change={this.onAreaSelected.bind(this)}/>
        </div>
        <div className="col-md-9">
        <Set areas={this.state.area} />
        </div>
      </div>
    </ApolloProvider>
  )
}
};





export default App
