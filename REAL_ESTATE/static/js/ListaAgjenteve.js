
document.addEventListener('DOMContentLoaded', () => {

	//animacion per teksti 'Lista e agjenteve'
    anime({
		targets: '.container .listimi .fs-2',
		translateY: [-40, 0],
		easing: 'easeOutExpo',
		duration: 1500,
		delay: 1000,
		opacity: [0, 1],
	})


		//animacion per hr
    anime({
		targets: '.container .listimi  hr',
		scale: [0, 1],
		easing: 'easeInOutQuart',
		duration: 1500,
		delay: 1000,
		opacity: [0 , .5]

	})


		//animacion per teksti paragraph
	anime({
		targets: '.container .listimi .fs-6',
		translateY: [50, 0],
		easing: 'easeOutExpo',
		duration: 1500,
		delay: 1000,
		opacity: [0, 1],
	})

})




