import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
from transformers import AutoProcessor, BarkModel
processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")