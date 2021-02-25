!(function($) {
  "use strict";

  // Preloader
  $(window).on('load', function() {
    if ($('#preloader').length) {
      $('#preloader').delay(100).fadeOut('slow', function() {
        $(this).remove();
      });
    }
  });

//file uploader
  $('#attachment .fileinput').on('change', function () {
    var file = $(this).prop('files')[0];
    $(this).closest('#attachment').find('.filename').text(file.name);
  });

  $(document).ready(function(){ 
    $("#id_username").attr('placeholder', 'メールアドレス'); 
    $("#id_password").attr('placeholder', 'パスワード'); 
   }); 



})(jQuery);
