# 📝 Reflection - Task 2: Data Cleaning and Preprocessing

## 🎯 What I Did
For this task, I worked with the Codveda Churn dataset, which was provided as two separate files (an 80% split and a 20% split of the same data). I combined them into a single dataset of 3,333 customer records and 20 original columns.

Before doing any cleaning, I ran a full investigation of the data:
- 🔍 Checked the shape, column data types, and a preview of the first rows
- ❓ Checked for missing values (found none)
- 🧬 Checked for duplicate rows (found none)
- 📊 Ran a statistical summary to look for potential outliers

I then completed the four core objectives of this task:

- **🧩 Missing data:** confirmed there were none, but documented the standard approaches I would use if there were (dropping rows, filling with mean/median for numeric columns, filling with mode for categorical columns).
- **🚨 Outliers:** used the IQR (Interquartile Range) method to flag unusual values in "Customer service calls" and "Total intl calls." After reasoning through both, I decided to keep them, since they looked like genuine customer behavior rather than data entry errors, and potentially meaningful for understanding churn.
- **🔢 Categorical encoding:** used Label Encoding for binary columns (International plan, Voice mail plan, Churn), and One-Hot Encoding for the State column, since it has many unrelated categories with no natural order.
- **📏 Standardization:** applied StandardScaler to the 16 genuine numeric columns (minutes, calls, charges, account length), so that no column would dominate a future model just because of its raw scale.

The final cleaned dataset has **3,333 rows and 70 columns** (after one-hot encoding expanded the State column into 51 separate columns), and is saved as `churn_cleaned.csv`.

## 💡 What I Learned
- ✅ The importance of investigating a dataset thoroughly before making any changes to it - understanding column types, checking for missing values/duplicates, and reviewing summary statistics first.
- ✅ That statistical outlier detection (like the IQR method) tells you what is *unusual*, but not necessarily what is *wrong* - deciding whether to keep, cap, or remove outliers requires human judgment about the context of the data.
- ✅ The difference between Label Encoding and One-Hot Encoding, and why using Label Encoding on a column like State would have incorrectly implied an order between categories that doesn't exist.
- ✅ The difference between Normalization and Standardization, and why Standardization is generally a better fit when a dataset contains outliers.

## 🧗 Challenges I Faced
- Initially unsure which encoding method to use for which column - resolved this by thinking through whether each column had a natural order (binary columns) or not (State).
- Deciding whether to remove the outliers I found. Rather than automatically deleting them, I reasoned through whether they represented real customer behavior or likely data errors, and concluded they were most likely genuine.

## 🛠️ Tools Used
`Python` · `pandas` · `scikit-learn` (LabelEncoder, StandardScaler) · `Jupyter Notebook`

---
*Task 2 of the Codveda Data Science Internship - Level 1 (Basic)*