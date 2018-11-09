import 'particles.js';


import React from "react";
import ReactDOM from "react-dom";

import { Query } from "react-apollo";



// Запросы к GraphQL

import Areas from './components/Areas';
import Set from './components/Set';

import { Container, Row, Col } from 'reactstrap';





class App extends React.Component {

state = {'area':''}

constructor(props){
  super(props);
  this.handleSelect=this.handleSelect.bind(this);
}

handleSelect(area){
  this.setState({'area':area});
}

render() {
  return(
      <Row>
        <Col md="3">
          <Areas onSelect={this.handleSelect}/>
        </Col>
        <Col md="9">
          <Set area={this.state.area}/>
        </Col>
      </Row>
  )
}
};





export default App
