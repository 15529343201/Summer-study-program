//��������������죬��n���n�Ӽ������룩�����ڼ�
#include<stdio.h>
int main()
{
   int n,a;
   scanf("%d",&n);
   a=n%7;
   switch(a)
   {
      case 1:printf("����һ");break;
      case 2:printf("���ڶ�");break;
      case 3:printf("������");break;
      case 4:printf("������");break;
      case 5:printf("������");break;
      case 6:printf("������");break;
      case 0:printf("������");break;
   }
}  

