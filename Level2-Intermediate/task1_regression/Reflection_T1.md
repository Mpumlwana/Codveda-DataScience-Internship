# 📝 Reflection - Level 2, Task 1: Predictive Modeling (Regression)

## 🎯 What I Did
For this task, I worked with the Boston Housing dataset (506 houses, 13 features) to predict median house prices (MEDV). Before any modelling, I had to fix a data-loading issue: the file had no header row and was actually space-separated rather than comma-separated, despite the .csv extension - I fixed this using `header=None`, `names=[...]`, and `sep=r"\s+"`.

After confirming the dataset had 0 missing values and 0 duplicates, I completed all 4 objectives:

- 🔀 **Train/test split:** split the data into 404 training rows (80%) and 102 testing rows (20%) using `train_test_split`, with `random_state=42` for reproducibility.
- 📈 **Linear Regression:** trained a baseline model - R² = 0.669, RMSE ≈ $4,929.
- 🌳 **Decision Tree:** trained a more flexible model - R² improved to 0.757, RMSE dropped to ≈ $4,221.
- 🌲 **Random Forest:** trained an ensemble of 100 trees - best result by far, R² = 0.893, RMSE ≈ $2,807.
- 📊 **Visualization:** plotted actual vs predicted prices for the Random Forest model, confirming strong overall accuracy with some underperformance at the price extremes (very cheap and very expensive homes).

## 💡 What I Learned
- ✅ A `.csv` file extension doesn't guarantee comma-separated data - always inspect the raw content before trusting the file format.
- ✅ Why we split data into training and testing sets: training on and testing on the same data risks the model "memorizing" rather than genuinely learning general patterns.
- ✅ MSE punishes large errors more than small ones (because errors are squared), while RMSE converts that back into the original units, making it far easier to explain to a non-technical audience.
- ✅ R² measures the percentage of the pattern in the target variable that the model can explain - 0 means no better than guessing the average, 1 means a perfect fit.
- ✅ More flexible models (Decision Tree, Random Forest) captured the housing price pattern noticeably better than a straight-line Linear Regression model, suggesting the real relationship between features and price isn't purely linear.
- ✅ Random Forest builds many different Decision Trees and averages their predictions, which smooths out the instability of any single tree - this is why it consistently outperformed both other models here.
- ✅ Tree-based models tend to underperform at the extremes of a target variable's range, since there are fewer training examples to learn from at those extremes.

## 🧗 Challenges I Faced
- The dataset initially loaded completely incorrectly (all values crammed into one column) because the file used spaces instead of commas - diagnosed by inspecting the raw output rather than assuming the load had worked.
- Got a `NameError: name 'plt' is not defined` when trying to visualize results, because matplotlib hadn't been imported yet in this new notebook - a good reminder that imports don't carry over between separate notebooks.

## 🛠️ Tools Used
`Python` · `pandas` · `scikit-learn` (LinearRegression, DecisionTreeRegressor, RandomForestRegressor, train_test_split, metrics) · `matplotlib` · `Jupyter Notebook`

---
*Level 2, Task 1 of the Codveda Data Science Internship - Intermediate*