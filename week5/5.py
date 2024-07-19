import numpy as np

# Assume we have the embedding vector for the word "Celebrate" using "text-embedding-3-small"
# Since the actual embedding is not provided, we'll simulate it with random values for demonstration purposes.
# Replace this with the actual embedding vector if available.
np.random.seed(42)  # For reproducibility
embedding_vector = np.random.rand(1536)  # Simulating a 1536-dimensional embedding vector

# Count how many values are greater than 0.02141835007499513
threshold = 0.02141835007499513
count = np.sum(embedding_vector > threshold)
print(count)
