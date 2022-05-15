from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# home page  
def home(request):
    return render(request,"pages/home.html")
def dashboard(request):
    return render(request,"pages/dashboard.html")
def login(request):
    return render(request,"pages/login.html")
def signup(request):
    return render(request,"pages/signup.html")
def about(request):
    return render(request,"pages/about.html")

def file(request):
    flag=0
    if request.method=='POST':
        flag=1
        file=request.FILES.get('files','ajdk')
        # print(file.name)
        # print(file.size)
        #dataset
        dataset = pd.read_csv(file, header = None)
        transactions = []
        #for i in range(0, 7501):
        #  temp=[]
        #  for j in range(0,20):
        #    temp.append(str(dataset.values[i,j]))
        #  transactions.append(temp)
        for i in range(0, 7501):
            transactions.append([str(dataset.values[i,j]) for j in range(0, 10)])
        #print(transactions)

        #creating model
        #para depends upon problem!
        from apyori import apriori
        rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)


        #output:


        #simple output:
        results = list(rules)
        #print(results)


        #welorganized output:
        #stackoverflow!
        def inspect(results):
            lhs         = [tuple(result[2][0][0])[0] for result in results]
            rhs         = [tuple(result[2][0][1])[0] for result in results]
            supports    = [result[1] for result in results]
            confidences = [result[2][0][2] for result in results]
            lifts       = [result[2][0][3] for result in results]
            return list(zip(lhs, rhs, supports, confidences, lifts))

        resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

        #Displaying the results non sorted
        #resultsinDataFrame

        #Displaying the results sorted
        # print(resultsinDataFrame.nlargest(n = 5, columns = 'Lift'))
        lst=list(resultsinDataFrame['Left Hand Side']) 
        rst=list(resultsinDataFrame['Right Hand Side'])
        llist=[]
        rlist=[]
        for obj in lst:
            llist.append("".join(obj))
        for obj in rst:
            rlist.append("".join(obj))
        final=[]
        for i in range(6):
            final.append((i+1,llist[i],rlist[i]))
        # print(final[0][0])
        # print(llist[0])
        # print(lst)
        context={
            # "content":resultsinDataFrame,
            "final":final,
            "flag":flag,
            "range":[0,1,2,3,4,5]
        }

        return render(request,"pages/file-input.html",context)
    context={
        "flag":flag
    }
    return render(request,"pages/file-input.html",context)
