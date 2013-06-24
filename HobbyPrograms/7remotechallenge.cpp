#include<iostream>
#include<math.h>
#include<stdlib.h>
using namespace std;
int getmoves(int cur,int next,int length,int sblock[]);
int updatemoves(int &moves,int temp);
int updatemoves(int &moves,int temp)
{
    if(moves>temp)
    moves=temp;
}
int getmoves(int cur,int next,int length,int sblock[])
{
    int i,j;
    for(i=0;i<length;i++)
    if(sblock[i]>=cur)
    break;
    for(j=0;j<length;j++)
    if(sblock[j]>=cur)
    break;
    return (abs(abs(cur-next)-abs(i-j)));
}
int main()
{
    int noc,nob,moves;
    cout<<"enter no of channels";
    cin>>noc;
    cout<<"enter no of blocked list";
    cin>>nob;
    int i=0; int block[nob+1];int j=0,temp;
    for(i=0;i<nob;i++)
    cin>>block[i];
    for(i=0;i<nob;i++)
    {
        for(j=0;j<nob;j++)
        {
            if(block[i]<block[j])
            {
                temp=block[i];
                block[i]=block[j];
                block[j]=temp;
            }
        }
    }
    int cur,next,back;
    cout<<"enter current channel number";
    cin>>cur;
    cout<<"enter next channel number";
    cin>>next;
    cout<<"enter back channel number";
    cin>>back;
//    moves=log10(cur)+1;
    temp=getmoves(cur,next,nob,block);
    //if(moves>temp)
    //moves=temp;
    updatemoves(moves,temp);
    temp=getmoves(back,next,nob,block);
    //if(moves>temp)
    //moves=temp;
    updatemoves(moves,temp);
    if(cur>noc/2 &&next <noc/2)
    {
    temp=getmoves(cur,noc,nob,block)+getmoves(1,next,nob,block)+1;
    }
    //if(moves>temp)
   // moves=temp;
    updatemoves(moves,temp);
    if(cur<noc/2 &&next >noc/2)
    {
    temp=getmoves(cur,1,nob,block)+getmoves(noc,next,nob,block)+1;
    }
    //if(moves>temp)
   // moves=temp;
    updatemoves(moves,temp);
    if(next>noc-10 &&next <noc)
    {temp=getmoves(1,next,nob,block)+1;}
   // if(moves>temp)
    //moves=temp;
    updatemoves(moves,temp);
    if(next>9 && next <20)
    {temp=next-9+1;}
    //if(moves>temp)
    //moves=temp;
    updatemoves(moves,temp);
    cout<<"moves="<<moves;
}
