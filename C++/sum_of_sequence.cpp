
#include <bits/stdc++.h>

using namespace std ;

int sequenceSum(int start, int end, int step)
{
	int r = 0 ;
	for(int i = start ; i < end + 1 ; i = i + step)
	{
		r += i ;
	}
	return r ;
}

// Link: https://www.codewars.com/kata/586f6741c66d18c22800010a
