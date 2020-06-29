from config import Config
from dataset import ML100kDataset
from model.general_recommender.bprmf import BPRMF
from trainer import Trainer


config = Config('properties/overall.config')
config.init()

dataset = ML100kDataset(config)
train_data, test_data = dataset.preprocessing(
    workflow=['split']
)

model = BPRMF(config, dataset)
trainer = Trainer(config, model)
trainer.train(train_data)
trainer.predict(test_data)