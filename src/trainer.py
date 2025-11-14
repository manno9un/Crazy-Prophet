import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np
import pickle
import os

DATA_PATH = "data/cleaned/cleaned.txt"
MODEL_PATH = "models/crazy_prophet.keras"
TOKENIZER_PATH = "models/tokenizer.pkl"

SEQ_LEN = 40

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return f.read()

def create_sequences(text, tokenizer):
    sequences = []
    tokens = tokenizer.texts_to_sequences([text])[0]

    for i in range(SEQ_LEN, len(tokens)):
        seq = tokens[i-SEQ_LEN:i+1]
        sequences.append(seq)

    return np.array(sequences)

def build_model(vocab_size):
    model = Sequential([
        Embedding(vocab_size, 128, input_length=SEQ_LEN),
        LSTM(256, return_sequences=True),
        LSTM(256),
        Dense(256, activation="relu"),
        Dense(vocab_size, activation="softmax")
    ])
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam")
    return model

def train():
    text = load_data()

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([text])

    vocab_size = len(tokenizer.word_index) + 1

    sequences = create_sequences(text, tokenizer)

    X = sequences[:, :-1]
    y = sequences[:, -1]

    model = build_model(vocab_size)

    model.fit(X, y, batch_size=128, epochs=30)

    model.save(MODEL_PATH)

    with open(TOKENIZER_PATH, "wb") as f:
        pickle.dump(tokenizer, f)

    print("✔ Training complete. Model saved!")
    

if __name__ == "__main__":
    train()
