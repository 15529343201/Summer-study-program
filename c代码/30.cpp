//��29���ҳ�6x6����ÿ�о���ֵ����Ԫ�أ�����ͬ�Խ���Ԫ�ؽ��н��� 
#include<stdio.h>
#include<math.h>
int main()
{
    int i,j,array[6][6],k=0,t;
    for(i=0;i<6;i++)
    for(j=0;j<6;j++)
       scanf("%d,",&array[i][j]);
    for(i=0;i<6;i++)
    {
         k=0;
         for(j=0;j<6;j++)
         {
         	if(abs(array[k][i])<abs(array[j][i]))
            {
			     k=j;
                 t=array[k][i];
                 array[k][i]=array[k][k];
                 array[k][k]=t;
		    }
        }
    }
    for(i=0;i<6;i++)
    {
         for(j=0;j<6;j++)
            printf("%d ",array[i][j]);
            printf("\n");
    }
    return 0;
}

