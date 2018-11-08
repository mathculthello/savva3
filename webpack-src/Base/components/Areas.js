import AREAS_QUERY from "../graphql/areas.gql";
import React from "react";
import { Query } from "react-apollo";
import { Button } from 'reactstrap';


class Areas extends React.Component {

  state = {'id': null}

  handleSelect = (id) => {
    this.setState((state)=>{
      var new_id=(state.id==id)?null:id;
      this.props.onSelect(new_id)
      return ({'id':new_id});
    });

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

          <Button className="mt-2 d-block" outline  active={(item.node.id==this.state.id)?true:false} key={item.node.id} onClick={this.handleSelect.bind(this,item.node.id)}>
          {item.node.title}
          </Button>

        ))}
        </div>
      );
    }}
  </Query>



)}

};


export default Areas;
