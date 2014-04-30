'use strict';

/*
 * Interact with the activity API
 */
var activityApi = {
    activityUrl: function(activityId) {
        return '/api/users/123/activities/' + activityId + '/';
    },

    /*
     * Record a checkin
     * @return a jquery promise
     */
    checkin: function (activityId) {
        return $.ajax({
            type: 'POST',
            url: this.activityUrl(activityId) + 'checkins/',
            dataType: 'json'
        });
    },

    get: function(activityId) {
        return $.ajax({
            type: 'GET',
            url: this.activityUrl(activityId),
            dataType: 'json'
        });
    }
};

function drawMonthWidget(selector, currentStreak) {
    var margin = {top: 49, right: 20, bottom: 20, left: 19},
        width = 960 - margin.right - margin.left,
        height = 136 - margin.top - margin.bottom,
        cellSize = 17;
    var now = new Date();
    var year = now.getFullYear();

    var day = d3.time.format('%w'),
        week = d3.time.format('%W'),
        months = d3.time.months(new Date(year, now.getMonth()), new Date(year, now.getMonth() + 1));

    var svg = d3.select(selector).selectAll('svg')
        .data(months)
        .enter().append('svg')
          .attr('width', width + margin.right + margin.left)
          .attr('height', height + margin.top + margin.bottom);

    var rectEnter = svg.selectAll('rect.day')
        .data(function(d, i) { return d3.time.days(d, new Date(d.getFullYear(), d.getMonth()+1, 1)); })
        .enter();

    rectEnter.append('rect')
          .attr('class', 'day')
          .attr('width', cellSize)
          .attr('height', cellSize)
          .attr('data-day', function(d) {return (7 + day(d) - 1) % 7;})
          .attr('data-week', function(d) {return (week(d) - week(new Date(d.getFullYear(),d.getMonth(),1)));})
          .attr('x', function(d) { return ((7 + day(d) - 1) % 7) * cellSize; })
          .attr('y', function(d) { return (week(d) - week(new Date(d.getFullYear(),d.getMonth(),1))) * cellSize; });

    // TODO: fix alignment
    rectEnter.append('text').text(function(d) {
            var daysago = moment(now).diff(moment(d), 'days');
            if(currentStreak > 0 && now >= d && daysago < currentStreak) {
                return '\u2714';
            } else {
                return '';
            }
          })
          .attr('width', cellSize)
          .attr('height', cellSize)
          .attr('x', function(d) { return ((7 + day(d) - 1) % 7) * cellSize + 9; })
          .attr('y', function(d) { return (week(d) - week(new Date(d.getFullYear(),d.getMonth(),1))) * cellSize + 14; })
          .attr('class', function() {return 'selected-day-text';})
}
