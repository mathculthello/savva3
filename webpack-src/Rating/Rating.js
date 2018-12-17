import React, {PureComponent}  from "react";
import '../scss/rating.scss';

class Rating extends PureComponent{

    constructor(props){
        super(props);
        this.state = {
            rating: this.props.rating,
            successAnimation: false,
            errorAnimation: false,
        }
    }

    onVoteClick(value){
        const { iid, rating_type } = this.props;
        this.setState(Object.assign({}, this.state, {
            successAnimation: false,
            errorAnimation: false,
        }));
        return fetch('/rating/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
                "X-CSRFToken": this.props.csrf
            },
            body: JSON.stringify({
                iid,
                rating_type,
                value
            }), 
        })
        .then(response => {
            if (response.status != 200){
                return Promise.reject(response.json());
            }
            return response.json();
        })
        .then(response => {
            const {rating} = response;
            this.setState(Object.assign({}, this.state, {
                rating,
                successAnimation: true
            }));
        })
        .catch(()=>{
            this.setState(Object.assign({}, this.state, {
                errorAnimation: true
            }));
        })
    }

    render() {
        const {rating, successAnimation, errorAnimation} = this.state;
        let className = 'rating';
        if (rating > 0){
            className += ' green';
        }
        if (rating < 0){
            className += ' red';
        }
        if (successAnimation){
            className += ' pop-up';
        }
        if (errorAnimation){
            className += ' error';
        }
        
        const renderLinkContent = (vote)=>{
            if (vote > 0) {
                return (<span>+</span>)
            }
            return (<span>-</span>)
        }
        const renderLink = (vote) => {
            return (
                <button 
                    type="button" 
                    className="btn btn-default btn-sm"  
                    onClick={this.onVoteClick.bind(this, vote)}>
                    {renderLinkContent(vote)}
                </button>
            )
        }
        return (
            <div>
                {renderLink(-1)}
                <span className={className}>
                    <b>{rating}</b>
                </span>
                {renderLink(1)}
            </div>
        )
    } 
}
export default Rating;
