import React, {PureComponent}  from "react";

class RatingButton extends PureComponent{
    constructor(props){
        super(props);
    }

    render() {
        const {vote, onVoteClick} = this.props;

        const renderLinkContent = (vote)=>{
            if (vote > 0) {
                return (<span>+</span>)
            }
            return (<span>-</span>)
        }
        return (
            <button 
                type="button" 
                className="btn btn-default btn-sm"  
                onClick={onVoteClick.bind(null, vote)}>
                {renderLinkContent(vote)}
            </button>
        )
    } 
}
export default RatingButton;
