//f(x) is a function that takes a single parameter and returns the
//result of the parameter being multiplied by 3 then adding by 7
function f(x)
{
    return 3 * x + 7;
}

//Display the result of calling function f() with argument 2
console.log(f(2));
console.log(f(12));
console.log(f(7));

function k(r)
{
    return 2 * Math.PI * r;
}

console.log("\n");
console.log(k(1));
console.log(k(1.5));
function l(a,b,c)
{
    var d = b**2 - 4 * a * c;
    if(d >= 0)
    {
        var srd = Math.sqrt(d);
        return (-1 * b + srd)/(2*a);
    }
    else
    {
        return NaN;
    }
}

console.log(1(1,4,4));
console.log(1(1,0,-1));