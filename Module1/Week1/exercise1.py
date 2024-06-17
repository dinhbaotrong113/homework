def Pre(tp,fp):
    return tp/(tp+fp)
def Rec(tp,fn):
    return tp/(tp+fn)
def exercise1(tp,fp,fn):
        if (type(fn)!=int)or(type(tp)!=int)or(type(fp)!=int):
            print("fn, tp, fp must be int")
        elif (fn<=0)or(tp<=0)or(fp<=0):
            print("fn, tp, fp must be greater than zero")
        else:
            f1=2*(Pre(tp,fp)*Rec(tp,fn))/(Pre(tp,fp)+Rec(tp,fn))
            print(f"precision is:{Pre(tp,fp)}")
            print(f"recall is:{Rec(tp,fn)}")
            print(f"f1_score is:{f1}")
            return f1

print(round(exercise1(2,4,5),2))
