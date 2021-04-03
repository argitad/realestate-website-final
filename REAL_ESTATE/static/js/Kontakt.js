document.addEventListener('DOMContentLoaded', () => {

	//animacion per tekstin 'Contact Us'
    anime({
		targets: '.horizontal_line .fs-2', //emri i klases tek html
		translateY: [-40, 0], //animon txt nga siper posht
		easing: 'easeOutExpo',  //ben me smooth tekstin kur leviz
		duration: 1500,      //kohzgjatje e animimi
		delay: 1000,        //ben animimin pas 1 sekondash
		opacity: [0, 1],  //ben opacityne  e txt nga 0 ne 1
	})


		//animacion per hr
    anime({
		targets: '.horizontal_line  hr',
		scale: [0, 1],
		easing: 'easeInOutQuart',
		duration: 1500,
		delay : 1000,
		opacity: [0 , .5]
	})


		//animacion per teksti paragraph
	anime({
		targets: '.horizontal_line .fs-6',
		translateY: [50, 0],
		easing: 'easeOutExpo',
		duration: 1500,
		delay: 1000,
		opacity: [0, 1],
	})
})