let map;
let hoveredState = null;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 37.0902, lng: -95.7129 }, // Center on the United States
        zoom: 4.8, // Adjust the zoom level as per your preference
        draggable: false, // Disable map dragging
        scrollwheel: false, // Disable zooming via scrollwheel
        disableDoubleClickZoom: true, // Disable zooming via double-click
        keyboardShortcuts: false, // Disable keyboard shortcuts
        styles: [
          {
            featureType: "administrative",
            elementType: "geometry.stroke",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "administrative.country",
            elementType: "geometry.stroke",
            stylers: [
              { visibility: "on" },
              { color: "#000000" }, // Black outline color
            ],
          },
          {
            featureType: "administrative.land_parcel",
            elementType: "geometry.stroke",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "administrative.locality",
            elementType: "labels.text.fill",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "administrative.neighborhood",
            elementType: "labels.text.fill",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "administrative.province",
            elementType: "geometry.stroke",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "landscape",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "poi",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "road",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "transit",
            stylers: [
              { visibility: "off" },
            ],
          },
          {
            featureType: "water",
            elementType: "labels.text.fill",
            stylers: [
              { visibility: "off" },
            ],
          },
        ],
      });

  map.data.addListener('mouseover', function(event) {
    // Retrieve the hovered state feature
    const stateName = event.feature.getProperty('NAME');
  
    // Only highlight if the hovered state is different from the currently hovered state
    if (stateName !== hoveredState) {
      // Remove the highlight from the previously hovered state (if any)
      if (hoveredState) {
        map.data.overrideStyle(hoveredState, {
          strokeWeight: 1, // Reset the stroke weight
          strokeColor: '#000000', // Reset the stroke color
        });
      }
  
      // Highlight the hovered state
      map.data.overrideStyle(event.feature, {
        strokeWeight: 2, // Increase the stroke weight to highlight
        strokeColor: '#ff0000', // Red stroke color for highlighting
      });
  
      // Update the currently hovered state
      hoveredState = event.feature;
    }
  });

  map.data.addListener('mouseout', function(event) {
    // Only remove the highlight if the state is the currently hovered state
    if (event.feature === hoveredState) {
      // Remove the highlight from the previously hovered state
      map.data.overrideStyle(hoveredState, {
        strokeWeight: 1, // Reset the stroke weight
        strokeColor: '#000000', // Reset the stroke color
      });
  
      // Reset the currently hovered state
      hoveredState = null;
    }
  });
  
  // Load the GeoJSON data for the United States
  map.data.loadGeoJson('https://storage.googleapis.com/mapsdevsite/json/states.js');
}

initMap();
