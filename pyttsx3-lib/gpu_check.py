import torch 

# device = "cuda" if torch.cuda.is_available() else "cpu"
# model.to(device)

if torch.cuda.is_available():
    print("GPU")
else:
    print("NO GPU")