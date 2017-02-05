app = new Vue({
	el: '#app',
	data: {
		bannerOpen: false,
		topic: 'trump',
		vis: 'states',
		mood: 'total',
		allMoods: ['total', 'positive', 'neutral', 'negative'],
		moduleIndex: ['states', 'probBars'],
		loadedModuleIndex: []
	},

	created: function() {
		this.loadModule(this.vis)
		console.log('chirp viewer initialized');
	},

	methods: {
		loadModule: function(module_name) {
			if (this.loadedModuleIndex.indexOf(module_name) != -1) return;
			fetch('js/vis/' + module_name + '.js')
				.then(resp => resp.text())
				.then(resp => {
					var el = document.createElement('script');
					el.innerHTML = resp;
					document.body.append(el);
					this.loadedModuleIndex.push(module_name);

					setTimeout(_ => this.callModule(module_name), 50);
				}).catch(_ => console.log('failed to load module'));
		},
		callModule: function(module_name) {
			if (this.loadedModuleIndex.indexOf(module_name) == -1) {
				this.loadModule(module_name);
				return;
			}
			document.getElementById('map').innerHTML = '';
			try {
				window[module_name].init(document.getElementById('map'), this.topic, this.mood);
			} catch (e) {
				console.log(e);
			}
		},
		toggleBanner: function() {
			this.bannerOpen = !this.bannerOpen;
		},
		topic_enter: function(ev) {
			this.callModule(this.vis);
		},
		change_vis: function() {
			console.log('changed vis: ' + this.vis);
			this.callModule(this.vis);
		},
		change_mood: function() {
			this.callModule(this.vis);
		}
	}
});
