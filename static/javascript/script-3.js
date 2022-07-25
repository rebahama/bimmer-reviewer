// For category page
// scroll to the top of the page when clicked on the element.
window.onload = function(){
    "use strict";
 let categoryBtn=document.getElementById('scroll-btn-category');
 if(categoryBtn){
     categoryBtn.addEventListener('click', topClickCategory);
 }
 
 function topClickCategory(){
     categoryBtn.style.backgroundColor="red";
     document.body.scrollTop=0;
     document.documentElement.scrollTop = 0;
 }
 };