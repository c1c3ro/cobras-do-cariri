function getInputValue(){
    var inputVal = document.getElementById("searchBar").value
    inputVal = inputVal.toLowerCase().replace('cobra', '').replace('serpente', '')
    inputVal = inputVal.replace(/\s/g, '%20')
    var url = "/cobras/"
    hostName = window.location.host
    url = "http://".concat(hostName, url, inputVal)
    window.location.href = url
}