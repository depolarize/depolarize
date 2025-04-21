from transformers import RobertaForSequenceClassification, RobertaTokenizerFast
from huggingface_hub import create_repo

save_dir = "/Users/vedarth/depolarize/server/political_alignment/political_affiliation_model"

model = RobertaForSequenceClassification.from_pretrained(save_dir, local_files_only=True)
tokenizer = RobertaTokenizerFast.from_pretrained(save_dir, local_files_only=True)

repo_id = "vedarth31/political-alignment-classification"
create_repo(repo_id)

model.push_to_hub(repo_id)
tokenizer.push_to_hub(repo_id)