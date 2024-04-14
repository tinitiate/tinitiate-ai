import csv
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, AdamW
from torch.utils.data import DataLoader, Dataset

# Define a custom dataset class to load data from the CSV file
class QADataset(Dataset):
    def __init__(self, csv_file, tokenizer, max_length=512):
        self.data = []
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file, delimiter="|")
            next(csv_reader)  # Skip header row if exists
            for row in csv_reader:
                question = row[0]
                context = row[1]
                answer = row[2]
                self.data.append((question, context, answer))
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        question, context, answer = self.data[idx]
        inputs = self.tokenizer(
            question,
            context,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        inputs["labels"] = self.tokenizer.encode(answer, max_length=self.max_length, padding="max_length", truncation=True, return_tensors="pt")[0]
        return inputs

# Define training parameters
batch_size = 8
num_epochs = 3
learning_rate = 1e-5

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased")

# Define optimizer and dataloader
optimizer = AdamW(model.parameters(), lr=learning_rate)
dataset = QADataset("questions_and_answers.csv", tokenizer)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Training loop
for epoch in range(num_epochs):
    model.train()
    for batch in dataloader:
        optimizer.zero_grad()
        inputs = {k: v.to(model.device) for k, v in batch.items()}
        outputs = model(**inputs)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

# Save the trained model
model.save_pretrained("fine_tuned_model")
tokenizer.save_pretrained("fine_tuned_model")
