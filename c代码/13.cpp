//��12���ж�һ�����Ƿ���ˮ�ɻ���
#include<stdio.h>
int judge(int n)
{
	int a,b,c;
	a=n%10;
	b=n/10%10;
	c=n/100;
	if(a*a*a+b*b*b+c*c*c==n)
	{
		return 1;
	}
	return 0;
} 
int main(void)
{
	int m;
	scanf("%d",&m);
	if(judge(m)==1)
	{
		printf("%d��ˮ�ɻ���",m);
	}
	else 
	{
		printf("%d����ˮ�ɻ���",m);
	}
	return 0;
}

