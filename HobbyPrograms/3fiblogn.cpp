#include<iostream>
#include<stdio.h>
using namespace std;


void matmul(int **arr,int **arr1)
{
    int a=(arr[0][0] * arr1[0][0]) + (arr[0][1]*arr1[1][0]);
    int b=(arr[0][0] * arr1[0][1]) + (arr[0][1]*arr1[1][1]);
    int c=b;
    int d=(arr[1][0] * arr1[0][1]) + (arr[1][1] * arr1[1][1]);
    arr[0][0]=a;
    arr[0][1]=b;
    arr[1][0]=c;
    arr[1][1]=d;

}
void fibn(int **arr, int n)
{

 if(n==0)
 {
    arr[0][0]=1;
    arr[0][1]=0;
    arr[1][0]=0;
    arr[1][1]=-1;
 }
 else if(n==1)
 {
    arr[0][0]=1;
    arr[0][1]=1;
    arr[1][0]=1;
    arr[1][1]=0;
 }
 else if(n%2==0)
 {
    fibn(arr,n/2);
    matmul(arr,arr);
 }
 else
 {
    int **a;
    a=new int*[2];
    a[0]=new int[2];
    a[1]=new int[2];
    a[0][0]=1;
    a[0][1]=1;
    a[1][0]=1;
    a[1][1]=0;
    fibn(arr,n-1);
    matmul(arr,a);
    delete a;
 }
}
int main()
{
    int **arr;
    arr=new int*[2];
    arr[0]=new int[2];
    arr[1]=new int[2];
    arr[0][0]=1;
    arr[0][1]=1;
    arr[1][0]=1;
    arr[1][1]=0;
    int n=22;
    cin>>n;
    fibn(arr,n);
    cout<<arr[0][1];

return 0;
}
