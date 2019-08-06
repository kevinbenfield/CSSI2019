console.log(1);
console.log(2);
console.log(3);
console.log(4);
console.log(5);
console.log(6);
console.log(7);
console.log(8);
console.log(9);
console.log(10);
// With one line
console.log('1\n2\n3\n4\n5\n6\n7\n8\n9\n10')

//Prompt
let result = prompt("Enter Your Name");
console.log("Hello, ", result);
let num = prompt("Enter a Number")
num = Number(num);
if(isNaN(num))
    {
        num = 10;
    }
num = num + 10;
console.log(num);

//Prompts for a number
let response = prompt('What was your grade')
//Converts response into a number
let grade = Number(response);

//Checks is grade is "not not" a number
if(!isNaN(grade)){
    //Checks is grade is greater than 70
    if(grade >= 70){
        console.log('you passed!');
    }else{
        //runs is grade is not greater than 70
        console.log('you failed');
    }
}else{
    //runs if number is not a number.
    console.log(response, 'is not a number')
}
