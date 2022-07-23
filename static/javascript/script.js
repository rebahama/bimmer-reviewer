// Load this script after the html tag have been loaded

    // shows and hide the comments in the detail review page
     'use strict';
    let btn = document.getElementById('hide-btn');
    if(btn){
    btn.addEventListener('click', clickIt);
    }
    function clickIt(){
        let hide = document.querySelectorAll('.hide');
        for (let i = 0; i < hide.length; i++) {
            if (hide[i].style.display==="none")
            {
                hide[i].style.display="block";
            }
            else{
                hide[i].style.display="none";
            }   
        }
    }

// Initialize and add the map from google
function initMap() {
    // The location of Uluru
    const sthlm = { lat: 59.33258, lng: 18.0649 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: sthlm,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: sthlm,
      map: map,
    });
  }
