$('#likes').click(function () {
    var cat_id;

    cat_id = $(this).attr('data-catid');

    $.get('/rango/like_category/', {category_id:cat_id}, function (data) {
        $('#likes_count').html(data+' People liked this category.');
        $('#likes').hide();
        $('#dislikes').show();
    })


});