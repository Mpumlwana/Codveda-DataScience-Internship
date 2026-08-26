# 📝 Reflection - Level 2, Task 2: Classification

## 🎯 What I Did
For this task, I worked with the Iris flower dataset (150 rows, 4 measurements, 3 species) to classify flowers by species. After the usual investigation, I found and removed 3 exact duplicate rows (147 rows remaining) - reasoning that, unlike the churn outliers in Task 2, duplicates here posed a real risk of letting the model "cheat" by seeing identical rows in both training and testing.

I then completed all 4 objectives:

- 🧩 **Preprocessing:** Label encoded the "species" target column (setosa=0, versicolor=1, virginica=2) - reasoning that Label Encoding was appropriate here specifically because species is the target, not an input feature, so there was no risk of introducing a fake ranking between categories. Standardized the 4 numeric measurement columns using StandardScaler.
- 📈 **Logistic Regression:** trained and evaluated the model - Accuracy = 96.7%.
- 📊 **Evaluation metrics:** calculated precision, recall, and a full per-species classification report. Also built a one-vs-rest ROC curve for all 3 species, with AUC scores of 1.00 (setosa), 0.99 (versicolor), and 0.99 (virginica).
- ⚖️ **Model comparison:** compared Logistic Regression (96.7%) against Random Forest (93.3%) and SVM (93.3%) - Logistic Regression performed best.

## 💡 What I Learned
- ✅ Whether to remove duplicate rows depends on context - in Task 2 I kept statistical outliers because they represented real customer behaviour, but here I removed duplicate rows because they risked letting the model be evaluated on data it had effectively already seen.
- ✅ Label Encoding is appropriate for a *target* column even with 3+ categories, since the model treats the numbers as labels, not as a meaningful order - the risk of "fake ranking" mainly applies to *input features*, like State was in the churn dataset.
- ✅ Precision and recall can conflict, and reading them per-category revealed a specific overlap: the model's only mistake likely confused one real versicolor flower for virginica - which lines up with these two species being known to look more visually similar to each other than to setosa.
- ✅ ROC curves are naturally built for 2-category problems, so a "one-vs-rest" approach (treating each category as its own yes/no question) is used to adapt them for a multi-class problem like this one.
- ✅ More complex models (Random Forest, SVM) are not automatically better - on this small, cleanly-separated dataset, the simpler Logistic Regression model actually outperformed both.

## 🧗 Challenges I Faced
- Deciding whether to remove the 3 duplicate rows required different reasoning than our Task 2 outlier decision - concluded that duplicates specifically risk contaminating a train/test split, which is a different kind of problem than an unusual-but-real value.
- Got a FutureWarning when using `SVC(probability=True)` - confirmed it was just a heads-up about a future scikit-learn version change, not an actual error, since the model still trained and predicted correctly.

## 🛠️ Tools Used
`Python` · `pandas` · `scikit-learn` (LogisticRegression, RandomForestClassifier, SVC, LabelEncoder, StandardScaler, train_test_split, metrics) · `matplotlib` · `Jupyter Notebook`

---
*Level 2, Task 2 of the Codveda Data Science Internship - Intermediate*