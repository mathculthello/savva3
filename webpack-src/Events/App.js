import React from "react";
import ReactDOM from "react-dom";


import { Query } from "react-apollo";
import Loader from 'react-spinners/PacmanLoader';
import Event from './components/Event';

import EVENTS_QUERY from "./graphql/events.gql";



import { ApolloProvider } from 'react-apollo';
import client from '../client';


const Vam = ()=> (<p>hello</p>)



class App extends React.Component {

  render() {
    return (
      <ApolloProvider client={client}>

        <Query
          query={EVENTS_QUERY}
        >
          {({ loading, error, data }) => {
            if (loading) return <Loader/>;
            if (error) return <p>Error :(</p>;

            return (
              <>
              {data.allEvents.edges.map(event=>(

                <Event
                key={event.node.id}
                start={event.node.start}
                city={event.node.city}
                title={event.node.title}
                place={event.node.place}
                address={event.node.address}
                comment={event.node.comment}/>

              ))}
              </>
            );
          }}
        </Query>
      </ApolloProvider>
    );
  };
};


export default App;
