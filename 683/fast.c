#include <stdio.h>
long int a,b;
void op(long int x,long int y){
        if (x==0 | y==0){
            printf("Yes\n");
            exit(0);
        }
    if ((x%2==1)&&(y%2==1)){
        return;
    }
    else if((x%2==0)&&(y%2==0)){
        if ((x/2)%2==1){
            op(x-1,y/2);
        }
        else if ((y/2)%2==1){
            op(x/2,y-1);
        }
        else{
            op(x-1,y/2);
            op(x/2,y-1);
        }
    }
    else if (x%2==0){
        op(x/2,y-1);
    }
    else{
        op(x-1,y/2);
    }
}
int main(){
    scanf("%ld %ld",&a,&b);
    op(a,b);
    printf("No\n");
    return 0;
}
