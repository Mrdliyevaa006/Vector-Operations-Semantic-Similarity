# 💻Vector-Operations-Semantic-Similarity
Word embedding analogy and cosine similarity implemented from scratch and verified with NumPy, demonstrating the classic King - Man + Woman ≈ Queen relationship.
---
This project demonstrates how **word embeddings** can be represented and manipulated as vectors to capture semantic relationships between words.

### 🔹 Why Word Vectors?

In Natural Language Processing (NLP), words are often represented as high-dimensional vectors called **embeddings**. These embeddings capture semantic meaning: words with similar contexts have vectors that are close to each other. By representing words as vectors, we can perform mathematical operations on them to uncover linguistic patterns.

For example, the famous analogy:
**King - Man + Woman ≈ Queen**
shows that vector arithmetic can capture gender and role relationships.

### 🔹 What This Code Does

1. **From Scratch Implementation**

   * Vector addition and subtraction functions to compute analogies.
   * Dot product and norm functions to calculate **cosine similarity**.
   * Analogy computed: `v_king - v_man + v_woman`.
   * Cosine similarity used to compare the result with `v_queen`.

2. **NumPy Verification**

   * The same operations are repeated with **NumPy** (`np.array`, `np.dot`, `np.linalg.norm`) to verify correctness.

### 🔹 Results

* Analogy result (from scratch & NumPy): **\[0.9, 0.55, 0.2]**
* Cosine similarity with `Queen`: **≈ 1.0** (almost perfect match).

### 🔹 Why It Matters

This small project illustrates how **vector arithmetic in word embeddings** can capture meaningful linguistic relationships, and how **cosine similarity** can measure closeness between word meanings. It serves as an educational example for understanding the foundation of modern NLP techniques like **Word2Vec**, **GloVe**, and **transformer-based models**.

