import React from "react";
import ReactDOM from "react-dom";
import Areas from './components/Areas';
import Set from './components/Set';
import { Container, Row, Col } from 'reactstrap';



class App extends React.Component {

render() {
  let params = new URLSearchParams(this.props.location.search);

  console.log(params.get('area'))
  return(
      <Row>
        <Col md="3">
          <Areas area={params.get('area')}/>
        </Col>
        <Col md="9">
          <Set area={params.get('area')}/>
        </Col>
      </Row>
  )
}
};





export default App
