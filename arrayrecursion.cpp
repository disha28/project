#include<bits/stdc++.h>
using namespace std;

int search(int a[],int n,int k)
{ int c;
    if(n==0)
    return 0;
    
    if(a[n]==k)
    return 1;
    search(a,n-1,k) ;
             
    
}

int main() {
	int n, k,c;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
	{
	    cin>>a[i];
	}
	cin>>k;
	c=search(a,n,k);
	cout<<c;
	
	
	
	
	//return 0;
}