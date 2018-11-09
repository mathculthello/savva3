import SET_QUERY from "../graphql/set.gql";
import React from "react";
import { Query } from "react-apollo";
import { Table } from 'reactstrap';

import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class Set extends React.Component {


  render() {
    return(


  <Query
    query={SET_QUERY}
    variables={ {"areas": this.props.area} }
  >
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;

      return (
        <Table>
        <tbody>
        {data.allUrls.edges.map(item=>{
          let icon, link, url
          url = item.node.getAbsoluteUrl;
          link=<a href={url} target="_blank">{item.node.title}</a>;

        if(item.node.url.includes('youtube')){
          icon=<i className="fab fa-youtube pr-2 youtube"></i>;
          //url="/base/"+item.node.id;
          //link=<Link to={url}>{item.node.title}</Link>
          link=<a href={url}>{item.node.title}</a>
        }
        return(<tr key={item.node.id}>
          <td>{icon}{link}</td>
          </tr>);
        })}
        </tbody>
        </Table>
      );
    }}
  </Query>



)}


};

export default Set;
