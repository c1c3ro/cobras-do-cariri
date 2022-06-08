
document.querySelector("#searchBar").addEventListener("keyup", function(event) {
  if (event.key !== "Enter") return;
    console.log("vc apertou enter")
    document.querySelector("#searchBtn").click();
    event.preventDefault();
});

function getInputValue(){
    console.log("entrei na função?")
    var inputVal = document.getElementById("searchBar").value
    inputVal = inputVal.toLowerCase()
    inputVal = inputVal.replace(/\s/g, '%20')
    var url = "/cobras/"
    hostName = window.location.host
    url = "http://".concat(hostName, url, inputVal)
    window.location.href = url
}