/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO"); // Prints string in the dev console upon loading page

// These variables can both be accessed from the console
// When you enter the var names in the console, it prints out the assigned values
var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

var fact = function(n) {
        if (n <= 1) return 1;
        return fact(n - 1) * n;
}

var fib = function(n) {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
}

var gcd_helper = function(low, high) {
    result = 0;
    for (let i = 0; i <= low; i++) {
        if (low % i == 0 && high % i == 0) {
            result = i;
        }
    }
    return result;
}

var gcd = function(a, b) {
    if (a == 0 || b == 0) {
        return 0;
    }
    else if (a == b) {
        return a;
    }
    else if (a < b) {
        return gcd_helper(a, b);
    }
    else {
        return gcd_helper(b, a);
    }
}
