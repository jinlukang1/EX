#include<cstdio>  
#define maxn 10000  
#define maxm 100  
#define mod 20123  
using namespace std;  
  
int n,m;  
int a[maxn+100][maxm+20];  
bool flag[maxn+100][maxm+20];  
  
int main()  
{  
  int i,j,k,last,ans;  
  scanf("%d%d",&n,&m);  
  for(i=1;i<=n;i++)  
    for(j=0;j<m;j++)  
      {  
        scanf("%d%d",&k,&a[i][j]);  
        flag[i][j]=k;  
        if(k)a[i][maxm+15]++;  
      }  
        
  scanf("%d",&last);  
  for(ans=0,i=1;i<=n;i++)  
    {  
      ans=(ans+a[i][last])%mod;  
      if(i==n)break;  
        
      k=a[i][last]%a[i][maxm+15];  
      if(k==0)k=a[i][maxm+15];  
        
      for(j=1;j<=k;j++)  
        {  
          while(!flag[i][last])last=(last+1)%m;  
          if(j==k)break;  
          last=(last+1)%m;  
        }    
    }      
  printf("%d\n",ans);    
  return 0;  
}
