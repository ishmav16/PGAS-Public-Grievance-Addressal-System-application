function delineate()
{
var lat = 13.511499;
    var lon = 80.014366;
 var latlng = new google.maps.LatLng(lat, lon);
            var geocoder = geocoder = new google.maps.Geocoder();
            geocoder.geocode({ 'latLng': latlng }, function (results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    if (results[0]) {
                     //  alert("Location: " + results[0].formatted_address);
                     var result=results[0].formatted_address;
                     document.write('sunil');
                    }
                }
            });

}