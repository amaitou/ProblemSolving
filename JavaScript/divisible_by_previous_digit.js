
function divisibleByLast(n)
{
    let a = n.toString().split("") ;
        p = 0
        r = []

    for(let i = 0 ; i < a.length ; i++)
    {
        if(parseInt(a[i]) % p == 0)
            r.push(true) ;
        else
            r.push(false) ;
        p = parseInt(a[i]) ;
    }
    return r ;
}

// Link: https://www.codewars.com/kata/5a2809dbe1ce0e07f800004d
