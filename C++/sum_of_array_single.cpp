
#include <bits/stdc++.h>

using namespace std ;

int repeats(vector<int> v)
{
	int s = 0 ;

	for(auto t : v)
	{
		if(count(v.begin() , v.end() , t) == 1)
			s += t ;
		else
			continue ;
	}
	return s ;
}

// Link: https://www.codewars.com/kata/59f11118a5e129e591000134
