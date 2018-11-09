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
        return(<tr key={item.node.id}>
          <td><a href={item.node.url}>{item.node.title}</a></td>
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
