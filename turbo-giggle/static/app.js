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

  $('#docForm').ready(function(event) {
    var post = $.get('/docForm', function(data) {
      var response = JSON.parse(data)[0];
      console.log(response);
      for (var col in response) {
        console.log(col);
        $('#' + col).val(response[col]);
      }
    });
    post.fail(function(data) {
      console.error("FAIL:" + data);
    });
  });
};

$(document).ready(main);
