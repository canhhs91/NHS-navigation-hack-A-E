$(document).ready(function(){
    step = 1;
    max_step = 3;
    $('.start-btn, .start-text').click(function(){
        location.href = '/question_1.html';


    })
    if($('#welcome_screen').length > 0){
        $('#welcome_screen').fadeIn();   
        $('#welcome_screen').fullpage({
            slidesNavigation: true,
            loopHorizontal: false
        });
    }
    if($('#splash_screen').length > 0){
        $('#splash_screen').fadeIn().fadeOut(1500);
    }
});

// function show_hide_nav_buttons(){
//     if (step < max_step){
//         $('.nav-right').removeClass('inactive');
//     }else{
//         $('.nav-right').addClass('inactive');
//     }

//     if (step > 1){
//         $('.nav-left').removeClass('inactive');
//     }else{
//         $('.nav-left').addClass('inactive');
//     }
// }

