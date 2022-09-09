
function calculate(str)
{
	let a = str.replace(/\s/g , "").split("+") , r = 0 ;
	for(let i = 0 ; i < a.length ; i++)
	{
		r += parseInt(a[i]) ;
	}
	return r ;
}

// Link: https://www.codewars.com/kata/59512d72944ca1feb000013d
