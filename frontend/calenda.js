import $ from 'jquery';
require('fullcalendar');

import './scss/_calenda.scss';

$(function() {

  // page is now ready, initialize the calendar...

  $('#calendar').fullCalendar({


    events: {
      url: '/api/events',
      type: 'GET',
      data: {
        format: 'json',
      },
      error: function() {
        alert('there was an error while fetching events!');
      },
      color: 'yellow',   // a non-ajax option
      textColor: 'black' // a non-ajax option
    }




  })

});
