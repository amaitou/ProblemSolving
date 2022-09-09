#include <cmath>
#include <string>

using namespace std ;

bool narcissistic(int value)
{
  string s = to_string(value) ;
  int n = 0 ;

  for(int i = 0 ; i < s.length() ; i++)
  {
    n += pow((int)s[i] - '0' , s.length()) ;
  }
  return n == value ;
}

// Link: https://www.codewars.com/kata/5287e858c6b5a9678200083c
