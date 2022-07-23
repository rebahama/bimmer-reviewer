// For category page
window.onload = function(){
let categoryBtn=document.getElementById('scroll-btn-category');
if(categoryBtn){
    categoryBtn.addEventListener('click', topClickCategory);
}

function topClickCategory(){
    categoryBtn.style.backgroundColor="red"
    document.body.scrollTop=0;
    document.documentElement.scrollTop = 0;
}
}