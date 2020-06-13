#  1  2  3  4  5  6  7  8
#  
#  1 --> (2 or 3)
#  2 --> (1 or 3)
#  3 --> (1 or 2)
#  
#  dist  count
#  3     2
#  4     2
#  5     2
#  


a=[]
N=int(input())

int i, N;
unsigned k;
scanf("%d", &N);
if (N <= 10) k = a[N];
else {
	for (i = 11; i <= N; i++) 
		a[i] = ((long long)a[i-3] + a[i-4] + a[i-5] + (a[i-6]<<1)) % MOD;
	k = a[N];
}
printf("%u\n", k);
return 0;
