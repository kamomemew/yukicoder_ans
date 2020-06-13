#include <stdio.h>
int N,S,X,Y,Z;

void mk_arr_int (int arr[N]){
    arr[0]=S;
    int prev = S;
    for(int i=1;N>i;i++){
        prev = (X * prev + Y) % Z;
        arr[i] = prev;
    }
}

void mk_arr(int arr[N],int bool_arr[N]){
    for(int i=0;N>i;i++){
        if (arr[i]%2 == 0){
            bool_arr[i] = 0;
        }
        else{
            bool_arr[i] = 1;
        }
    }
}

void mask_and_xor(int arr[N],int i,int j,int m,int n){
    int length = n-m;
    int mini_arr[length];
    for(int c=i-1;c<j;c++){
        mini_arr[c-i] = arr[c]; 
    }
    for(int c=m-1;c<n;c++){
        arr[c] = mini_arr[c-m] ^ arr[c];
    }
}

int main(){
    
    scanf("%d %d %d %d %d",&N,&S,&X,&Y,&Z);
    int arr[N];
    int bool_arr[N];
    int Q;
    int I,J,K,L;
    scanf("%d",&Q);
    mk_arr_int(arr);
    mk_arr(arr,bool_arr);
    
    for(int i=0;i<Q;i++){
        scanf("%d %d %d %d",&I,&J,&K,&L);
        mask_and_xor(bool_arr,I,J,K,L);
    }


    for(int i=0;i<N;i++){
        if (bool_arr[i]==1){
            printf("%s","O");
        }
        else{
            printf("%s","E");
        }
    }
    return 0;
}