import re

'''
Usage:
text_a = "CHARLOTTE, N.C. — The closely-watched special U.S. House election being held here Tuesday is taking place in the shadow of a political scandal that, according to the candidates, is having a real impact on the race. But this time around, the issue is not the illegal ballot harvesting that marred last year's contest, it's the fact the one of the candidates has been effectively running for over two years. Democratic candidate Dan McCready likes to tell his supporters that he began running for the 9th Congressional District seat when his..."
text_b = "A special election in North Carolina's 9th congressional district on Tuesday is essentially a do-over after a candidate's 2018 victory was negated by allegations of illegal ballot harvesting. The election could flip a longtime Republican district, and has shifted national attention to the issue of ballot harvesting, the arguments in favor of and against it, and how different states regulate the practice."

result = compare_texts(text_a, text_b, vad_dict)
print_comparison_results(result)
'''
def load_VAD_lexicons():
    VAD_path = '/Users/apendela10/CSCE489/project/nlp_backend/data_gen/VAD/NRC-VAD-Lexicon.txt'
    with open(VAD_path, 'r') as infile:
        lines = infile.read().split("\n")
        
        vad_dict = {}
        for l in lines:
            if not l.strip():  # skip empty lines
                continue
            lexicon, v_score, a_score, d_score = l.split("\t")
            vad_dict[lexicon] = {
                'v': float(v_score),
                'a': float(a_score),
                'd': float(d_score)
            }
        return vad_dict

vad_dict = load_VAD_lexicons()

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def filter_emotional_tokens(tokens, vad_dict):
    filtered = []
    for t in tokens:
        if t in vad_dict:
            v = vad_dict[t]['v']
            if v > 0.65 or v < 0.35:
                filtered.append(t)
    return filtered

def compute_bias_metrics(tokens, vad_dict):
    pos_arousal, neg_arousal = 0, 0
    pos_tokens, neg_tokens = [], []

    for t in tokens:
        if t in vad_dict:
            v = vad_dict[t]['v']
            a = vad_dict[t]['a']
            if v > 0.65:
                pos_arousal += a
                pos_tokens.append(t)
            elif v < 0.35:
                neg_arousal += a
                neg_tokens.append(t)

    total_tokens = len(pos_tokens) + len(neg_tokens)
    avg_arousal = (pos_arousal + neg_arousal) / total_tokens if total_tokens > 0 else 0

    return {
        "Arousal+": pos_arousal,
        "Arousal-": neg_arousal,
        "Arousal_sum": pos_arousal + neg_arousal,
        "Avg Arousal per Token": avg_arousal,
        "Positive Tokens": pos_tokens,
        "Negative Tokens": neg_tokens
    }

def compare_texts(text_a, text_b, vad_dict):
    tokens_a = set(tokenize(text_a))
    tokens_b = set(tokenize(text_b))

    unique_a = tokens_a - tokens_b
    unique_b = tokens_b - tokens_a

    emo_a = filter_emotional_tokens(unique_a, vad_dict)
    emo_b = filter_emotional_tokens(unique_b, vad_dict)

    metrics_a = compute_bias_metrics(emo_a, vad_dict)
    metrics_b = compute_bias_metrics(emo_b, vad_dict)

    return {
        "Original": metrics_a,
        "Neutral Summary": metrics_b,
        "Delta Arousal_sum": metrics_a["Arousal_sum"] - metrics_b["Arousal_sum"],
        "Delta Avg Arousal": metrics_a["Avg Arousal per Token"] - metrics_b["Avg Arousal per Token"]
    }

def interpret_delta(delta):
    if abs(delta) < 0.5:
        return "Minimal emotional difference."
    elif abs(delta) < 1.5:
        return "Moderate emotional difference."
    else:
        return "Significant emotional difference."

def print_comparison_results(result):
    def format_tokens(tokens):
        return ", ".join(tokens) if tokens else "None"

    # print("=== Original Metrics ===")
    # print(f"Arousal+       : {result['Original']['Arousal+']:.3f}")
    # print(f"Arousal-       : {result['Original']['Arousal-']:.3f}")
    # print(f"Arousal Total  : {result['Original']['Arousal_sum']:.3f}")
    # print(f"Avg Arousal/Token: {result['Original']['Avg Arousal per Token']:.3f}")
    # print(f"Positive Tokens: {format_tokens(result['Original']['Positive Tokens'])}")
    # print(f"Negative Tokens: {format_tokens(result['Original']['Negative Tokens'])}")
    # print()

    # print("=== Neutral Summary Metrics ===")
    # print(f"Arousal+       : {result['Neutral Summary']['Arousal+']:.3f}")
    # print(f"Arousal-       : {result['Neutral Summary']['Arousal-']:.3f}")
    # print(f"Arousal Total  : {result['Neutral Summary']['Arousal_sum']:.3f}")
    # print(f"Avg Arousal/Token: {result['Neutral Summary']['Avg Arousal per Token']:.3f}")
    # print(f"Positive Tokens: {format_tokens(result['Neutral Summary']['Positive Tokens'])}")
    # print(f"Negative Tokens: {format_tokens(result['Neutral Summary']['Negative Tokens'])}")
    # print()

    delta = result['Delta Arousal_sum']
    # print("=== Comparative Result ===")
    if delta > 0:
        return (f"Original shows higher emotional intensity (+{delta:.3f}) compared to Neutral Summary. \n Interpretation: {interpret_delta(delta)}")
    
    elif delta < 0:
        return (f"Neutral Summary shows higher emotional intensity (+{abs(delta):.3f}) compared to Original. \n Interpretation: {interpret_delta(delta)}")
    else:
        return (f"Both texts have equal emotional intensity. \n Interpretation: {interpret_delta(delta)}")