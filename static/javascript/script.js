// Load this script after the html tag have been loaded
window.onload = function(){
// shows and hide the comments in the detail review page
let btn = document.getElementById('hide-btn');
if(btn){
btn.addEventListener('click', clickIt)
}
function clickIt(){
    let hide = document.querySelectorAll('.hide');
    for (let i = 0; i < hide.length; i++) {
        if (hide[i].style.display==="none")
        {
            hide[i].style.display="block";
        }
        else{
            hide[i].style.display="none"
        }   
    }
}
// scroll back to top when clicked on this button
let scrollBtn = document.getElementById('scroll-btn')
if (scrollBtn){
    scrollBtn.addEventListener('click', topClick)
}

function topClick(){
    scrollBtn.style.backgroundColor="red"
    document.body.scrollTop=0;
    document.documentElement.scrollTop = 0;
}

let categoryBtn=document.getElementById('scroll-btn-category')
if(categoryBtn){
    categoryBtn.addEventListener('click', topClickCategory)
}

function topClickCategory(){
    categoryBtn.style.backgroundColor="red"
    document.body.scrollTop=0;
    document.documentElement.scrollTop = 0;
}

//Change colour of cards when clicked
let reveal=document.querySelectorAll('.swipe-up')
if(reveal){
    window.addEventListener('click', scrollIt)
}

function scrollIt(){
for (let i = 0; i < reveal.length; i++) {
  if (reveal[i].style.backgroundColor==="white")
     reveal[i].style.backgroundColor="blue"
  else
  reveal[i].style.backgroundColor="white"
}
}


}















