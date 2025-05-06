/*!
=========================================================
* LeadMark Landing page
=========================================================

* Copyright: 2019 DevCRUD (https://devcrud.com)
* Licensed: (https://devcrud.com/licenses)
* Coded by www.devcrud.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
});

// protfolio filters
$(window).on("load", function() {
    var t = $(".portfolio-container");
    t.isotope({
        filter: ".new",
        animationOptions: {
            duration: 750,
            easing: "linear",
            queue: !1
        }
    }), $(".filters a").click(function() {
        $(".filters .active").removeClass("active"), $(this).addClass("active");
        var i = $(this).attr("data-filter");
        return t.isotope({
            filter: i,
            animationOptions: {
                duration: 750,
                easing: "linear",
                queue: !1
            }
        }), !1
    })
})

$(document).ready(function() {
    // Other existing code...

    // Check for form submission status from the Django context
    const formSubmissionStatus = document.getElementById('form-submission-status').innerText;

    if (formSubmissionStatus === "success") {
        alert("Your message has been sent successfully!");
    } else if (formSubmissionStatus === "error") {
        alert("There was an error sending your message. Please correct the form.");
    }
});


const audioPlayers = document.querySelectorAll('.audio-player');

// Loop through all audio players and add event listener to each
audioPlayers.forEach(player => {
    player.addEventListener('play', function() {
        // Pause all other players when one starts playing
        audioPlayers.forEach(otherPlayer => {
            if (otherPlayer !== player) {
                otherPlayer.pause();
            }
        });
    });
});

// $(document).ready(function() {
//     // Set carousel interval (5000ms = 5 seconds)
//     $('#carouselExampleIndicators').carousel({
//         interval: 2000
//     });
    
//     // Optional: Pause carousel on hover
//     $('#carouselExampleIndicators').hover(
//         function() {
//             $(this).carousel('pause');
//         },
//         function() {
//             $(this).carousel('cycle');
//         }
//     );
// });

// $(document).ready(function() {
//     // For Bootstrap 4 (most likely used in Leadmark)
//     $('#carouselExampleIndicators').carousel({
//         interval: 3000  // Set your desired interval in milliseconds (3000 = 3 seconds)
//     });
    
//     // If using Bootstrap 5
//     /*
//     const myCarousel = document.querySelector('#carouselExampleIndicators');
//     const carousel = new bootstrap.Carousel(myCarousel, {
//         interval: 3000  // Set your desired interval in milliseconds
//     });
//     */
// });



