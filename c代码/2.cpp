//��1:ʮ����ת���ɶ�����
#include<stdio.h>
int main(void)
{
   int i=0,n;
   int d[32];
   printf("������һ��ʮ������:");
   scanf("%d",&n);
   while(n>0)
   {
   	 d[i]=n%2;
   	 i++;
   	 n=n/2;
   }
   for(i--;i>=0;i--)
   {
   	 printf("%d",d[i]);
   }
   return 0;
} 

