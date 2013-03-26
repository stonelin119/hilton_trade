!function ($) {
$(function(){
  // carousel demo
  $('#myCarousel').carousel()
})
}(window.jQuery)

$(document).ready(function(){
    $(".dropdown-menu li a").each(function(){
        $(this).attr('href', 'javascript:void(0);')
            .bind('click', function(){
                var lang = $(this).attr("lang");
                $.post("/i18n/setlang/", { language: lang })
                .done(function(data) {
                    window.location.replace(window.location.href);
                });
            });
    });
});
