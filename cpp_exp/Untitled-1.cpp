#include <iostream>
using namespace std;
 
int main() {
  int hour,minute,timeh,timem= 0;
  cin >>hour >> minute;

if(minute>=45)
   timeh = hour;
   timem = minute-45;
   cout<<timeh<<timem;
  

else if(hour>=1 and minute<45)
  timeh = hour-1;
  timem = minute +15;
  cout<<timeh<<timem;
 

else
    timeh = 23;
    timem = minute + 15;
   cout<<timeh<<timem;

}
