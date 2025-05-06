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
    const formSubmissionStatus = document.getElementById('form-submission-status').innerText;

    if (formSubmissionStatus === "success") {
        alert("Your message has been sent successfully!");
    } else if (formSubmissionStatus === "error") {
        alert("There was an error sending your message. Please correct the form.");
    }
});


const audioPlayers = document.querySelectorAll('.audio-player');


audioPlayers.forEach(player => {
    player.addEventListener('play', function() {

        audioPlayers.forEach(otherPlayer => {
            if (otherPlayer !== player) {
                otherPlayer.pause();
            }
        });
    });
});

