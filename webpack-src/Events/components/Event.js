
import React from "react";
import ReactDOM from "react-dom";
const ReactMarkdown = require('react-markdown');
import {Collapse, Button } from 'reactstrap';
import moment from 'moment';
moment.locale('ru');




class Event extends React.Component {

  constructor(props){
    super(props);
    this.toggle = this.toggle.bind(this);
    this.state = { collapse: false };

  }

  toggle() {
  this.setState({ collapse: !this.state.collapse });
  }

  HeaderDisabled() {
    return(
        <div>
                {this.props.title}
        </div>
    )
  }

  HeaderActive() {
    return(
      <div className="eventButton" onClick={this.toggle}>
              {this.props.title}
      </div>
    )
  }

  Collapse() {
    return (
      <Collapse isOpen={this.state.collapse}>
      <div>{this.props.place}</div>
      <div>{this.props.address}</div>
      <ReactMarkdown source={this.props.comment} />
      </Collapse>
    )
  }

  Card() {
    let button=this.HeaderActive();
    if(!this.props.title||!this.props.place&!this.props.address&!this.props.comment){
      button = this.HeaderDisabled();
    }
    return(
      <div>
      {button}
      {this.Collapse()}
      </div>
    )
  }

  render() {
    let format;
    if(moment(this.props.start).utc().format('H')==0){
      format='LL';
    } else {
      format='LLL';
    }

    return(
      <div className="row border-bottom pt-1 pb-2">
        <div className="col-md-2 date-nowrap">
        {moment(this.props.start).utc().format(format)}
        </div>
        <div className="col-md-1 city-nowrap">
        {this.props.city}
        </div>
        <div className="col">
        {this.Card()}
        </div>
      </div>
    )
  }
}

export default Event;
