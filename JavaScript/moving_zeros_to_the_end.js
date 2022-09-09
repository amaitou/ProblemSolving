
var moveZeros = function (arr) 
{
    // TODO: Program me

    let a = [] ;
        b = [] ;
    for(let i = 0 ; i < arr.length ; i++)
    {
        if(arr[i] === 0)
        {
            b.push(arr[i]) ;
        }
        else
        {
            a.push(arr[i]) ;
        }
    }
    return [...a , ...b] ;
}

// Link: https://www.codewars.com/kata/52597aa56021e91c93000cb0
