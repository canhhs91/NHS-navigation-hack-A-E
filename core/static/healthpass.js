$(document).ready(function(){
    $('.plus-icon').click(function(){
        $(this).toggleClass('open');
        if ($(this).hasClass('open')){
            $('.information', $(this).closest('.summary-item')).slideDown();
        }else{
            $('.information', $(this).closest('.summary-item')).slideUp();
        }
    })
})