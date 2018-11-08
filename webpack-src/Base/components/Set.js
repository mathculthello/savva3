import SET_QUERY from "../graphql/set.gql";
import React from "react";
import { Query } from "react-apollo";


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
        <div>
        {data.allUrls.edges.map(item=>(
            <div key={item.node.id}>
            <a href={item.node.url}>
            {item.node.title}
            </a>
            </div>
          ))}
        </div>
      );
    }}
  </Query>



)}


};

export default Set;
