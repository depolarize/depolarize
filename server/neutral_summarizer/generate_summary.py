from transformers import BartTokenizer, BartForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM

def generate_neutral_summary(source, model=1):
    '''
        Generates a neutral summary of the given source text using a pre-trained BART model (model=1) or a pre-trained flan-t5 model (model=2).
        Usage:
        print(generate_neutral_summary("""enter source source""", model=2)) # 1 for bart, 2 for flan-t5
    '''
    if model == 1:
        model_path = "apend10/bart-finetuned-neutral"
        tokenizer = BartTokenizer.from_pretrained(model_path)
        model = BartForConditionalGeneration.from_pretrained(model_path)

        # Prepare input
        input_text = f"Source: {source.strip()}"

        # Tokenize input
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)

        # Generate summary
        summary_ids = model.generate(inputs["input_ids"], max_length=128, min_length=60, do_sample=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary
    else:
        model_path_2 = "apend10/flan-t5-neutral"
        tokenizer = AutoTokenizer.from_pretrained(model_path_2, use_fast=True)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path_2)

        # Prepare input
        input_text = f"Source: {source.strip()}"

        # Tokenize input
        inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)

        # Generate summary
        summary_ids = model.generate(inputs["input_ids"], max_length=128, min_length=60, do_sample=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary