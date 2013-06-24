#include <iostream>
#include <stdio.h>
using namespace std;
//most occurence without hashing
int findCandidate(int a[], int size)
{
    int maj_index = 0, count = 1;
    int i;
    for(i = 1; i < size; i++)
    {
        if(a[maj_index] == a[i])
            count++;
        else
            count--;
        if(count == 0)
        {
            maj_index = i;
            count = 1;
        }
    }
    return a[maj_index];
}
int main()
{
    int a[] = {1, 2, 1, 2, 1,2,3,3,1,1,3,3};
    int n=12;
    int cutoffpt=n/3;
    while(n>cutoffpt)
    {
        int c = findCandidate(a,n);
        int flag=0,j,k;
        for(int i=0;i<n;i++)
        {
        if(flag==1)
        {
            if(a[i]!=c)
            {
                int temp=a[j];
                a[j]=a[i];
                a[i]=temp;
                j++;
            }
        }
        if(a[i]==c&&flag!=1)
        {
            flag=1;
            j=i;
        }
    }
/*
    for(int i=0;i<n;i++)
    cout<<a[i];
*/
    if(n-j>cutoffpt)
    cout<<c<<endl;
    n=j;
    }

    return 0;
}
