#include<stdio.h>
int main()
{
   int n, sum;

   printf("Enter n value: \n");
   scanf("%d",&n);

    sum = 0;
    printf("%d",sum);
   for(int i=1; i<=n; i++)
   {
     printf("+%d",i);
     sum += i; //sum = sum + i;
   }

   printf("=%d\n",sum);

   return 0;
}
