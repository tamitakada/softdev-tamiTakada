var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var mode = "rect";

var toggleMode = function(e) {
  if (mode === "rect") mode = "circ";
  else mode = "rect";
}

var drawRect = function(e) {
  var mouseX = e.clientX;
  var mouseY = e.clientY;
  // console.log(`${mouseX}, ${mouseY}`);
  ctx.beginPath();
  ctx.rect(mouseX, mouseY, 100, 100);
  ctx.fillStyle = "blue";
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.fill();
}

var drawCircle = function(e) {
  var mouseX = e.clientX;
  var mouseY = e.clientY;
  // console.log(`${mouseX}, ${mouseY}`);
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, 50, 0, 2* Math.PI);
  ctx.fillStyle = "yellow";
  ctx.strokeStyle = "black";
  ctx.stroke();
  ctx.fill();
}

var draw = (e) => {
  if (mode === "rect") drawRect(e);
  else drawCircle(e);
}

var wipeCanvas = () => {

}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
