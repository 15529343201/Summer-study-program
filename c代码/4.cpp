//��3���ݹ�������� 
#include<stdio.h>
void fun(int n)
{
	if(n>1)
	fun(n/2);
	printf("%d",n%2);
}
int main(void)
{
	 int x;
	 scanf("%d",&x);
	 fun(x);
}

