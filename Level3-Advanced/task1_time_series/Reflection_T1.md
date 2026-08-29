# 📝 Reflection - Level 3, Task 1: Time Series Analysis

## 🎯 What I Did
For this task, I first tried to download real stock price data from Stooq using Python's requests library, the same web-scraping approach from Task 1. This failed, and investigating why revealed that Stooq now requires an API key obtained through an on-site CAPTCHA (as of early 2026), which cannot be automated. I chose to generate a realistic synthetic daily sales dataset instead, deliberately built from three known ingredients (trend, yearly seasonality, and random noise) using numpy, giving me full control and a known "ground truth" to check my analysis against.

I completed all 4 objectives:

- 📊 **Decomposition:** used statsmodels' seasonal_decompose (additive model, period=365) to split the data into trend, seasonal, and residual components. All three extracted components closely matched the exact ingredients I had built into the synthetic data.
- 📉 **Smoothing:** implemented both a 30-day moving average and exponential smoothing (span=30). Both closely tracked the true underlying pattern; they looked nearly identical in this case since the data had no sudden shocks for the two methods to react differently to.
- 🔮 **SARIMA forecasting:** built a SARIMA model to forecast future sales. Initially attempted this on daily data with a 365-day seasonal period, which proved computationally impractical and had to be interrupted. Resolved by resampling to weekly data (reducing the seasonal period to 52), which trained successfully in a reasonable time.
- 📏 **Evaluation:** calculated RMSE = 2.93 on a 26-week held-out test set, and visualized the forecast against actual values, showing a close match.

## 💡 What I Learned
- ✅ Free data sources can add access restrictions over time (like CAPTCHAs), and a failed scraping attempt isn't necessarily a coding mistake, it can be a sign the source itself has changed.
- ✅ Building a synthetic dataset with known components is a legitimate and useful way to learn a new technique, since it lets you verify a tool's output against a known "ground truth" you built yourself.
- ✅ Time series decomposition (trend, seasonal, residual) can accurately reverse-engineer the true components of a series, without being told what those components are, only the expected cycle length.
- ✅ SARIMA's seasonal period has a huge impact on computational cost. A daily dataset with a 365-day seasonal period can become computationally impractical, while resampling to a lower frequency (weekly, with a 52-period season) makes the same real-world pattern far more tractable.
- ✅ Statistical warnings (like "too few observations to estimate seasonal parameters") should be taken seriously and reported honestly, but don't necessarily mean the model's results are unusable, in this case, the forecast still performed well despite the warning.
- ✅ Time series train/test splits must be taken from the end of the data in chronological order, unlike our earlier tasks where splits were randomly shuffled, since order and recency genuinely matter for forecasting.

## 🧗 Challenges I Faced
- The initial SARIMA model (daily data, 365-day season) appeared to hang indefinitely, requiring the kernel to be interrupted. Resolved by resampling to weekly data to reduce computational load.
- Received an EstimationWarning about insufficient observations for the seasonal component, given only about 2.5 years of training data for a 52-week season. Documented this honestly as a real limitation rather than ignoring it.

## 🛠️ Tools Used
`Python` · `pandas` · `numpy` · `statsmodels` (seasonal_decompose, SARIMAX) · `scikit-learn` (RMSE) · `matplotlib` · `Jupyter Notebook`

---
*Level 3, Task 1 of the Codveda Data Science Internship - Advanced*