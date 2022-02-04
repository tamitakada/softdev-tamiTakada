// Team Cappuccino :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd1
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


function fact(n) {
	if (n <= 1) return 1;
	return fact(n - 1) * n;
}

function fib(n) {
	if (n <= 1) return n;
	return fib(n - 1) + fib(n - 2);
}
