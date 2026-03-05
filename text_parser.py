import nltk
from pathlib import Path
from nltk.tokenize import sent_tokenize

nltk.download("punkt")
nltk.download("punkt_tab")

source_text_dir = Path("text_parts")
source_text_dir.mkdir(exist_ok=True)

def split_text_into_chunks(text, sentences_per_chunk=5, overlap=1):
    sentences = sent_tokenize(text)
    chunks = []
    start = 0

    while start < len(sentences):
        end = start + sentences_per_chunk
        chunk = " ".join(sentences[start:end])
        chunks.append(chunk)
        start += sentences_per_chunk - overlap

    return chunks

def create_file(content, path: Path):
    with path.open("w", encoding="utf-8") as f:
        f.write(content)

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = split_text_into_chunks(text, sentences_per_chunk=5, overlap=1)

for i, chunk in enumerate(chunks):
    create_file(chunk, source_text_dir / f"{i}.txt")
    print(f"--- Chunk {i+1} ---\n{chunk}\n")
