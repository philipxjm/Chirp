(function (name, definition) {
	/*global define module*/
	if (typeof define == 'function') define(definition);
	else if (typeof module != 'undefined') module.exports = definition;
	else this[name] = definition;
}('states', { // replace this!
	init: function(el, req_name, req_mood) {
		//var req_name = 'clinton';
		//inserting css
		var css_src = [
			'.background {fill: none; pointer-events: all;}',
			'#states {fill: #aaa;}',
			'#states .active {fill: orange;}',
			'#state-borders {fill: none;stroke: #fff;stroke-width: 1.5px;stroke-linejoin: round;stroke-linecap: round;pointer-events: none;}'
		]
		var css = document.createElement('style');
		css.innerHTML = css_src.join('\n');
		el.appendChild(css);

		//var request_url = 'data/' + req_name;
		
		var request_url;
		request_url = 'http://13.82.219.142:8080/analyzed-tweets/' + req_name;
		console.log('loading ' + request_url);
		var width = 960,
			height = 500,
			centered;

		var projection = d3.geo.albersUsa()
			.scale(1070)
			.translate([width / 2, height / 2]);

		var path = d3.geo.path()
			.projection(projection);

		var svg = d3.select(el).append("svg")
		 svg.attr("viewBox", "0 0 " + width + " " + height)
			.attr('width', '100vw')
			.attr('height', '100vh');

		svg.append("rect")
			.attr("class", "background")
			.attr("width", width)
			.attr("height", height)
			.on("click", clicked);

		var g = svg.append("g");

		 // request multiple requests
		queue()
			.defer(d3.json, 'data/us.json')
			.defer(d3.json, 'data/statedict.json')
			.defer(d3.json, request_url)
			.await(function(error, us, dict, tweets)
				{
					console.log(error);
					if (error) throw error;

						console.log(tweets);

					statesdict = dict;
					var stateslist = [];
					Object.keys(dict).map(k => {
						stateslist.push(statesdict[k]);
					});

					console.log(stateslist);

					window.tweets = tweets;

					// map
					states_tweets = {};

					tweets = tweets.filter(t => (t['state'] !== undefined && (stateslist.indexOf(t['state']) != -1)));

					tweets.map(function(tweet) {
						// add in an array for a state if it doesn't exist
						if (!(tweet['state'] in states_tweets)) {
							states_tweets[tweet['state']] = {
								positive: 0,
								negative: 0,
								neutral: 0,
								total: 0,
								twitIDs: [],
							};
						}

						// because fuck your api anyways
						var key_translate = {
							'pos': 'positive',
							'neg': 'negative',
							'neutral': 'neutral'
						};
						// add in an array
						states_tweets[tweet['state']][ key_translate[tweet['label']] ] += 1;
						states_tweets[tweet['state']][ 'total' ] += 1;
						states_tweets[tweet['state']][ 'twitIDs' ].push(tweet.twitID);
						// identity
						return tweet;
					});

					var color_scales = {
						positive: d3.scale.linear()
							.domain([0, d3.max(Object.keys(states_tweets), k => states_tweets[k]['positive'])])
							.range([0,1]),
						negative: d3.scale.linear()
							.domain([0, d3.max(Object.keys(states_tweets), k => states_tweets[k]['negative'])])
							.range([0,1]),
						neutral: d3.scale.linear()
							.domain([0, d3.max(Object.keys(states_tweets), k => states_tweets[k]['neutral'])])
							.range([0,1]),
						total: d3.scale.linear()
							.domain([0, d3.max(Object.keys(states_tweets), k => states_tweets[k]['total'])])
							.range([0,1]),
					}

					var color_interpolator = d3.interpolateRgb('#2b2b2b', '#ffa500');

					var color_gen = function(val) {
						//return (statesdict[val.id] === undefined) ? 'red' : '#2b2b2b';
						var mood = states_tweets[statesdict[val.id]];
						mood = (mood === undefined) ? 0 : mood[req_mood];
						console.log(statesdict[val.id] + ":" + color_scales[req_mood](mood));
						return color_interpolator(color_scales[req_mood](mood));
					}

					console.log(color_scales);
					window.states_tweets = states_tweets;

					g.append("g")
						.attr("id", "states")
					.selectAll("path")
					.data(topojson.feature(us, us.objects.states).features)
					.enter().append("path")
					.attr("d", path)
					.on("click", clicked)
					.attr('text', (d) => d.id)
					.attr('fill', color_gen);

					

					g.append("path")
						.datum(topojson.mesh(us, us.objects.states, function(a, b)
							{
								return a !== b;
							}))
								.attr("id", "state-borders")
					.attr("d", path)
				});

		function clicked(d)
		{
			console.log('clicked ' + statesdict[d.id]);
			var x, y, k;


			if (d && centered !== d)
				{
					var centroid = path.centroid(d);
					x = centroid[0];
					y = centroid[1];
					k = 4;
					centered = d;
				}
			else
				{
					x = width / 2;
					y = height / 2;
					k = 1;
					centered = null;
				}

			var panel = document.getElementById('panel');
				
			if (k == 1) {
				panel.classList.remove('active');
			} else {
				panel.classList.add('active');
			}
			panel.innerHTML = '<iframe id="barsembed" src="js/vis/bars.html" width="450" height="350" border=0 frameborder=0></iframe>';
			if (statesdict[d.id] in states_tweets) {
				states_tweets[statesdict[d.id]].twitIDs.map(function(tweet) {
					console.log(tweet);
					panel.innerHTML += '<iframe border=0 frameborder=0 height=250 width=450 src="https://twitframe.com/show?url=https%3A%2F%2Ftwitter.com%2Fjack%2Fstatus%2F' + tweet + '"></iframe>\n';
				});
			} else {
				panel.classList.remove('active');
			}

			g.selectAll("path")
				.classed("active", centered && function(d)
					{
						return d === centered;
					});

			g.transition()
				.duration(750)
				.attr("transform", "translate(" + width / 2 + "," + height / 2 +
					")scale(" + k + ")translate(" + -x + "," + -y + ")")
						.style("stroke-width", 1.5 / k + "px");
		}
	}
}));
