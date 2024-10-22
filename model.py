# models.py
from transformers import BertTokenizer, BertModel, T5ForConditionalGeneration, T5Tokenizer

# Load LegalBERT
bert_tokenizer = BertTokenizer.from_pretrained("nlpaueb/legal-bert-base-uncased")
bert_model = BertModel.from_pretrained("nlpaueb/legal-bert-base-uncased")

# Load T5
t5_tokenizer = T5Tokenizer.from_pretrained("t5-base")
t5_model = T5ForConditionalGeneration.from_pretrained("t5-base")