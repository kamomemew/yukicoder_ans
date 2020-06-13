#include <stdio.h>

int main(){
    int N;
    scanf("%d",&N);
    int cats[N];
    for(int i = 0; i < N; i++){
        scanf("%d", &cats[i]);
    }
    int nyan_count=0;
    for(int i = 0; i<N;i++){
        for(int j = i + 1;j<N;j++){
            if((cats[i]-i)-(cats[j]-j) >= j-i){
                nyan_count=nyan_count+1;
            }
        }
    }    
    printf("%d\n", nyan_count);    
    return 0;
}
