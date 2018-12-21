import React, {PureComponent}  from "react";
import Page from './Page';
import '../scss/pagination.scss';

const MAX_PAGES = 10;

class Pagination extends PureComponent{
    render() {
        const {count, current, size} = this.props;
        let start = 1;
        let stop = count;
        let currentPosition = current;

        const pages = [];
        if (count > MAX_PAGES){
            if (current > MAX_PAGES - 2){
                pages.push(<Page page={ 1 } isLink={true}></Page>);
                pages.push(<Page page='...' isLink={false}></Page>);
                start = current - 3;
                currentPosition = 5;
            }
            if (count - current > MAX_PAGES - currentPosition){
                stop = current + 3;
            }
        }

        for (let i=start; i <= stop; i++){
            pages.push(
                <Page key={i} page={ i } isLink={i != current}></Page>
            )
        }

        if (stop != count){
            pages.push(<Page page='...' isLink={false}></Page>);
            pages.push(<Page page={ count } isLink={true}></Page>);
        }

        return (
            <ul>
                {pages}
            </ul>
        )
    } 
}
export default Pagination;
