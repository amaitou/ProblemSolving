
var uniqueInOrder = function(iterable)
{
    //your code here - remember iterable can be a string or an array
    let r = [] ;
    for(let i = 0 ; i < iterable.length ; i++)
    {
        if(r.length == 0 || r[r.length - 1] != iterable[i])
        {
            r.push(iterable[i]) ;
        }
    }
    return r ;
}

// Link: https://www.codewars.com/kata/54e6533c92449cc251001667
