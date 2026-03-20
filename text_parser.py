import nltk
from pathlib import Path
from nltk.tokenize import sent_tokenize

nltk.download("punkt", quiet=True)

def split_text_into_chunks(text, sentences_per_chunk=10, overlap=1):
    sentences = sent_tokenize(text)
    chunks = []
    start = 0

    while start < len(sentences):
        end = start + sentences_per_chunk
        chunk = " ".join(sentences[start:end])
        chunks.append(chunk)
        start += sentences_per_chunk - overlap

    return chunks


def parse(input_file_path: str, output_dir: str = "text_parts"):
    input_path = Path(input_file_path)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Read input file
    with input_path.open("r", encoding="utf-8") as f:
        text = f.read()

    # Split into chunks
    chunks = split_text_into_chunks(text)

    # Write chunks to files
    for i, chunk in enumerate(chunks):
        with (output_path / f"{i}.txt").open("w", encoding="utf-8") as f:
            f.write(chunk)

    print(f"Created {len(chunks)} chunks in '{output_path}'")