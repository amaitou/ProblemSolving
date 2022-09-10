
async function execute(action, nTimes)
{
    let arrayPromises = []
    let i = 0
    while(i < nTimes)
      {
        arrayPromises.push(action())
        ++i
      }
    await Promise.all(arrayPromises)
}

// Link: https://www.codewars.com/kata/5b2b4836b6989d207700005b
