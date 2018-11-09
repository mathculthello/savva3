import React from "react";
import ReactDOM from "react-dom";
import Areas from './components/Areas';
import Set from './components/Set';
import { Container, Row, Col } from 'reactstrap';

import qs from 'qs';

class App extends React.Component {

render() {
  let params=qs.parse(this.props.location.search,{ ignoreQueryPrefix: true });
//  let params = new URLSearchParams(this.props.location.search);

  return(
      <Row>
        <Col md="3">
          <Areas area={params.area}/>
        </Col>
        <Col md="9">
          <Set area={params.area}/>
        </Col>
      </Row>
  )
}
};





export default App
