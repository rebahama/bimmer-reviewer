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








