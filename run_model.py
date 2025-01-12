import torch
from torch import nn
from torchvision import datasets
from torchvision.transforms import ToTensor


test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__() # super constructor
        self.flatten = nn.Flatten()
        self.linear_rule_stack = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512,10)
        )
        
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_rule_stack(x)
        return logits

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)

model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("./models/model.pth", weights_only=True))

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

model.eval()
x, y = test_data[0][0], test_data[0][1]
with torch.no_grad():
    x = x.to(device)
    pred = model(x)
    predicted = classes[pred[0].argmax(0)]
    actual = classes[y]
    print(f"Predicted: {predicted}, Actual: {actual}")
