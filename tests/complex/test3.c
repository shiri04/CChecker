#include<stdio.h>
#include<stdlib.h>
int main(){
	long int xx,i2,y2=0,n2,i,x,y,n;
	int j,k;
	scanf("%ld %d",&n,&k);
	long int t[n],v[n-1];
	for(i=0;i<n;i++) t[i]=i+1;
	for(j=0;j<k;j++){
		scanf("%ld",&x);
		n2=n;
		if(n==x) y=0;
		else if(n>=x) y=x;
		else y=x%n;
	//if(y>=n) y=y-n-1;
		if(j!=k-1)printf("%d ",t[y]);
		else printf("%d",t[y]);
		
		for(i=y+1;i<n;i++) t[i-1]=t[i];n--;
		for(i=0;i<y;i++){
			xx=t[0];
			for(i2=0;i2<n-1;i2++){
				t[i2]=t[i2+1];
			}t[n-1]=xx;
		}
		
		
	//	for(i=0;i<n;i++) printf("%ld ",t[i]);
	
	//	system("pause");
		
	}
	
	
	return 0;
}
