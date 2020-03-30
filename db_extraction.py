import pandas as pd

def get_person(bg):
    
    data = pd.read_csv('data.csv')
    


    data1=[]
    for i in data.iterrows():
        print(i[1][2])
        if i[1][2]==bg:
            data1.append(tuple(i[1]))

    return data1