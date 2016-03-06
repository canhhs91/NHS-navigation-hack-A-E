$(document).ready(function(){
    $('#questions').fadeIn();
    $('.tinderslide').jTinder(
    {
        onDislike: function (item) {
            is_finish('dislike');
        },
        onLike: function (item) {
            is_finish('like');
        },
        animationRevertSpeed: 200,
        animationSpeed: 400,
        threshold: 1,
        likeSelector: '.like',
        dislikeSelector: '.dislike'
    });
    $('.actions .like, .actions .dislike').click(function(e){
        e.preventDefault();
        $(".tinderslide").jTinder($(this).attr('class'));
    });
});

function is_finish(option){
    question_id = $('#data').data('question-id');
    if (option == 'like'){
        answer = 'yes';
    }else{
        answer = 'no';
    }
    $.cookie('nhs_question_'+question_id, answer);

    if (option == 'like'){
        next_question_id = $('#data').data('next-if-yes');
    }else{
        next_question_id = $('#data').data('next-if-no');
    }
    
    data = {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()};
    $.each($.cookie(), function (key, val) {
        if (key.indexOf('nhs_question_') == 0) {
            data[key] = val;
        }
    });

    if(parseInt(next_question_id) == -1){
        $.ajax({
            'url': '/submitanswer', 
            'type': 'POST', 
            'data': data, 
            
        }).done(function(){
            location.href = '/healthpass';
        })
        return;
    }
    location.href = '/question_'+next_question_id+'.html';
}