import React from "react";
import {FaYoutube, FaCheckCircle} from 'react-icons/fa';

import { Link } from "react-router-dom";

const SetLink = (props) => {
  let icon, link, url, item, passed
  item = props.item;
  url = item.node.getAbsoluteUrl;
  if(item.node.passed){
    passed = <FaCheckCircle color="green" />
  }

  link=<a href={url} target="_blank">{item.node.title}</a>;
if(item.node.url.includes('youtube')){
  icon=<FaYoutube color="red" className="m-1"/>;
  //url="/base/video/"+item.node.id;
  link=<a href={url} title={item.node.title}>{item.node.title}</a>;
  //link=<Link to={url}>{item.node.title}</Link>
  //link=<Link to={url}>{item.node.title}</Link>
}
return(<tr key={item.node.id}>
  <td>{passed}{icon}{link}</td>
  </tr>);
}


export default SetLink;
