//��13���������ȫƽ�����������������ȫƽ����������λ������ͬ
#include<stdio.h>
int main(void)
{
	int i,j;
	int bai,ge,shi;
	printf("the result is:\n");
	for(i=100;i<=999;i++)
	{
		j=10;
		while(j*j<=i)
		{
			if(i==j*j)
			{
				bai=i/100;
				shi=i/10%10;
				ge=i%10;
				if(bai==shi||bai==ge||shi==ge)
				printf("%5d",i);
			}
			j++;
		}
	}
 } 

