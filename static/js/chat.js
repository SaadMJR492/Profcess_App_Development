const text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
    '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
    '{message}' +
    '</div>';

let userState = ''


function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}

function send(sender, receiver, message) {
    $.post('/api/messages', '{"sender": "' + sender + '", "receiver": "' + receiver + '","message": "' + message + '" }', function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message);
        $('#board').append(box);
        scrolltoend();
    })
}

function receive() {
    $.get('/api/messages/' + sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0) {
            for (var i = 0; i < data.length; i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                $('#board').append(box);

                scrolltoend();
            }
        }
    })
}

function getUsers(senderId, callback) {
    return $.get('/api/users', function (data) {
        if (userState !== JSON.stringify(data)) {
            userState = JSON.stringify(data);
            const doc = data.reduce((res, user) => {
                if (user.id === senderId) {
                    return res
                } else {
                    return [userDiv(senderId, user.id, user.username, user.online), ...res]
                }
            }, [])
            callback(doc)
        }
    })
}

/*EMOJI*/

$(document).on("click","#emoji-picker",function(e){
    e.stopPropagation();
     $('.intercom-composer-emoji-popover').toggleClass("active");
 });

 $(document).click(function (e) {
     if ($(e.target).attr('class') != '.intercom-composer-emoji-popover' && $(e.target).parents(".intercom-composer-emoji-popover").length == 0) {
         $(".intercom-composer-emoji-popover").removeClass("active");
     }
 });

 $(document).on("click",".intercom-emoji-picker-emoji",function(e){
     $(".emoji-test").append($(this).html());
     $('#id_message').val($('#id_message').val() + $(this).html());
 });

 $(document).on('input','.intercom-composer-popover-input', function() {
     var query = this.value;
     if(query != ""){
       $(".intercom-emoji-picker-emoji:not([title*='"+query+"'])").hide();
     }
     else{
       $(".intercom-emoji-picker-emoji").show();
     }
 });
