// Liesel Wong, Tami Takada
// SoftDev pd1
// K32 -- More Moving Parts
// 2022-02-17

//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON
var saverButton = document.getElementById("buttonSaver");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d"); // YOUR CODE HERE

//set fill color to team color
ctx.fillStyle = "#ff335c"; // YOUR CODE HERE

var requestID = 0;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...");
  ctx.clearRect(0, 0, c.width, c.height);
};


var radius = 0;
var growing = true;

//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...")
  
  clear();
  
  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0, 2* Math.PI);
  ctx.stroke();
  ctx.fill();
  
  if (radius >= (c.width/2)) growing = false;
  else if (radius <= 0) growing = true;
  
  if (growing) radius += 2;
  else radius -= 2;
  
  window.cancelAnimationFrame(requestID);
  requestID = window.requestAnimationFrame(drawDot);
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );

  window.cancelAnimationFrame(requestID);
};

var x; var y; var angle;

var f = () => {
  clear();
  
  var img = new Image(100, 200);
  img.src = 'logo_dvd.jpg';
    
  x += 2 * Math.cos(angle);
  y += 2 * Math.sin(angle);
    
  if (x >= (c.width - 100) || x <= 0) {
    angle = Math.PI - angle;
  }
    
  if (y >= (c.height - 50) || y <= 0) {
    angle = 2 * Math.PI - angle;
  }
  
  ctx.drawImage(img, x, y, 100, 50);
  
  window.cancelAnimationFrame(requestID);
  requestID = window.requestAnimationFrame(f);
};


dotButton.addEventListener( "click", drawDot);
stopButton.addEventListener( "click",  stopIt );
saverButton.addEventListener("click", function() {
    x = Math.floor(Math.random() * (c.width - 100));
    y = Math.floor(Math.random() * (c.height - 50));
    angle = Math.floor(Math.random() * (2 * Math.PI));
    f();
});
