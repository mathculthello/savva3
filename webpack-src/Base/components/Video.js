
import QUERY from '../graphql/video.gql';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import { Query } from "react-apollo";
import React from "react";
import YouTube from 'react-youtube';

import { Container, Row, Col, Button } from 'reactstrap';


import YouTubeGetID from '../helper';

import createBrowserHistory from "history/createBrowserHistory";

const history = createBrowserHistory();


const Video = ({match}) => {

  const back = e => {
     e.stopPropagation();
     history.goBack();
   };

   const opts = {
      height: '500',
      width: '100%',
   }

   const query = (
     <Query query={QUERY}
     variables={{'id':match.params.id}}>
       {({ loading, error, data }) => {
         if (loading) return <p>Loading...</p>;
         if (error) return <p>Error :</p>;
           console.log(data)
         return (
           <div>

               <h2>{data.url.title}</h2>
               <YouTube
                 videoId={YouTubeGetID(data.url.url)}
                 opts={opts} />
           </div>
         );
       }}
         </Query>
   );

   const button = <Button color="warning" className="mt-1" onClick={back}>&larr; Назад</Button>

  return(
    <>
    <Row>
    <Col md={{size: 1}}>
      {button}
    </Col>
    <Col md={{size: 10}}>
      {query}
    </Col>
    </Row>
    </>


)}





export default Video;
