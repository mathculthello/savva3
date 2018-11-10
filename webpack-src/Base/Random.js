import 'particles.js';

import YouTubeGetID from './helper';
import React from "react";
import ReactDOM from "react-dom";

import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';


import client from './client';
import { ApolloProvider } from 'react-apollo';


import YouTube from 'react-youtube';
import Loader from 'react-spinners/PacmanLoader';


const QUERY = gql`
  {randomUrl {
    title, url
  }}
`;

import { Query } from "react-apollo";
import gql from "graphql-tag";


const opts = {
  width: '100%',
}

const Video = () => (


  <Query query={QUERY}>
    {({ loading, error, data }) => {
      if (loading) return <Loader />;
      if (error) return <p>Error :(</p>;
      return (
        <>
        <p className="h4">{data.randomUrl.title}</p>
          <YouTube
            videoId={YouTubeGetID(data.randomUrl.url)}
            onReady={loadParticles}
            opts={opts} />
        </>
      );
    }}
  </Query>
);


function loadParticles(){
  window.particlesJS.load('particles-js', '/static/particles.json');

}




const App = () => (
  <ApolloProvider client={client}>
      <Video />
  </ApolloProvider>
);


export default App
