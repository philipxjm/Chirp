(function (name, definition) {
	/*global define module*/
	if (typeof define == 'function') define(definition);
	else if (typeof module != 'undefined') module.exports = definition;
	else this[name] = definition;
}('baz', {
	name: 'baz'
}));
