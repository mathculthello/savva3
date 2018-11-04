import './common.js';

import $ from 'jquery';
require('fullcalendar');

import './scss/calenda.scss';

$(function() {

  // page is now ready, initialize the calendar...

  $('#calendar').fullCalendar({


    events: {
      url: '/api/events/',
      type: 'GET',
      data: {
        format: 'json',
      },
      error: function() {
        alert('there was an error while fetching events!');
      },
      color: 'yellow',   // a non-ajax option
      textColor: 'black' // a non-ajax option
    },

    eventClick: function(event) {
      if (event.url) {
        window.open(event.url);
        return false;
      }
    },




  })

});
