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
          var link, icon;
          link=<a href={item.node.url} target="_blank">{item.node.title}</a>;

        if(item.node.url.includes('youtube')){
          icon=<i className="fab fa-youtube pr-2 youtube"></i>;
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
