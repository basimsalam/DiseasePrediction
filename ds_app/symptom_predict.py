import csv
import csv

# Open the CSV file in read mode
i=0
x=[]
y=[]
distdis=[]
distsym=[]
with open(r'C:\Users\HP\Desktop\Regional\dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if i!=0:
            if row[0] not in distdis:
                distdis.append(row[0])
            y.append(distdis.index(row[0]))
            r=[]
            for j in range(1,len(row)):
                if row[j]=="":
                    break
                if row[j] not in distsym:
                    distsym.append(row[j])
                r.append(row[j])
            x.append(r)

        i=i+1

print(x[0])
print(y[0])

print(distsym)
print(distdis)
k=0
xdata=[]
for i in x:
    r=[]

    for j in distsym:

        if j in i:
            r.append(1)
        else:
            r.append(0)
    xdata.append(r)
    #print(r)
    k=k+1

print(xdata[0])


from sklearn.model_selection import train_test_split
# i.e. 70 % training dataset and 30 % test datasets
X_train, X_test, y_train, y_test = train_test_split(xdata, y, test_size = 0.30)

from sklearn.ensemble import RandomForestClassifier


clf = RandomForestClassifier(n_estimators=100)

# Training the model on the training dataset
# fit function is used to train the model using the training sets as parameters
clf.fit(X_train, y_train)

# performing predictions on the test dataset
y_pred = clf.predict(X_test)

# metrics are used to find accuracy or error
from sklearn import metrics

print()

# using metrics module for accuracy calculation
print("ACCURACY OF THE MODEL:", metrics.accuracy_score(y_test, y_pred))

#print(distsym)

input=[' skin_rash',' chills',	 'joint_pain',	' vomiting',	 'fatigue',	 'high_fever	',	' headache',	'	 nausea	',	' loss_of_appetite',	'	 pain_behind_the_eyes	',	' back_pain',	'	 muscle_pain',	'	 red_spots_over_body' ]
row=[]
for i in distsym:
    if i in input:
        row.append(1)
    else:
        row.append(0)
res=clf.predict([row])

print(res[0])

print(distdis[res[0]])