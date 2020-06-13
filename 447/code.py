
N=input()
magick_number=65 #ord("A")
L=list(map(int,input().split()))

paticipat={}
prob_solve = [1 for x in range(len(L))]
prob_star  =  L
def score (star,ac):
    # 50×★の数+50×★の数 / (0.8+ 0.2×ACの順位)
    return int(50 * star +50 * star /(0.8 + 0.2*ac))

T=int(input())
person,query=[],[]
for i in range(T):
    p,q=input().split()
    person.append(p)
    query.append(q)

for p in list(set(person)):
    paticipat[p]=[[0 for x in range(len(L))],0]
    #paticipat.append({"name":p,"score":[1 for x in range(len(L))]})
#for p,q in zip(person,query):
#    q=ord(q)-magick_number
#    paticipat[p][q]=score(prob_star[q],prob_solve[q])
#    prob_solve[q]=prob_solve[q]+1

for time in range(len(query)):
    p,q=person[time],ord(query[time])-magick_number
    paticipat[p][0][q]=score(prob_star[q],prob_solve[q])
    paticipat[p][1]=len(query)-time
    prob_solve[q]=prob_solve[q]+1

l_kekka=[]
for k in paticipat.keys():
    l_kekka.append({"name":k,"sum":sum(paticipat[k][0]),"time":paticipat[k][1]})
#    l_kekka.append([k,kekka[k]])

score_sorted = sorted(l_kekka,reverse=True, key=lambda x:(x["sum"],x["time"]))
#print(score_sorted)
#exit()
for i in range(len(score_sorted)):
    print("{} {} {} {}".format(i+1,score_sorted[i]["name"]," ".join(map(str,paticipat[score_sorted[i]["name"]][0])),score_sorted[i]["sum"]))
