// Team Cappuccino :: Daniel Sooknanan, Tami Takada 
// SoftDev pd1
// K31 -- canvas based JS animation
// 2022-02-15t



// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON

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


dotButton.addEventListener( "click", function() {
  drawDot();
});
stopButton.addEventListener( "click",  stopIt );

