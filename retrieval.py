# retrieval.py
import faiss
import torch
import os
from models import bert_tokenizer, bert_model, documents

# Create FAISS index
d = bert_model.config.hidden_size
index = faiss.IndexFlatL2(d)

def load_documents_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents

# Embed and index documents
def embed_documents(documents):
    # ... (embedding logic)
    return embeddings

document_embeddings = embed_documents(documents)
for embedding in document_embeddings:
    index.add(embedding)

# Retrieval function
def retrieve(query, k=2):
    # ... (retrieval logic)
    return retrieved_docs