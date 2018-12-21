import React, {PureComponent}  from "react";

class Page extends PureComponent{
    render() {
        const {page, isLink} = this.props;
        const path = `${window.location.pathname}?page=${page}`;

        const getItem = ()=>{
            if (!isLink)
                return (<span>{page}</span>)
            return <a href={path}> {page} </a>
        }

        return (
            <li className="page-item">
                {getItem()}
            </li>
        )
    } 
}
export default Page;
