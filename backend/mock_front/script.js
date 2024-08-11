/* eslint-disable no-undef */
/**
 * Simple map
 */

var map = L.map('map',{crs: L.CRS.Simple});

var bounds = [[0,0],[1000,1000]]

var image = L.imageOverlay('http://127.0.0.1:5000',bounds).addTo(map);

map.fitBounds(bounds);

/*
L.tileLayer('file:///E:/Temp/SPARC/test/{z}/{x}/{y}.png', {
    maxZoom: 9,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
*/