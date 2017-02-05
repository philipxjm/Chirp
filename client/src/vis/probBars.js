(function (name, definition) {
	/*global define module*/
	if (typeof define == 'function') define(definition);
	else if (typeof module != 'undefined') module.exports = definition;
	else this[name] = definition;
}('probBars', { // replace this!
	init: function(el) {
		el.innerHTML = '<iframe src="js/vis/bars.html" height="100%" width="100%"></iframe>'
	}
}));
