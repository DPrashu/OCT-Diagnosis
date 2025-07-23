import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

transform = transforms.Compose([
  transforms.Resize((28,28)),
  transforms.ToTensor()
])

class MyNetwork(nn.Module):
  def __init__(self):
    super().__init__()
    self.feature_extraction = nn.Sequential(
        nn.Conv2d(in_channels=3,out_channels=16,kernel_size=3,stride=1,padding='same'),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,stride=2),

        nn.Conv2d(in_channels=16,out_channels=32,kernel_size=3,stride=1,padding='same'),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,stride=2)
    )
    self.classifier = nn.Sequential(
        nn.Flatten(),

        nn.Linear(32*7*7,32),
        nn.ReLU(),
        nn.Dropout(0.3),

        nn.Linear(32,16),
        nn.ReLU(),
        nn.Dropout(0.3),

        nn.Linear(16,4)
    )

  def forward(self,x):
    out = self.feature_extraction(x)
    out = self.classifier(out)
    return out

def preprocess(image):
  image = image.convert('RGB')
  image = transform(image).unsqueeze(0)
  return image

def predict(image):
  idx_to_label = {0:'CNV',1:'DME',2:'Drusen',3:'Normal'}
  model = MyNetwork()
  model.load_state_dict(torch.load('model_weights28.pth',map_location=torch.device("cpu")))
  model.eval()

  with torch.no_grad():
    output = model(image)
    idx = torch.max(output,dim=1)[1]
    return idx_to_label[idx.item()]
