//��x����n�����������ĺ�
#include<stdio.h>
int main()
{
   int n,x,i,sum=0;
   scanf("%d%d",&x,&n);
   for(i=x;i<x+n;i++)
   {
      sum=sum+i;
   }
   printf("%d",sum);
} 

