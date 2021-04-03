document.addEventListener('DOMContentLoaded', () => {


    anime({
        targets: '.center',
        // translateY: [50, 0],
        easing: 'easeOutExpo',
        duration: 3000,
        delay: 500,
        opacity: [0, 1],
    })

    anime({
		targets: '.testimonial-text',
		scale: [0, 1],
		easing: 'easeInOutQuart',
		duration: 1000,
		delay : 500,
		opacity: [0 , .6]
	})


})