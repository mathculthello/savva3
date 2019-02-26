import 'particles.js';

import YouTubeGetID from './helper';
import React from "react";
import ReactDOM from "react-dom";

import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { Button } from 'reactstrap';

import client from '../client';
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
  height: '100%'
}


const particlesjson=require('../particles.json');

function truncate(value, limit = 25, completeWords = false, ellipsis = '...') {
  let truncated;
  if (value !== undefined && value != null && value.length > limit) {
    if (completeWords) {
      limit = value.substr(0, limit).lastIndexOf(' ');
    }
    truncated = `${value.substr(0, limit)}${ellipsis}`;
  } else {
    truncated = value;
  }
  return truncated;
}


const Video = () => (

  <Query query={QUERY}>
    {({ loading, error, data, refetch }) => {
      if (loading) return <Loader />;
      if (error) return <p>Error :(</p>;
      return (
        <div className="player">
          <h2>{truncate(data.randomUrl.title, 45)}</h2>
          <YouTube containerClassName="videoWrapper"
            videoId={YouTubeGetID(data.randomUrl.url)}
            onReady={loadParticles}
            opts={opts} />

          <div className="text-center next-button">
            <Button color="success" onClick={() => refetch()}>Другое видео</Button>
          </div>
        </div>
      );
    }}
  </Query>
);

function loadParticles(){
  console.log(particlesjson)
  window.particlesJS('particles-js', particlesjson);

}

const App = () => (
  <ApolloProvider client={client}>
      <Video />
  </ApolloProvider>
);


export default App
