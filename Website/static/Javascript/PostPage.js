var post = document.getElementById("post");

var req = new XMLHttpRequest();
req.open("POST", "/api/GetPostData");
req.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
req.onreadystatechange = function(){
    if(req.readyState!=4){
        $(document).ready(function(){
            $("#loading").show();
        });
    }else{
        $(document).ready(function(){
            $("#loading").hide();
    });
}
}
req.onload = function(){
    var response = JSON.parse(req.responseText); 
    if (response.Status == 1){
        RenderPost(response);
    }else if(response.Status == 2){
        post.insertAdjacentHTML('beforeend', response.Msg)
    }else{
        post.insertAdjacentHTML('beforeend', response.Msg)
    }
};
var Id = new URL(location.href).searchParams.get('p');
payload = JSON.stringify({
    "PublicID" : Id
});
req.send(payload);

function RenderPost(data){
var title = document.getElementById("title");
var content = document.getElementById("content");
var type = document.getElementById("type");
var postedat = document.getElementById("postedat");
var user = document.getElementById("user");
var link = document.getElementById("userlink");

title.innerText = data.Title;
content.innerText = data.Content;
type.innerText = data.Type;
postedat.innerText = data.PostedAt;
user.innerText = data.User;
link.setAttribute("href", ("/Profile?u=" + data.User));
}


