function FillOut()
{
	
	var elements = [document.forms['form1']['noun1'].value,
	document.forms['form1']['nouns'].value,
	document.forms['form1']['noun2'].value,
	document.forms['form1']['place'].value,
	document.forms['form1']['adjective'].value,
	document.forms['form1']['noun3'].value];

	var msg = `Be kind to your ${elements[0]}-footed ${elements[1]} <br /> For a duck may be somebody's ${elements[2]}, <br /> Be kind to your ${elements[1]} in ${elements[3]} <br />
Where the weather is always ${elements[4]}. <br /> <br /> You may think that this is the ${elements[5]}, <br /> Well it is.`;

	var p = document.getElementById("msg");
	p.style.borderStyle = 'dashed';
	p.innerHTML = msg;
}