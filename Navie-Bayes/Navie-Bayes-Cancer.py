#Author Kaihao Zhao 09/21/2016
# Read data file
with open("breast_cancer.data") as data_file:
  data = [ map(float, line.split()) for line in data_file ]

# Read whole Label file
with open("breast_cancer.labels") as label_file:
  labels = { int(i.split()[1]) : int(i.split()[0]) for i in label_file }

# Read Training Label file
with open("breast_cancer.trainlabels.2") as label_file:
  trainlabels = { int(i.split()[1]) : int(i.split()[0]) for i in label_file }

# Cout number of 0s and 1s
label_class = [sum(1 for i in trainlabels if trainlabels[i]==0), sum(1 for i in trainlabels if trainlabels[i])]

# Calculate the mean
mean0 = [ sum(data[i][j] / label_class[0] for i in range(len(data)) if trainlabels.get(i) is not None and trainlabels[i] == 0) for j in range(len(data[0])) ]
mean1 = [ sum(data[i][j] / label_class[1] for i in range(len(data)) if trainlabels.get(i) is not None and trainlabels[i] == 1) for j in range(len(data[0])) ]
# To set default mean as 1
mean0 = [ mean + 1.0/label_class[0] for mean in mean0]
mean1 = [ mean + 1.0/label_class[1] for mean in mean1]

# Calculate standard deviation
s0 = [ sum( pow(data[i][j]-mean0[j], 2.0) / label_class[0] for i in range(len(data)) if trainlabels.get(i) is not None and trainlabels[i]==0) for j in range(len(data[0])) ]
s1 = [ sum( pow(data[i][j]-mean1[j], 2.0) / label_class[1] for i in range(len(data)) if trainlabels.get(i) is not None and trainlabels[i]==1) for j in range(len(data[0])) ]

# Calculate prediction
predict = { i: int(sum(pow(data[i][j]-mean0[j], 2.0)/s0[j] for j in range(len(data[0]))) >= sum(pow(data[i][j]-mean1[j], 2.0)/s1[j] for j in range(len(data[0])))) for i in range(len(data)) if trainlabels.get(i) is None }


# Calculate Balanced Error Rate
print (float(len(list(filter(lambda i : labels.get(i)==0 and predict.get(i)==1, labels))))
      / float(len(list(filter(lambda i : labels.get(i)==0 and predict.get(i) is not None, labels))))
      + float(len(list(filter(lambda i : labels.get(i)==1 and predict.get(i)==0, labels))))
      / float(len(list(filter(lambda i : labels.get(i)==1 and predict.get(i) is not None, labels))))) / 2.0
