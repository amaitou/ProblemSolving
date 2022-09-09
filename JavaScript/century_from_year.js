function century(year) {
  let i = 0
  while(year > 0)
    {
      i++
      year -= 100
    }
  return i
}

// Link: https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
