var main = function() {
  $('#btn-signin').on('click', function(e) {
    e.preventDefault();
    var post = $.post('/validateSession', $('#form-signin').serialize());
    post.done(function(data) {
      $('#signin-error').hide();
      // TODO: Handle success and redirect to form
      window.location.href = '/form';
    });
    post.fail(function(err) {
      $('#signin-error').show();
      console.error(err);
    });
  });

  $('#docForm').ready(function(e) {
    var post = $.get('/docForm', function(data) {
      var response = JSON.parse(data)[0];
      console.log(response);
      for (var col in response) {
        $('#' + col).val(response[col]);
      }
    });
    post.fail(function(data) {
      console.error("Failed to get form data:" + data);
    });
  });

  $('#form-submit').on('click', function(e) {
    e.preventDefault();
    var cols = ['patientID', 'name', 'dateofBirth', 'primaryPhys', 'phoneNum', 'medHistory', 'prescribeMeds'];
    requestData = {};
    for (var i = 0; i < cols.length; i++) {
      requestData[cols[i]] = $('#' + cols[i]).val();
    }
    requestData.patientID = 1;

    console.log(requestData);
    var post = $.post('/docForm', JSON.stringify(requestData));
    post.done(function(data) {
      $('#signin-success').show();
      $('#form-error').hide();
      console.log(data);
      window.location.href = '/';
    });
    post.fail(function(err) {
      $('#signin-success').hide();
      $('#form-error').show();
      console.error(err);
    });
  });
};

$(document).ready(main);
