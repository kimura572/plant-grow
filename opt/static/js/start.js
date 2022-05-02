var img_src = new Array('../static/image/1.jpeg','../static/image/2.jpeg','../static/image/3.gif',);
var i = 0;


function changeImage() { 
  const img = document.getElementById("orange"); 
  if (i == 2) {
    i = 0;
  } else {
    i ++;
  }
  img.src = img_src[i];
};