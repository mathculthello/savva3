import React, {PureComponent}  from "react";
import RatingValue from './RatingValue';
import RatingButton from './RatingButton';
import '../scss/rating.scss';

class Rating extends PureComponent{

    constructor(props){
        super(props);
        this.state = {
            rating_positive: this.props.rating_positive,
            rating_negative: this.props.rating_negative,
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
            const { rating_positive, rating_negative } = response;
            this.setState(Object.assign({}, this.state, {
                rating_positive, rating_negative,
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
        const {rating_positive, rating_negative, successAnimation, errorAnimation} = this.state;

        return (
            <div className="rating-container">
                <RatingButton vote={-1} onVoteClick={this.onVoteClick.bind(this)}></RatingButton>
                <div className="rating-container--value-container">
                    <div className="rating-container--value-container__overall">
                        <RatingValue 
                            rating={rating_positive+rating_negative}
                            successAnimation={successAnimation} 
                            errorAnimation={errorAnimation}
                        ></RatingValue>
                    </div>
                    <div className="
                    rating-container--value-container__parts">
                        <RatingValue 
                            rating={rating_negative}
                            successAnimation={successAnimation} 
                            errorAnimation={false}
                        ></RatingValue>
                        <RatingValue 
                            rating={rating_positive}
                            successAnimation={successAnimation} 
                            errorAnimation={false}
                        ></RatingValue>
                    </div>
                </div>
                <RatingButton vote={1} onVoteClick={this.onVoteClick.bind(this)}></RatingButton>
            </div>
        )
    } 
}
export default Rating;
