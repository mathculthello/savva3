import AREAS_QUERY from "../graphql/areas.gql";
import React from "react";
import { Query } from "react-apollo";


class Areas extends React.Component {

  constructor(props){
    super(props);
    this.click=this.click.bind(this);
  }


  click(e){
    this.setState({'area': e.target.id})
    this.props.change(e);
  }

  render() {
    return(

  <Query query={AREAS_QUERY}>
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;

      return (
        <div>
        {data.allAreas.edges.map(item=>(
          <div
          key={item.node.id}
          id={item.node.id}
          onClick={this.click}
          className="btn btn-light">
          {item.node.title}
          </div>
        ))}
        </div>
      );
    }}
  </Query>



)}

};


export default Areas;
