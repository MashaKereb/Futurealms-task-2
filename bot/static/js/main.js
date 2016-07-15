var dialog_id = 0;

function addMessage(message, author) {
    $("#message_box").prepend("<li>" + author + " : " + message + "</li>");
}

$("#send_but").click(function () {
    var message = $("#message").val();

    if(message){
        addMessage(message, "User");
        $.ajax({
            type:"GET",
            url: "answer/",
            data: { 
                "message": message,
                "dialog_id": dialog_id
            }
        }).done(function(data) {
            dialog_id = data.id;
            addMessage(data.message, "Bot");
        });
        $("#message").val("");
    }
});
