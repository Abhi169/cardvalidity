/* Hans Peter Luhn's Algorithm to check validity of cards */

#include <stdio.h>
#include <string.h>

int main(){
    char name[20] = "";
    int len = 0,sum = 0,dig;
    long long int cardnum,cncopy;
    printf("Enter Card Number to check: ");
    scanf("%lli",&cardnum);
    cncopy = cardnum;

    while(cncopy>0)
    {
        len+=1;
        cncopy/=10;
    }

    int arr[len];

    for(int i=1;i<=len;i++)
    {
        arr[i] = (cardnum%10);
        cardnum/=10;
    }

    for(int i=1;i<=len;i++)
    {
        if(i==(len-1))
        {
            if(((arr[i]==1)||(arr[i]==2)||(arr[i]==3)||(arr[i]==4)||(arr[1]==5))&&(arr[i+1]==5))
            strcpy(name,"MASTERCARD");
            else if(((arr[i]==4)||(arr[i]==7))&&(arr[i+1]==3))
            strcpy(name,"AMERICAN EXPRESS");
            else if(arr[i+1]==4)
            strcpy(name,"VISA");
        }

    }

    for(int i=1;i<=len;i++)
    {
        if(i%2==0)
        {
            arr[i] = (2*arr[i]);
        }
        else
        {
            arr[i] = arr[i];
        }
    }

    for(int i=1;i<=len;i++)
    {
       dig = arr[i];
       if(dig!=0 && dig!=1 && dig!=2 && dig!=3 && dig!=4 && dig!=5 && dig!=6 && dig!=7 && dig!=8 && dig!=9)
       {
           while(dig>0)
           {
               sum += (dig%10);
               dig/=10;
           }
       }
       else
       {
           sum += dig;
       }
       
    }

    dig = sum%10;
    if(dig==0)
    {
        printf("VALID\n");
        printf("%s\n",name);
    }
    else
    {
        printf("INVALID\n");
    }

    
    return 0;
}