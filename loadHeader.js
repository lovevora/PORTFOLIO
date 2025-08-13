// Load the header from header.html into the #header div
fetch("header.html")
  .then(response => response.text())
  .then(data => {
    document.getElementById("header").innerHTML = data;
  })
  .catch(err => console.error("Header failed to load:", err));
