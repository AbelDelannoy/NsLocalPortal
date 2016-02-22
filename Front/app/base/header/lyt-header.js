/**

	TODO:
	- header class hide : see router.js & app.js

**/

define(['marionette', 'config','i18n'],
function(Marionette, config) {
  'use strict';
  return Marionette.LayoutView.extend({
    template: 'app/base/header/tpl-header.html',
    className: 'header',
    events: {
      'click #logout': 'logout',
    },

    ui: {
      'user': '#user'
    },

    initialize: function() {
      this.model = window.app.user;
    },

    logout: function() {
      $.ajax({
        context: this,
        cache: false,
        url: config.coreUrl + 'security/logout?nocache=' + Date.now(),
      }).done(function() {
        Backbone.history.navigate('login', {trigger: true});
      });
    },

    onShow: function() {
      this.ui.user.html(this.model.get('fullname'));
      this.$el.i18n();
    },
  });
});
