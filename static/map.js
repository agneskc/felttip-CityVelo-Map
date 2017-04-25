var map = L.map('map').setView([40.7306,-73.9352], 12);

var mapTiles = L.tileLayer('https://a.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {	
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
	minZoom: 12,
	id: 'mapbox.run-bike-hike',
	accessToken: 'pk.eyJ1IjoiYWduZXMiLCJhIjoiaTVSSlpvNCJ9.dLN9PeQnt4OjQFapBv6dzQ'
});

L.control.locate(
	{ follow:true },
	{onLocationOutsideMapBounds:  function(context) { // called when outside map boundaries 
		alert("Citi Bike is not available outside of New York City.");
    },}
).addTo(map);

mapTiles.addTo(map);