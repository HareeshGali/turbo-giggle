var main = function() {
  $('#btn-signin').on('click', function(event) {
    event.preventDefault();
    var post = $.post('/validateSession', $('#form-signin').serialize());
    post.done(function(data) {
      // TODO: Handle success and redirect to form
    });
    post.fail(function() {
      $('#signin-error').show();
    });
  });
};

$(document).ready(main);
