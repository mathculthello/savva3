import React, {PureComponent}  from "react";

class Page extends PureComponent{
    render() {
        const {page, isLink, baseUrl} = this.props;
        const path = `${baseUrl}page=${page}`;

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
