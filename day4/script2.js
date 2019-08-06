let x1 = 3;
let x2 = 18;
let x3 = 6;
let t;

t=x1;
x1=x2;
x2=t;

t=x2;
x2=x3;
x3=t;

console.log("x1=" + x1);
console.log("x2=" + x2);
console.log("x3=" + x3);