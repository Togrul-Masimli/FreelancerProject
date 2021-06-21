/* For to go top of the page */

document.querySelector('.to-top').addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
});

/* For comment section */

$(document).ready(function() {
    $(".accordion").click(function() {
        const value = $(this).attr("data-filter")
        $(".comment").filter('.' + value).toggle(500);
    })
});

/* For profile page */

// $(document).ready(function() {
//     $(".profile-filter").click(function() {
//         const item = $(this).attr("data-filter")
//         $(".toggle").not('.' + item).hide(700);
//         $(".toggle").filter('.' + item).show(700);
//     })
// });

/* For comment button */

$('.fa-comment').click(function() {
    if ($(this).hasClass('comment-active') == true) {
        $(this).removeClass("comment-active");
    } else
        $(this).addClass("comment-active")
});

/* For like button */

$('.fa-heart').click(function() {
    if ($(this).hasClass('heart-active') == true) {
        $(this).removeClass("heart-active");
    } else
        $(this).addClass("heart-active")
});

/* For dropdown */

document.querySelector('.dropdown-container').addEventListener('click', () => {
    if (document.querySelector('.dropdown-container').nextElementSibling.style.opacity == "1") {
        document.querySelector('.dropdown-container').nextElementSibling.style.opacity = "0";
    } else {
        document.querySelector('.dropdown-container').nextElementSibling.style.opacity = "1";
    }
})

/* For post-dropdown */

// document.querySelector('.post-dropdown-container').addEventListener('click', () => {
//     if (document.querySelector('.post-dropdown-container').nextElementSibling.style.opacity == "1") {
//         document.querySelector('.post-dropdown-container').nextElementSibling.style.opacity = "0";
//     } else {
//         document.querySelector('.post-dropdown-container').nextElementSibling.style.opacity = "1";
//     }
// })


$(document).ready(function() {
    $(".post-dropdown-container").click(function() {
        const val = $(this).attr("data-filter1")
        $(".post-dropdown").filter('.' + val).toggleClass("random");
    })
});