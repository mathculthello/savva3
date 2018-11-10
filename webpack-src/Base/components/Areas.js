import AREAS_QUERY from "../graphql/areas.gql";
import React from "react";
import { Query } from "react-apollo";
import { Button } from 'reactstrap';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


const Areas = (props) => (

  <Query query={AREAS_QUERY}>
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;

      return (
        <>
        {data.allAreas.edges.map(item=>(
          <Link
          key={item.node.id}
          className={(item.node.id==props.area)?"mt-1 mr-1 btn btn-outline-secondary active":"mt-1 mr-1 btn btn-outline-secondary"}
          to={{ pathname: "/base/", search: "?area="+item.node.id }}
          >
            {item.node.title}
          </Link>
        ))}
        </>
      );
    }}
  </Query>



);


export default Areas;
