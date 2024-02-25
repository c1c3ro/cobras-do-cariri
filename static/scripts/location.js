function get_location() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, geoError);
        return true;
    } else {
        alert("Não foi possível obter a localização. O seu navegador não tem suporte à geolocalização.");
        return false;
    }
}

function showPosition(position) {
    $('#lat').val(position.coords.latitude);
    $('#lon').val(position.coords.longitude);
}

function geoError() {
    $('#gps').prop("checked", false);
    $('.coordenadas').removeClass('d-flex')
    $('.coordenadas').addClass('d-none')
    alert("Não foi possível obter a localização. O seu navegador não tem suporte à geolocalização.")
}