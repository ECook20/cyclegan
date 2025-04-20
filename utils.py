import os
from torchvision.io import read_image
from torch.utils.data import Dataset
from torchvision.transforms import ToTensor

class GANDataset(Dataset): # two separate datasets for day/night -> four datasets in total
    def __init__(self, root_path="./data", day=True, train=True, transform=None):
        if train:
            self.img_dir = os.path.join(root_path, "trainA") if day else os.path.join(root_path, "trainB")
        else:
            self.img_dir = os.path.join(root_path, "testA") if day else os.path.join(root_path, "testB")

        self.transform = transform

    def __len__(self):
        return len(os.listdir(self.img_dir))

    def __getitem__(self, idx):
        img_path = self.img_dir + "/" + str(idx) + ".jpg"
        image = read_image(img_path)

        if self.transform:
            image = self.transform(image)
        return image.float() / 255.