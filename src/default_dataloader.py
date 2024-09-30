from torch.utils.data import Dataset

class DefaultDataset(Dataset):
    def __init__(self, feats, tags):
        self.feats = feats
        self.tags = tags

    def __len__(self):
        return len(self.feats)

    def __getitem__(self, index):
        return self.feats[index], self.tags[index]