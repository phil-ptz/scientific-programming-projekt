import torch
import torch.nn as nn
from PIL import Image
import torchvision.transforms as transforms

# Konstanten
IMAGE_SIZE = 256
classes = ["fake", "real"]
device = "cpu"

# Modellarchitektur zum Laden der Gewichte
class CNNModel(nn.Module):
    """
    Model architecture TinyVGG from:
    https://poloclub.github.io/cnn-explainer/
    """
    def __init__(self, input_shape: int, hidden_units: int, output_shape: int):
        super().__init__()
        self.block_1 = nn.Sequential(
            nn.Conv2d(in_channels=input_shape,
                      out_channels=hidden_units,
                      kernel_size=3, # how big is the square that's going over the image?
                      stride=1, # default
                      padding=1),# options = "valid" (no padding) or "same" (output has same shape as input) or int for specific number
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_units,
                      out_channels=hidden_units,
                      kernel_size=3,
                      stride=1,
                      padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2,
                         stride=2) # default stride value is same as kernel_size
        )
        self.block_2 = nn.Sequential(
            nn.Conv2d(hidden_units, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Conv2d(hidden_units, hidden_units, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.5),
            nn.Linear(in_features=hidden_units * (IMAGE_SIZE//4) * (IMAGE_SIZE//4),
                    out_features=output_shape)
        )


    def forward(self, x: torch.Tensor):
        x = self.block_1(x)
        x = self.block_2(x)
        x = self.classifier(x)
        return x

# Laden der Gewichte
model = CNNModel(input_shape=3, hidden_units=32, output_shape=2).to(device)
model.load_state_dict(torch.load("core/classifier/model_weights_95.pth", map_location=torch.device('cpu')))
model.eval()

def classify_image(image_path):

    # Bild laden und vorverarbeiten

    image = Image.open(image_path).convert("RGB")  # wichtig: RGB erzwingen

    transform = transforms.Compose([
        transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
        transforms.ToTensor(),
    ])

    input_tensor = transform(image).unsqueeze(0).to(device)

    # Vorhersage
    with torch.no_grad():
        output = model(input_tensor)
        predicted_class = output.argmax(dim=1).item()
        return classes[predicted_class]