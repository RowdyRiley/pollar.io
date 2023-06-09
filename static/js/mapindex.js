let map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 37.0902, lng: -95.7129 }, // Center on the United States
    zoom: 4.8, // Adjust the zoom level as per your preference
    //disableDefaultUI: true, // Disable default map controls
    //gestureHandling: "none", // Disable map panning and zooming
    styles: [
      {
        featureType: "administrative",
        elementType: "geometry.stroke",
        stylers: [
          {
            visibility: "on",
          },
          {
            color: "#000000", // Black outline color
          },
        ],
      },
      {
        featureType: "administrative",
        elementType: "labels.text.fill",
        stylers: [
          {
            visibility: "on",
          },
        ],
      },
      {
        featureType: "administrative",
        elementType: "labels.text.stroke",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "administrative.country",
        elementType: "geometry.stroke",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "administrative.province",
        elementType: "geometry.stroke",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "administrative.locality",
        elementType: "labels.text.fill",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "administrative.neighborhood",
        elementType: "labels.text.fill",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "landscape",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "poi",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "road",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "transit",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
      {
        featureType: "water",
        elementType: "labels.text.fill",
        stylers: [
          {
            visibility: "off",
          },
        ],
      },
    ],
  });

  // Add event listener to detect when the user clicks on a state
  map.data.addListener('click', function(event) {
    // Retrieve the selected state feature
    const stateName = event.feature.getProperty('NAME');

    // Goes to the controller and sends it the stateName to insert into the database. 
    axios.post(get_state_url, {stateName: stateName}).then(function (response) {
      console.log('Selected state:', stateName);
      window.location = response.data.new_url;
      });
  });

  // Load the GeoJSON data for the United States
  map.data.loadGeoJson('https://storage.googleapis.com/mapsdevsite/json/states.js');
}

initMap();