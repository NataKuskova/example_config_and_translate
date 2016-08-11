$(document).ready(function() {
/*
    $('.css-label').click(function(){
        id = $(this).attr("for");
        price=$('#price').text();
        link=$('#link_cart').text();
        q50=$('#q50').val();
        q100=$('#q100').val();
        if(id=='q50')
        {
            $('#price').text(q50);
            $('.add_to_cart_btn').attr('href', link+'add_to_cart/50/');
        }
        else if(id=='q100')
        {
            $('#price').text(q100);
            $('.add_to_cart_btn').attr('href', link+'add_to_cart/100/');
        }
    });

    if($("#q50").is(":checked"))
    {
        $('#price').text($('#q50').val());
        $('.add_to_cart_btn').attr('href', $('#link_cart').text()+'add_to_cart/50/');
    }
    else if($("#q100").is(":checked"))
    {
        $('#price').text($('#q100').val());
        $('.add_to_cart_btn').attr('href', $('#link_cart').text()+'add_to_cart/100/');
    }
*/
    $('.popup .close_window, .overlay').click(function (){
        $('.popup, .overlay').css({'opacity': 0, 'visibility': 'hidden'});
    });

    $('.add_to_cart_btn.enabled').click(function(e){
        e.preventDefault();
        $('.popup, .overlay').css({'opacity': 1, 'visibility': 'visible'});

        url=$('.add_to_cart_btn.enabled').attr('href');
        $.ajax({
            url: url,
            type: "GET",
            dataType:"json",
            success: function(data) {
                $('#number').html(data.count);
            }
        });
    });
});