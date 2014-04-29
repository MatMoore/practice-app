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
