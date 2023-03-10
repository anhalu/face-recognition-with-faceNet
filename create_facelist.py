import glob
import torch 
from torchvision import transforms
from facenet_pytorch import InceptionResnetV1, fixed_image_standardization
import os
from PIL import Image
import numpy as np

IMG_PATH = './Datasets'


device =  torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)
def trans(img):
    transform = transforms.Compose([
            transforms.ToTensor(),
            fixed_image_standardization
        ])
    return transform(img)


model = InceptionResnetV1(
    classify=False,
    pretrained="casia-webface"
).to(device)


model.eval()

embeddings = []
names = []

for usr in os.listdir(IMG_PATH):
    embeds = []
    for file in glob.glob(os.path.join(IMG_PATH, usr)+'/*.jpg'):
        try:
            img = Image.open(file)
        except:
            continue
        with torch.no_grad():
            embeds.append(model(trans(img).to(device).unsqueeze(0)))
    if len(embeds) == 0:
        continue
    embedding = torch.cat(embeds).mean(0, keepdim=True) 
    embeddings.append(embedding) 
    # print(embedding)
    names.append(usr)
    
embeddings = torch.cat(embeddings) #[n,512]
names = np.array(names)

if device == 'cpu':
    torch.save(embeddings,"faceslistCPU.pth")
else:
    torch.save(embeddings,"faceslist.pth")
np.save("usernames", names)
print('Update Completed! There are {0} people in FaceLists'.format(names.shape[0]))