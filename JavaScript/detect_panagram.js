
function isalpha(character)
{
	if(character >= 'A' && character <= 'z')
		return true ;
	return false ;
}

function isPangram(string)
{
	let s = string.toLowerCase() ;
	let r = "" ;
	for(let i = 0 ; i < string.length ; i++)
	{
		if(isalpha(s[i]) && ! r.includes(s[i]))
		{
			r += s[i] ;
		}
	}
	return r.length == 26 ;
}

// Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
