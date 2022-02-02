/* ATM Services */
#include <stdio.h>

int main()
{
    int money,amount,pin,pin1,pin2,ch,a,first;
    money = 70000;
    first = 1;
    char c = 'y';
    
    while(c == 'y')
    {
        printf("\n   >>>ATM SERVICES<<<   \n");
        printf("\n1. To withdraw\n2. To deposit\n3. To check balance\n4. To reset pin\n5. To exit\n");
        printf("\nEnter your choice 1/2/3/4/5: ");
        scanf("%d",&ch);
        if((ch!=1)&&(ch!=2)&&(ch!=3)&&(ch!=4)&&(ch!=5))
        {
            while((ch!=1)&&(ch!=2)&&(ch!=3)&&(ch!=4)&&(ch!=5))
            {
                printf("\nEnter a valid choice 1/2/3/4/5: ");
                scanf("%d",&ch);
            }
        }

        else if(ch==5)
        {
            c='n';
            printf("\nThanks! Have a nice day!\n");
        }

        else if(first==1){
            printf("\nGenerate a PIN first");
            printf("\nEnter PIN: ");
            scanf("%d",&pin1);
            printf("Confirm PIN: ");
            scanf("%d",&pin2);
            if(pin1==pin2)
            {
                printf("\nPIN Created successfully!\n");
                pin = pin1;
                first++;
            }
            else
            {
                printf("\nPIN Mismatched\n");
            }
           
        }

        else if(ch==1)
        {
            printf("\nEnter amount to withdraw: ");
            scanf("%d",&amount);
            if(((amount%500==0)||(amount%2000==0)||(amount%200==0)||(amount%100==0))&&(amount<=money))
            {
                printf("Confirm your PIN: ");
                scanf("%d",&a);
                if(a==pin)
                {
                    money-=amount;
                    printf("\nCollect cash Rs.%d/-",amount);
                    printf("\nEnter 1. To check the balance else 0: ");
                    scanf("%d",&a);
                    if(a==1){
                        printf("\nUpdated Account Balance: Rs.%d/-\n",money);
                    }
                    else{
                        printf("");
                    }
                }
                else
                {
                    printf("\nYou Entered wrong PIN!\n");
                }
            }
            else
            {
                if(amount>money){
                    printf("\nInsufficient Account Balance!\n");
                }
                else
                printf("\nATM contains Rs.100,Rs.200,Rs.500,Rs.2000!\n");
            }
        
        }

        else if(ch==2)
        {
            printf("\nEnter amount to deposit: ");
            scanf("%d",&amount);
            if((amount%500==0)||(amount%2000==0)||(amount%200==0)||(amount%100==0))
            {
                printf("Confirm your PIN: ");
                scanf("%d",&a);
                if(a==pin){
                    money+=amount;
                    printf("\nMoney is collected successfully!");
                    printf("\nEnter 1. To check the balance else 0: ");
                    scanf("%d",&a);
                    if(a==1){
                        printf("\nUpdated Account Balance: Rs.%d/-\n",money);
                    }
                }
                else
                {
                    printf("\nYou Entered a wrong PIN!\n");
                }
            }
            else
            {
                printf("\nOnly Rs.100, Rs.200, Rs.500, Rs.2000 notes are accepted\n");
            }
            
        }

        else if(ch==3)
        {
            printf("\nHello, ");
            printf("\nYour account balance is Rs.%d\n",money);
        }

        else if(ch==4)
        {
            printf("\nEnter old PIN: ");
            scanf("%d",&a);
            if(a==pin)
            {
                printf("\nEnter new PIN: ");
                scanf("%d",&pin1);
                printf("\nConfirm PIN: ");
                scanf("%d",&pin2);
                if(pin1==pin2)
                {
                    printf("\nPIN Reset successful!\n");
                    pin = pin1;
                }
                else
                printf("\nPIN Mismatched\n");
            }
            else
            {
                printf("\nYou Entered wrong PIN!\n");
            }
            
        }

    }

    return 0;
}