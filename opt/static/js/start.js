var img_src = new Array('../static/image/hutuu.Gif','../static/image/genki.Gif','../static/image/dame.Gif',);
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