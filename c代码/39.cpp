//һ���M�׸߶��������䣬ÿ����غ󷵻�ԭ�߶ȵ�һ�룬�����¡� ���ڵ�N����غ󷴵���ߣ���N�����ʱ�����������ף� ������λС��
#include<stdio.h>
int main()
{
    float M,N,s,h;
    int i;
     
    scanf("%f%f",&M,&N);
    h=M;
    s=M;
    for(i=1;i<=N-1;i++)
    {
        h=h/2;
        s+=h*2;
         
    }
    printf("%.2f %.2f",h/2,s);
}

