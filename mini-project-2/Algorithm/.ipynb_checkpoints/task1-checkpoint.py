#Ignore warning
import torch
import warnings
warnings.filterwarnings("ignore")

data = torch.load('../dataset/dataset/part_one_dataset/train_data/1_train_data.tar.pth')
print(data['target'][0])