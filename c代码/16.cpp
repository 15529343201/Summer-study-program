//��15:�Ӽ�����������һ���������У�������һ�����֣����Ҵ����� 
#include <stdio.h>
int main()
{
    int n,a[100],b,i,cnt=0;
 
    printf("�������������ĸ���:");
    scanf("%d", &n);
 
    printf("���������е���:\n");
    for(i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
 
    printf("����Ҫ��ѯ������:");
    scanf("%d", &b);
    for(i = 0; i < n; i++)
    {
       if(a[i] == b)
       cnt++;
    }
    printf("%d����%d��\n", b, cnt);
}

