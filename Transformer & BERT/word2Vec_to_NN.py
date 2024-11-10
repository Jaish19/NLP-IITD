# Importing necessary libraries
import numpy as np
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Sample data (sentences and labels for classification)
sentences = [
    "This is a great product",
    "I love this movie",
    "This is the worst experience",
    "I hated the food",
    "Absolutely fantastic",
    "Horrible and disappointing",
    "I would recommend it to everyone",
    "Never again",
]
labels = ["positive", "positive", "negative", "negative", "positive", "negative", "positive", "negative"]

# Step 1: Preprocess the text data
tokenized_sentences = [sentence.lower().split() for sentence in sentences]

# Step 2: Train Word2Vec model on tokenized sentences
word2vec_model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Function to get sentence embeddings by averaging word embeddings
def get_sentence_embedding(sentence, word2vec_model):
    words = sentence.split()
    word_vectors = [word2vec_model.wv[word] for word in words if word in word2vec_model.wv]
    if len(word_vectors) == 0:
        return np.zeros(word2vec_model.vector_size)
    return np.mean(word_vectors, axis=0)

# Step 3: Create embeddings for each sentence
X = np.array([get_sentence_embedding(sentence, word2vec_model) for sentence in sentences])

# Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)
y = to_categorical(y)  # Convert labels to categorical format for neural network

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Build and train the neural network
model = Sequential([
    Dense(128, activation='relu', input_shape=(100,)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(2, activation='softmax')  # 2 output neurons for binary classification
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=2, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Testing with a sample sentence
sample_sentence = "I enjoy this product"
sample_embedding = get_sentence_embedding(sample_sentence, word2vec_model)
prediction = model.predict(np.array([sample_embedding]))
predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])
print(f"Prediction for '{sample_sentence}': {predicted_label[0]}")
