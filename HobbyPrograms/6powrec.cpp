#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
float pow(int x,int y);
float pow(int x,int y)
{
    if(y>1)
    {
    if(y%2==0)
    return (pow(x,y/2)*pow(x,y/2));
    else
    return (pow(x,(y-1)/2)*pow(x,(y-1)/2)*x);
    }
    else if(y<0)
    return (1/pow(x,abs(y)));
    else if(y==1)
    return x;
    else
    return 1;
}
int main()
{
cout<<pow(2,-2);
}
