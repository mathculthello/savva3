import 'particles.js';


import React from "react";
import ReactDOM from "react-dom";

import { ApolloClient } from 'apollo-client';
import { HttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';

const client = new ApolloClient({
  // By default, this client will send queries to the
  //  `/graphql` endpoint on the same host
  // Pass the configuration option { uri: YOUR_GRAPHQL_API_URL } to the `HttpLink` to connect
  // to a different host
  link: new HttpLink(),
  cache: new InMemoryCache(),
});
import { ApolloProvider } from 'react-apollo';


import YouTube from 'react-youtube';




import { Query } from "react-apollo";
import gql from "graphql-tag";

class Video extends React.Component {


  render() {
    return(


  <Query
    query={gql`
      {randomUrl {
        title, url
      }}
    `}
  >
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;
      return (
        <div>
        <h4>{data.randomUrl.title}</h4>
          <YouTube
            videoId={YouTubeGetID(data.randomUrl.url)}
            onReady={loadParticles} />
        </div>
      );
    }}
  </Query>
)}


componentDidMount() {
//  setTimeout(loadParticles, 3000);
}

};


function loadParticles(){
  window.particlesJS.load('particles-js', '/static/particles.json');

}




const App = () => (
  <ApolloProvider client={client}>
    <div>
      <Video />
    </div>
  </ApolloProvider>
);










function YouTubeGetID(url){
  var ID = '';
  url = url.replace(/(>|<)/gi,'').split(/(vi\/|v=|\/v\/|youtu\.be\/|\/embed\/)/);
  if(url[2] !== undefined) {
    ID = url[2].split(/[^0-9a-z_\-]/i);
    ID = ID[0];
  }
  else {
    ID = url;
  }
    return ID;
}

export default App
