//For the html called home.html
// scroll back to top when clicked on this button

let scrollBtn = document.getElementById('scroll-btn');
if (scrollBtn){
    scrollBtn.addEventListener('click', topClick);
}

function topClick(){
    scrollBtn.style.backgroundColor="red";
    document.body.scrollTop=0;
    document.documentElement.scrollTop = 0;
}


function scrollIt(){
for (let i = 0; i < reveal.length; i++) {
  if (reveal[i].style.display==="none")
     reveal[i].style.display="block";
  else
  reveal[i].style.display="none";
}
}

