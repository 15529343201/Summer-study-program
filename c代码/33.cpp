//��31:����һ�����źõ�9��Ԫ�ص����飬������һ����Ҫ��ԭ������Ĺ��ɽ������������С�
#include<stdio.h>
int main()
{
    int a[10],i,index,s;
    for(i=0;i<9;i++)
    {
        scanf("%d",&a[i]);
    }
    scanf("%d",&s);
    for(i=0;i<9;i++)
    {
        if(s<a[i])
        {
            index=i;
            break;
        }
    }
    if(i==9)
    {
    a[9]=s;
    }
    else{
        for(i=9;i>index;i--)
        {
            a[i]=a[i-1];
        }
        a[index]=s;
    }
    for(i=0;i<10;i++)
    {
        printf("%d\n",a[i]);
    }
}

