import SET_QUERY from "../graphql/set.gql";
import React from "react";
import { Query } from "react-apollo";
import { Table } from 'reactstrap';


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
          var link;
        if(item.node.url.includes('youtube')){
          link=<div><i className="fab fa-youtube pr-2 youtube"></i><a href={item.node.url}>{item.node.title}</a></div>;
        } else {
          link=<a href={item.node.url}>{item.node.title}</a>;
        }
        return(<tr key={item.node.id}>
          <td>{link}</td>
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
