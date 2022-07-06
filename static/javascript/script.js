// shows and hide the elements
let hide = document.querySelectorAll('.hide')
let btn = document.getElementById('hide-btn');

btn.addEventListener('click', function clickIt(){

    for (let i = 0; i < hide.length; i++) {
        if (hide[i].style.display==="none")
        {
            hide[i].style.display="block";
        }
        else{
            hide[i].style.display="none"
        }
        
        
    }
    
})
