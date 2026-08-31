# 📝 Reflection - Level 3, Task 2: NLP - Text Classification

## 🎯 What I Did
For this task, I worked with a sentiment-labeled tweet dataset to classify text as Positive, Negative, or Neutral. Before any processing, an investigation revealed the dataset actually contained 191 different sentiment labels (e.g. "Joy," "Grief," "Runway Creativity"), far too fragmented for reliable classification with only 732 total rows. I built a keyword-based mapping to simplify these into 3 broad categories, checking and expanding the keyword lists after finding several clearly positive/negative labels had been mis-bucketed into "Neutral" on the first attempt.

I then completed all 4 objectives:

- 🧹 **Preprocessing:** used nltk to lowercase, tokenize, remove stopwords, and lemmatize the tweet text, reducing each tweet to its core meaningful words.
- 🔢 **TF-IDF:** converted the cleaned text into a 732 x 500 numeric matrix using TfidfVectorizer, capturing which words were both frequent in a given tweet and distinctive across the dataset.
- 🤖 **Model training:** trained both Naive Bayes and Logistic Regression classifiers on the TF-IDF features.
- 📏 **Evaluation:** calculated accuracy, precision, recall, and F1-score for both models. Naive Bayes reached 61.2% accuracy, Logistic Regression reached 62.6%. Both models showed the same specific weakness: strong recall for Positive tweets (0.81) but weak recall for Negative tweets (0.39 in both models).

## 💡 What I Learned
- ✅ Always check unique() on a target/label column before assuming it's already clean - a "sentiment" column can hide 191 inconsistent labels instead of the expected 3, and this must be resolved before modelling can proceed meaningfully.
- ✅ A first-pass keyword mapping should be sanity-checked, not trusted blindly - checking which original labels ended up in "Neutral" revealed several genuinely positive/negative labels that had been missed, and expanding the keyword lists meaningfully rebalanced the categories.
- ✅ Tokenization, stopword removal, and lemmatization are all different, complementary preprocessing steps - breaking text into words, removing common filler words that carry little sentiment meaning, and reducing words to their root form.
- ✅ TF-IDF rewards words that are frequent within a specific piece of text but rare across the whole dataset, since those words tend to be the most distinctive and meaningful for that particular text.
- ✅ When two different types of models (Naive Bayes and Logistic Regression) show the exact same specific weakness, the issue is more likely to be with the data (in this case, class imbalance - Negative had far fewer examples than Positive) than with either individual model choice.
- ✅ Text classification is inherently harder than structured numeric classification (like the iris flowers task) - human language is ambiguous, and our own imperfect label simplification added an extra layer of noise on top of that.

## 🧗 Challenges I Faced
- Discovering 191 sentiment labels instead of the expected 3 required pausing to investigate rather than assuming the "Sentiment" column was ready to use as-is.
- The first version of the keyword-based label mapping incorrectly bucketed many genuinely positive/negative labels into "Neutral" - resolved by explicitly checking which labels landed there and expanding the keyword lists.
- Both trained models struggled specifically with Negative tweet recall (0.39), traced back to Negative having the fewest training examples of the three categories (class imbalance), a limitation that could not be fully resolved within this task.

## 🛠️ Tools Used
`Python` · `pandas` · `nltk` (tokenization, stopwords, lemmatization) · `scikit-learn` (TfidfVectorizer, MultinomialNB, LogisticRegression, metrics) · `Jupyter Notebook`

---
*Level 3, Task 2 of the Codveda Data Science Internship - Advanced*