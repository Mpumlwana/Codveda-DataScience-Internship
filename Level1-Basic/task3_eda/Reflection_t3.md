📝 Reflection - Task 3: Exploratory Data Analysis (EDA)
🎯 What I Did

For this task, I explored the cleaned Churn dataset produced in Task 2 (3,333 rows, 70 columns). I worked through all four objectives:

📐 Summary statistics: used .describe() for an overall view, then computed mean, median, variance, and standard deviation individually for "Total day minutes" to confirm our Task 2 standardization worked correctly (mean ≈ 0, std ≈ 1).
📊 Visualizations: built a histogram (Total day minutes - confirmed a clean, symmetric bell-curve shape), a box plot (Customer service calls - visually confirmed the 267 outliers found in Task 2's IQR analysis), and a scatter plot (Total day minutes vs Total day charge - revealed a near-perfect linear relationship).
🔗 Correlation matrix: computed correlations across the 16 core numeric columns, then visualized them as a heatmap using seaborn. Found that no single column strongly predicts Churn, with Customer service calls (0.21) being the strongest individual signal.
📄 Insights report: wrote up a full written report summarizing 5 key findings and 3 recommendations for the modelling tasks in Level 2.
💡 What I Learned
✅ A box plot is literally a visual version of the IQR method used in Task 2 - the box, whiskers, and outlier dots map directly onto Q1, Q3, and the fences calculated by hand.
✅ A box plot shows which values are extreme, but not how many rows share that value - a whole-number column can show far fewer dots than the actual outlier row count.
✅ Correlation values range from -1 to +1, and a value near 0 doesn't mean "no insight" - it can mean the outcome depends on a combination of weaker signals rather than one dominant cause.
✅ Columns that are mathematically derived from each other (like minutes and charge) show near-perfect correlation - this is called multicollinearity, and it's something to watch for before building predictive models.
✅ Findings from earlier tasks connect forward - the correlation between Customer service calls and Churn gave real evidence supporting the decision (made back in Task 2) to keep rather than remove the outliers in that column.
🧗 Challenges I Faced
Initially expected the box plot to show one dot per outlier row, but realized dots represent unique values, not individual rows - this required reasoning through why 267 rows only produced 6 visible dots.
Deciding which columns to include in the correlation matrix, since including all 70 (with 51 one-hot encoded State columns) would have been unreadable - solved by focusing on the 16 core numeric/target columns.
🛠️ Tools Used

Python · pandas · matplotlib · seaborn · Jupyter Notebook

Task 3 of the Codveda Data Science Internship - Level 1 (Basic)