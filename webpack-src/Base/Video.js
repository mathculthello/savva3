
import QUERY from './graphql/video.gql';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import { Query } from "react-apollo";
import React from "react";
import YouTube from 'react-youtube';

import { Container, Row, Col, Button } from 'reactstrap';


import YouTubeGetID from './helper';

import createBrowserHistory from "history/createBrowserHistory";

const history = createBrowserHistory();


const Video = ({match}) => {

  let back = e => {
     e.stopPropagation();
     history.goBack();
   };

  return(
    <Container>
    <Row>
    <Col md={{size: 8, offset: 2}}>
          <Button color="warning" onClick={back}>&larr; Назад</Button>
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
              videoId={YouTubeGetID(data.url.url)} />
        </div>
      );
    }}
      </Query>

    </Col>
    </Row>
    <Row>
    <Col>
    </Col>
    </Row>
    </Container>


)}


export default Video;
