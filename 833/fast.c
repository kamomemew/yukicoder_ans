#include <stdio.h>
int N,Q;
long int x;
int q;
struct train
{
    long long int cool;
    long long int setpoint;
    int connected;
};


int main(){
    scanf("%d %d",&N,&Q);
    struct train t[N];
    for(int i =0;i<N;i++){
        scanf("%lld",&t[i].cool);
        t[i].setpoint=t[i].cool;
        t[i].connected=0;
    }
    for(int i =0;i<Q;i++){
        scanf("%d %ld",&q,&x);
        if(q==1){
            t[x-1].connected=1;
            //t[x].setpoint = t[x-1].setpoint+t[x].cool;
            for(int j=x-1;j<N;j++){
                if(t[j].connected == 1){
                    t[j+1].setpoint = t[j].setpoint+t[j+1].cool;
                }
                else{
                    break;
                }
            }
        }
        else if(q==2){
            //t[x].setpoint = t[x-1].setpoint-t[x].cool;
            for(int j=x-1;j<N;j++){
                if(t[j].connected == 1){
                    t[j+1].setpoint = t[j+1].setpoint-t[x-1].setpoint;
                }
                else{
                    break;
                }
            }
            t[x-1].connected=0;
        }
        else if(q==3){
            t[x-1].cool=t[x-1].cool + 1;
            t[x-1].setpoint=t[x-1].setpoint + 1;
            for(int j=x-1;j<N;j++){
                if(t[j].connected == 1){
                    t[j+1].setpoint = t[j+1].setpoint + 1;
                }
                else{
                    break;
                }
            }
        }
        else if(q==4){
            long long int res=0;
            for(int j=x-1;j<N;j++){
                if (t[j].connected ==0){
                    res=t[j].setpoint;
                    break;
                }
            }
            printf("%lld\n",res);
        }
    }
    return 0;
}