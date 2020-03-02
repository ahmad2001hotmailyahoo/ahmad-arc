#include<iostream>
using namespace std ;
int factorial();
int factorial(int fact)
{
	if(fact == 1)
		return 1 ;
	else
		return ( fact * factorial(fact-1) ) ;	
}
int main()
{
	int fact     ;
	cout << "The number of which you want to find factorial \n" ;
	cin  >> fact ;
	int l = factorial(fact) ; 
	cout << "the factorial of " << fact << " is  = " << l ;
}

