import React, {PureComponent}  from "react";
import Page from './Page';
import '../scss/pagination.scss';

const MAX_PAGES = 9;
const HALF_MAX = Math.floor(MAX_PAGES / 2);
const OFFSET = HALF_MAX - 2;

class Pagination extends PureComponent{
    constructor(){
        super();
        const parameters = window.location.search.replace(/^[?]/, '')
            .split('&')
            .filter(param => param.search(/^page[=]/i) < 0)
            .join('&');
        
        this.baseUrl = `${window.location.pathname}?`;
        if (parameters){
            this.baseUrl = `${this.baseUrl}${parameters}&`;
        }        
    }

    getPages(count, current){
        let start = 1;
        let stop = count;

        const pages = [];
        if (count > MAX_PAGES){
            if (current > HALF_MAX){
                pages.push(<Page baseUrl={this.baseUrl} page={ 1 } isLink={true}></Page>);
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
                <Page baseUrl={this.baseUrl} key={i} page={ i } isLink={i != current}></Page>
            )
        }

        if (stop != count){
            pages.push(<Page page='...' isLink={false}></Page>);
            pages.push(<Page baseUrl={this.baseUrl} page={ count } isLink={true}></Page>);
        }

        return pages;
    }

    render() {
        const {count, current} = this.props;
        if (count < 2)
            return;
            
        const pages = this.getPages(count, current);
        return (
            <ul>
                {pages}
            </ul>
        )
    } 
}
export default Pagination;
