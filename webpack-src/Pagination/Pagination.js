import React, {PureComponent}  from "react";
import Page from './Page';
import '../scss/pagination.scss';

const MAX_PAGES = 9;
const HALF_MAX = Math.floor(MAX_PAGES / 2);
const OFFSET = HALF_MAX - 2;

class Pagination extends PureComponent{
    render() {
        const {count, current, size} = this.props;
        let start = 1;
        let stop = count;
        let currentPosition = current;

        const pages = [];
        if (count > MAX_PAGES){
            if (current > HALF_MAX){
                pages.push(<Page page={ 1 } isLink={true}></Page>);
                pages.push(<Page page='...' isLink={false}></Page>);
                start = Math.min(current - OFFSET, count - MAX_PAGES + 3);
                currentPosition = HALF_MAX;
            }
            if (count - start > MAX_PAGES - 2){
                stop = Math.max(current + OFFSET, MAX_PAGES-2);
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
