
#include <bits/stdc++.h>

using namespace std ;

int findOdd(const vector<int>& numbers)
{
	int r = 0 ;
	for(auto t : numbers)
	{
		if(count(numbers.begin() , numbers.end() , t) % 2 != 0)
			r = t ;
		else
			continue ;
	}
	return r ;
}

// Link: https://www.codewars.com/kata/54da5a58ea159efa38000836
