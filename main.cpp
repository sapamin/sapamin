#include <iostream>

using namespace std;
int index=0;
int array[10000];

void push()
{   
    cin>>array[index];
    index++;
}

void pop()
{
    cout<<array[index];
    index--;
}

void size()
{
    cout<<"정수 개수:"<<index;
}

void empty()
{
    if(index>0)
        cout<<"0";
    else
        cout<<"1";
}

void top()
{
    if(index=0)
        cout<<"-1";
    else
        cout<<array[index];
}

int main()
{
int array[10000];
int count;
int i=0;
cin>>count;
for(i=0;i<count;i++)
{
 string cmd;
 cin>>cmd;
 if(cmd=="push")
    push();
 else if(cmd=="pop")
    pop();
 else if(cmd=="size")
    size();
 else if(cmd=="empty")
    empty();
 else if(cmd=="top")
    top();

 }
}

else =