import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = re.sub(r'[^a-zA-Z\s.,;:!?\'"-]', ' ', text)  # remove special symbols
    text = re.sub(r'\s+', ' ', text).strip()  # normalize spaces
    return text

def clean_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = f.read()

    cleaned = clean_text(data)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    print("Cleaning completed! Saved to:", output_path)
