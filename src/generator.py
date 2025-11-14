import pickle
import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = "models/crazy_prophet.keras"
TOKENIZER_PATH = "models/tokenizer.pkl"

SEQ_LEN = 40

model = load_model(MODEL_PATH)

with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

word_index = tokenizer.word_index
index_word = {v:k for k,v in word_index.items()}

def generate(seed, length=40, temperature=1.0):
    result = seed.split()

    for _ in range(length):
        encoded = tokenizer.texts_to_sequences([" ".join(result)])[0]
        encoded = encoded[-SEQ_LEN:]
        encoded = np.pad(encoded, (SEQ_LEN - len(encoded), 0))

        pred = model.predict(encoded[np.newaxis], verbose=0)[0]

        # temperature sampling
        pred = np.log(pred + 1e-8) / temperature
        pred = np.exp(pred) / np.sum(np.exp(pred))

        next_word = np.random.choice(len(pred), p=pred)

        result.append(index_word.get(next_word, ""))

    return " ".join(result)

if __name__ == "__main__":
    print(generate("I see that you", 20, 0.9))
