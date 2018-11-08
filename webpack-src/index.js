import './common.js';


import React from "react";
import ReactDOM from "react-dom";
import {default as Events} from './Events/App';
import {default as Video} from './Base/Random';


ReactDOM.render(
  <Video />,
  document.getElementById('video'),
);



ReactDOM.render(
  <Events />,
  document.getElementById('events')
);
