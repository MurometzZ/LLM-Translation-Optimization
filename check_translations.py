from pathlib import Path
from ollama import Client

client = Client()

source_text_dir = Path("text_parts")
translations_dir = Path("translations")
ratings_dir = Path("ratings")
instructions_file = Path("rating_instructions.txt")


def ask_cloud_llm(prompt, model):
    messages = [
        {'role': 'user', 'content': prompt},
    ]

    response = client.chat(model, messages=messages, stream=False)
    return response['message']['content']


def create_file_with_text(file_path, content):
    ratings_dir.mkdir(exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(content)


def rate(model: str = "gpt-oss:120b-cloud"):
    instructions = instructions_file.read_text(encoding="utf-8")

    for file in source_text_dir.glob("*.txt"):
        translated_file_path = translations_dir / (file.stem + "_translation.txt")

        if translated_file_path.exists():
            original_text = file.read_text(encoding="utf-8")
            translated_text = translated_file_path.read_text(encoding="utf-8")

            rating = ask_cloud_llm(
                instructions
                + "\nHere is the original text:\n" + original_text
                + "\nHere is the translated text:\n" + translated_text,
                model
            )

            new_filepath = ratings_dir / (file.stem + "_rating.txt")
            create_file_with_text(new_filepath, rating)

            # print(f"Rated {file.name}")