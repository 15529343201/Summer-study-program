//��9���Ӽ�������һ�����������жϸ����Ƿ�������������������Ĳ�������������ʾ�������
//��C���Ա�д����ʵ�֡�
//�������ݣ����룺7          �����7������ ��
//                  ���룺9           �����9�������� ��
//                   ���룺-3          ������������������������ 
#include <stdio.h>
int is_prime( int n )
{
    int i;
    if ( n < 2 )
        return 0;
    for( i=2; i<=n/2;i++ )
        if ( n%i==0 )
            return 0;
    return 1;
}
int main()
{
    int n;
    while( scanf("%d", &n)!=EOF )
    {
        if ( n <= 0 )
        {
            printf("���������������������\n");
        }
        else 
        {
            if ( is_prime( n ) )
                printf("%d��������\n", n);
            else
                printf("%d����������\n", n);
        }
    }
    return 0;
}

