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
}


const particlesjson=require('../particles.json');

const Video = () => (


  <Query query={QUERY}>
    {({ loading, error, data, refetch }) => {
      if (loading) return <Loader />;
      if (error) return <p>Error :(</p>;
      return (
        <>
          <h2>{data.randomUrl.title}</h2>
          <YouTube
            videoId={YouTubeGetID(data.randomUrl.url)}
            onReady={loadParticles}
            opts={opts} />

          <div className="text-center">
            <Button color="success" onClick={() => refetch()}>Другое видео</Button>
          </div>
        </>
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
