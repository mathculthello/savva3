import React, {PureComponent}  from "react";

class RatingValue extends PureComponent{
    constructor(props){
        super(props);
    }

    getSign(rating){
        if (rating > 0){
            return '+'
        }
        return '';
    }

    render() {
        const {rating, successAnimation, errorAnimation} = this.props;
        const sign = this.getSign(rating);
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
        
        return (
            <span className={className}>
                <b>{sign}{rating}</b>
            </span>
        )
    } 
}

export default RatingValue;
