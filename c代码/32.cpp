//��31:�Ӽ�������10��ѧ���ɼ��洢�������У���ɼ�����ߵ���źͳɼ�
#include<stdio.h>
int main()
{
    int a[11],max,i,j;
    for(i=1;i<11;i++)
    {
       scanf("%d",&a[i]);
    }
    max=a[1];
    for(i=1;i<11;i++)
    {
      if(max<a[i])
     { max=a[i];
 
      j=i;}
    }
    printf("%d %d",j,max);
}

