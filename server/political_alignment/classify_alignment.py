import torch
import torch.nn.functional as F
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification
import os

dir="vedarth31/political-alignment-classification"
tokenizer = RobertaTokenizerFast.from_pretrained(dir)
model = RobertaForSequenceClassification.from_pretrained(dir)
model.eval()

label_names = [
    "highly conservative",
    "somewhat conservative",
    "neutral",
    "somewhat liberal",
    "highly liberal"
]

def classify(texts):
    """
    texts: single string or list of strings
    returns: list of (pred_idx, pred_label, probs) tuples
    """
    if isinstance(texts, str):
        texts = [texts]
        
    enc = tokenizer(
        texts,
        truncation=True,
        padding=True,
        max_length=256,
        return_tensors="pt"
    )
    with torch.no_grad():
        logits = model(**enc).logits
        probs  = F.softmax(logits, dim=-1)

    preds = torch.argmax(probs, dim=-1).tolist()
    probs = probs.tolist()
    
    results = []
    for idx, pr in zip(preds, probs):
        results.append((idx, label_names[idx], pr))
    return label_names[idx]