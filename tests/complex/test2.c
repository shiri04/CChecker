#include <stdio.h>
#include <string.h>
#define LB(X) ((X)&(-(X)))

typedef long long LL;
LL n;
int q;
char str[100010];

int main(void)
{
    //freopen("tree.in","r",stdin);
    //freopen("tree.out","w",stdout);
    scanf("%I64d%d",&n,&q);
    int i,j;
    LL u;
    for(i=1;i<=q;i++)
    {
        scanf("%I64d%s",&u,str);
        for(j=0;str[j];j++)
            if( str[j]=='L' && u>LB(u)/2 )
                u-=LB(u)/2;
            else if( str[j]=='R' && u+LB(u)/2<=n )
                u+=LB(u)/2;
            else if( str[j]=='U' && LB(u-LB(u))==LB(u)*2 )
                u-=LB(u);
            else if( str[j]=='U' && LB(u+LB(u))<=n && LB(u+LB(u))==LB(u)*2 )
                u+=LB(u);
        printf("%I64d\n",u);
    }
    return 0;
}
