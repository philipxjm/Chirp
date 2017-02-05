app = new Vue({
	el: '#app',
	data: {
		bannerOpen: false,
		topic: '',
		vis: ''
	},

	created: function() {
		console.log('chirp viewer initialized');
	},

	methods: {
		toggleBanner: function() {
			this.bannerOpen = !this.bannerOpen;
		},
		topic_keyup: function(ev) {

		}
	}
});
