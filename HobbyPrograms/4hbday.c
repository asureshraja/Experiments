#include<stdio.h>
#include <windows.h>
#define sleep(n) Sleep(n)
#define q SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE)
#define w for(i=0;
#define ee ;i++)
#define r printf(
#define t );
int main()
{
int i,j=0;
r "\n" );
q,14  );
    w i<5 ee
   {
    j++;
    r " " );
    if(j<2)
    {r "()" ); j=0;}
   }
   r "\n" );
q, FOREGROUND_RED  );
   w i<5 ee
   {
    j++;
    r " " );
    if(j<2)
    {q, i+5 ); r "||"  ); j=0;}
   }
   q, 12 );
   r "\n" );
    w i<17 ee
    r "." );
    q, 14 );
    r "\n" );
    r ". " );
    q, 2 );
    r "HAPPY" );
    w i<9 ee
    r " " );
    q, 14 );
    r ". \n." );
    q, 2 );
    w i<5 ee
    r " " );
    r "BIRTHDAY  " );
    q, 14 );
    r ". \n" );
    w i<17 ee
    r "." );
   r "\n" );
}
