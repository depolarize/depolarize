# Depolarize

Depolarize is a Chrome extension designed to help readers identify and understand bias in online news articles. Through natural language processing, it provides:

- **Bias Rating**: The emotional intensity of an article compared to its neutral rendition using a VAD (Valence–Arousal–Dominance) dataset.
- **Political Alignment**: Classifies articles as Left, Center, or Right using a fine-tuned RoBERTa model.
  - https://huggingface.co/vedarth31/political-alignment-classification
- **Neutral Summary**: Generates a balanced summary free from framing bias, using both fine-tuned BART and FLAN-T5 models.
  - https://huggingface.co/apend10/bart-finetuned-neutral
  - https://huggingface.co/apend10/flan-t5-neutral

---

## Usage

1. Navigate to any news article or blog post.
2. Click the **Depolarize** icon in the Chrome toolbar.
3. View:
   - **Bias Rating** (0–5 scale): Higher values indicate stronger emotional bias.
   - **Political Alignment**: Left | Center | Right.
   - **Neutral Summary**: An brief and unbiased summary of the events.
4. Optionally, open the **Developer Console** to see model logits and intermediate metrics.

---

## Setup & Installation

### Run Application

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python server/app.py
```

### Set Up Chrome Extension

1. **Clone this repository**
   ```bash
   git clone https://github.com/vedarth31/depolarize.git
   ```
2. **Open Chrome** and navigate to `chrome://extensions/`.
3. **Enable Developer mode** in the top-right corner.
4. **Click "Load unpacked"** and select the `depolarize/extension` folder.
5. **Pin the Depolarize icon** to your toolbar for easy access.

---

## Citations

### Political Alignment
- **Architecture**: RoBERTa-base
- **Dataset**: Political Bias Dataset (Christopher Jones, 2024)
- **Citation**:
  ```bibtex
  @misc{cajcodes_political_bias,
    author = {Christopher Jones},
    title = {Political Bias Dataset: A Synthetic Dataset for Bias Detection and Reduction},
    year = {2024},
    howpublished = {\url{https://huggingface.co/datasets/cajcodes/political-bias}},
  }
  ```

### Neutral Summarization
- **Models**: Fine-tuned BART and FLAN-T5
- **Dataset**: NeuS: Neutral Multi-News Summarization for Mitigating Framing Bias (Lee et al., NAACL 2022)
- **Citation**:
  ```bibtex
  @inproceedings{lee2022neus,
    title={NeuS: Neutral Multi-News Summarization for Mitigating Framing Bias},
    author={Lee, Nayeon and Bang, Yejin and Yu, Tiezheng and Madotto, Andrea and Fung, Pascale},
    journal={Annual Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
    year={2022}
  }
  ```

### Bias (Emotional Intensity)
- **Technique**: Valence–Arousal–Dominance (VAD) analysis
- **Lexicon**: NRC VAD Lexicon
- **Citation**:
  ```bibtex
  @misc{nrc_vad_lexicon,
    author = {Saif M. Mohammad and Peter D. Turney},
    title = {NRC VAD Lexicon},
    year = {2018},
    url = {https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm}
  }
  ```

---
