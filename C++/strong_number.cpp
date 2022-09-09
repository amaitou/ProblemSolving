
#include <string>
using namespace std; 

int factorial(int value)
{
  if(value <= 1)
    return value ;
  else
    return value * factorial(value - 1) ;
}

string strong_num (int number )
{
    string s = to_string(number) ;
    int result = 0 ;
    for(int i = 0 ; i < s.size() ; i++)
    {
    	result += factorial(s[i] - '0') ;
    }
    return (number == result) ? "STRONG!!!!" : "Not Strong !!" ;
}

// Link: https://www.codewars.com/kata/5a4d303f880385399b000001
