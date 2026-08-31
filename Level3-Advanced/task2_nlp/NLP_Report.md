# 💬 NLP Report - Tweet Sentiment Classification

*Level 3, Task 2 - Natural Language Processing | Codveda Data Science Internship*

---

## 📁 Dataset Overview

- 🐦 **732 tweets**, originally labeled with 191 different, highly fragmented sentiment categories
- 🎯 **Simplified to 3 broad categories** using a keyword-based mapping: Positive (346), Neutral (248), Negative (138)
- ⚠️ This mapping is an honest limitation - keyword matching is imperfect, especially for subtle or unusual emotional labels

---

## 🧹 Preprocessing Pipeline

1. Lowercased all text
2. Tokenized into individual words
3. Removed punctuation, numbers, and emojis (kept alphabetic tokens only)
4. Removed English stopwords (e.g. "the," "is," "a")
5. Lemmatized remaining words to their root form

Example: `"Enjoying a beautiful day at the park!"` → `"enjoying beautiful day park"`

---

## 🔢 Feature Extraction (TF-IDF)

Cleaned text was converted into a **732 x 500** numeric matrix using TF-IDF (Term Frequency - Inverse Document Frequency), capturing which words were both common within a specific tweet and rare/distinctive across the dataset as a whole.

---

## 📊 Model Comparison

| Model | Accuracy | Negative Recall | Neutral Recall | Positive Recall |
|---|---|---|---|---|
| Naive Bayes | 61.2% | 0.39 | 0.46 | 0.81 |
| **Logistic Regression** | **62.6%** | 0.39 | 0.50 | 0.81 |

🏆 Logistic Regression performed marginally better overall, with a slight edge in Neutral recall.

---

## 🔍 Key Insight: A Shared Weakness Points to the Data, Not the Model

Both models independently showed the exact same specific weakness: strong recall for Positive tweets (0.81) but weak recall for Negative tweets (0.39). Since two different algorithms hit the identical limitation, this points to **class imbalance** in the training data (Negative had the fewest examples of the three categories) as the root cause, rather than a weakness specific to either model.

---

## 🚀 Recommendations for Next Steps

1. ⚖️ **Address class imbalance** - techniques like oversampling the Negative class, undersampling Positive, or using class-weighted models could improve Negative recall in future iterations.
2. 🏷️ **Refine the label mapping** - a more careful, possibly manual review of the original 191 labels (rather than keyword matching) could produce cleaner, more reliable sentiment categories.
3. 📈 **More training data** - a larger dataset, especially with more Negative examples, would likely improve overall performance across all three categories.

---

## 🛠️ Tools Used
`Python` · `pandas` · `nltk` · `scikit-learn` · `Jupyter Notebook`

---
*📌 This report was generated as part of Level 3, Task 2 (NLP - Text Classification) of the Codveda Data Science Internship.*