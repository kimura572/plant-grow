var img_src = new Array('../static/image/hutuu.Gif','../static/image/genki.Gif','../static/image/dame.Gif',);
var i = Number(0);
// localStorage.clear(); 
let data = localStorage.getItem('key');
if (data) {
  var i = Number(data);
} else {
  var i = 0;
}
function changeImage(vars) { 
  const img = document.getElementById("orange");
  if (Number(vars)<0) {
    vars = Number(vars)*10
  }
  i+=Number(vars)
  if (i >= 1) {
    num = 1;
  } else if (i >= 0) {
    num = 0;
  } else {
  num = 2;
  }
  img.src = img_src[num];
  localStorage.setItem('key', i);
  document.getElementById('edit_area').innerHTML = '元気度：'+String(i);
};

function myFunc(vars) {
  alert(vars);
  location.reload();
}