//��10���Ӽ�����������һ������n,��̼��㲢���1-n֮�����������֮��
# include <stdio.h>
int SumPrime(int n)
{
    int i;
    int k;
    int sum=0;
    for(i=2;i<=n;++i )
    {
        for(k=2;k<i;++k)
        {
            if(i%k==0)
                break;
        }
     if(k == i) sum+= k;
    }
    return sum;
}
int main (void)
{
    int n;
    int sum;
    printf("please enter a number:");
    scanf("%d",&n);
    sum=SumPrime(n);
    printf("sum = %d\n",sum);
 
    return 0;
}

