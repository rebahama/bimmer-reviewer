//For the html called home.html
// scroll back to top when clicked on this button

let scrollBtn = document.getElementById('scroll-btn');
if (scrollBtn){
    scrollBtn.addEventListener('click', topClick);
}

function topClick(){
  "use strict";
    scrollBtn.style.backgroundColor="red";
    document.body.scrollTop=0;
    document.documentElement.scrollTop = 0;
}

