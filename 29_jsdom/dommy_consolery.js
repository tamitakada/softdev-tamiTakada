// Lucas Tom-Wong, Tami Takada 
// SoftDev pd1
// K29 -- DOMfoolery++
// 2022-02-09
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO"); // Prints string in the dev console upon loading page

// These variables can both be accessed from the console
// When you enter the var names in the console, it prints out the assigned values
let i = "hello";
let j = 20;


//assign an anonymous fxn to a var
let f = function(x) {
  let j=30;
  return j+x;
};

//instantiate an object
let o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


let addItem = function(text) {
  let list = document.getElementById("thelist");
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


let removeItem = function(n) {
  let listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


let red = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


let stripe = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

let fact = function(n) {
        if (n <= 1) return 1;
        return fact(n - 1) * n;
}

let fib = function(n) {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
}

let gcd_helper = function(low, high) {
    result = 0;
    for (let i = 0; i <= low; i++) {
        if (low % i == 0 && high % i == 0) {
            result = i;
        }
    }
    return result;
}

let gcd = function(a, b) {
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

document.getElementById('fib').addEventListener('click', function() {
	let num = Math.floor(Math.random() * 31);
	let result = fib(num);
	document.getElementById('result').innerHTML = 'Fib of ' + num + ' is ' + result;
});
document.getElementById('fac').addEventListener('click', function() {
	let num = Math.floor(Math.random() * 21);
	let result = fact(num);
	document.getElementById('result').innerHTML = 'Fact of ' + num + ' is ' + result;
});
document.getElementById('gcd').addEventListener('click', function() {
	let num_0 = Math.floor(Math.random() * 101);
	let num_1 = Math.floor(Math.random() * 101);
	let result = gcd(num_0, num_1);
	document.getElementById('result').innerHTML = 'GCD of ' + num_0 + ' and ' + num_1 + ' is ' + result;
});
