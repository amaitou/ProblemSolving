function isanangram(s1 , s2)
{
    return s1.toLowerCase().split("").sort().join("") == s2.toLowerCase().split("").sort().join("")
}

function anagramCounter (wordsArray) 
{
    let c = 0 ;
    for(let i = 0 ; i < wordsArray.length ; i++)
    {
        for(let j = i + 1 ; j < wordsArray.length ; j++)
        {
            if(isanangram(wordsArray[i] , wordsArray[j]))
            {
                c++ ;
            }
        }
    }
  return c ;
}

// Link: https://www.codewars.com/kata/587e18b97a25e865530000d8
