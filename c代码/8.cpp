//��7�� ��дһ���ж������ĺ���
#include<stdio.h>
int prime(int n)
{
   int i;
   for(i=2;i<n;i++)
   {
   	if(n%i==0)
   	{
   		return 0;
	}
	return 1;
   }
} 
int main(void)
{
	int m;
	scanf("%d",&m);
	if(prime(m))
	{
		printf("%d������",m);
	}
	else
	{
		printf("%d��������",m);
	}
	return 0;
}

