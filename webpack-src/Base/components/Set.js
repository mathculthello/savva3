import SET_QUERY from "../graphql/set.gql";
import React from "react";
import { Query } from "react-apollo";
import { Table } from 'reactstrap';

import Loader from 'react-spinners/PacmanLoader';

import SetLink from './SetLink';

class Set extends React.Component {


  render() {
    return(


  <Query
    query={SET_QUERY}
    variables={ {"areas": this.props.area} }
  >
    {({ loading, error, data }) => {
      if (loading) return <Loader/>;
      if (error) return <p>Error :(</p>;

      return (
        <Table>
        <tbody>
        {data.allUrls.edges.map(item=>(<SetLink item={item} key={item.node.id} />))}
        </tbody>
        </Table>
      );
    }}
  </Query>



)}


};





export default Set;
