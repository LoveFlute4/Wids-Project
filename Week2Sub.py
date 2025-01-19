import torch
import torch.utils.data.dataloader
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
train = datasets.MNIST("", train=True, download= True, transform= transforms.Compose([transforms.ToTensor()]))
test = datasets.MNIST("", train=True, download= True, transform= transforms.Compose([transforms.ToTensor()]))

trainset = torch.utils.data.DataLoader(train , batch_size= 10, shuffle= True)
testset = torch.utils.data.DataLoader( test , batch_size= 10, shuffle= True)


import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 100)
        self.fc2 = nn.Linear(100, 64)
        self.fc3 = nn.Linear(64, 20)
        self.fc4 = nn.Linear(20, 10)

    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x,dim=1)
net = Net()
print(net)

import torch.optim as optim
loss_func = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(),lr = 0.001)

for epoch in range(3):
    for data in trainset:
        X,y = data
        net.zero_grad()
        output = net(X.view(-1,784))
        loss = F.nll_loss(output,y)
        loss.backward()
        optimizer.step()
    
    print(loss)

correct = 0
total = 0
with torch.no_grad():
    for data in testset:
        X,y = data
        output = net(X.view(-1,784))
        for idx, i in enumerate(output):
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1

print(f"Accuracy : {round(correct/total , 3)}")

img = int(input("HOw many images do you want to see? (Maximun 10)"))
userCount = 0
nnCount = 0
plt.ion()
for i in range(img):
    plt.imshow(X[i].view(28,28))
    plt.show()
    plt.pause(2)
    plt.close()
    #UserNum = int(input("What number do you see: "))
    #if(int(UserNum) == y[i].item()):
    #    print(f"You Guessed Correct! It is {UserNum}.")
    #    userCount += 1
    #else:
    #    print(f"Incorect! The number was {y[i].item()}")
    
    if(torch.argmax(net(X[i].view(-1,784))[0]) == y[i]):
        print("The nn was right!")
        nnCount += 1
    else:
        print("The nn was wrong :(")

#print( f"Your Accuracy was {round(((userCount/img) * 100),3) }")
print( f"Neural Network's Accuracy was {round(((nnCount/img) * 100),3)}")

