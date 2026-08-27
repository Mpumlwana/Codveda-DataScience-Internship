# 📝 Reflection - Level 2, Task 3: Clustering (Unsupervised Learning)

## 🎯 What I Did
For this task, I applied K-Means clustering to the cleaned Churn dataset to explore customer segmentation - my first unsupervised learning task, with no target/answer column to guide the model.

- 🎯 **Column selection:** deliberately excluded Churn (the known outcome) and the 51 one-hot encoded State columns (geography, not behaviour) from clustering, focusing instead on 15 behavioural/usage columns (minutes, calls, charges, account length, customer service calls).
- 🔢 **K-Means clustering:** ran an initial test with K=3, then properly determined the optimal K using both the elbow method (inertia across K=2 to K=10) and silhouette scores. Both methods pointed to K=2, though with notably weak silhouette scores (~0.08 at best, far below the ~0.5 threshold for genuinely strong clustering).
- 🖼️ **PCA visualization:** reduced the 15 columns down to 2 dimensions using PCA (capturing only ~27% of total variance) and plotted the two clusters. The chart showed a heavily overlapping cloud rather than two distinct groups, visually confirming the weak silhouette scores.
- 🔍 **Interpretation:** compared average behaviour between the two clusters and found a clear, interpretable pattern - Cluster 1 customers use more day/evening minutes and less at night, while Cluster 0 customers show the reverse. Other columns (account length, voicemail, international usage, customer service calls) showed little difference between clusters.

## 💡 What I Learned
- ✅ Unsupervised learning is fundamentally different from the supervised tasks I've done so far - there's no "correct answer" column, so the model has to find structure on its own, and evaluating quality requires different tools (elbow method, silhouette score) rather than accuracy/precision/recall.
- ✅ Not every dataset has strong, naturally separated clusters - real customer behaviour data often exists on a continuous spectrum rather than in clean groups, and honestly reporting weak separation is itself a valid, useful finding rather than a failure.
- ✅ The elbow method and silhouette score can (and should) be used together - the elbow chart here didn't show a clean, obvious bend, but the silhouette score gave a clearer, more decisive signal pointing to K=2.
- ✅ PCA is a way to flatten many columns down to 2 dimensions for visualization, but it comes with a real cost - our 2D chart only captured about 27% of the original data's variation, so it should be interpreted as a rough approximation, not the full picture.
- ✅ Even weak/overlapping clusters can still reveal a real, interpretable behavioural pattern (day/evening vs night usage timing) - statistical separation strength and practical interpretability are two different things worth reporting separately.

## 🧗 Challenges I Faced
- Deciding which of the 70 available columns to actually cluster on - resolved by reasoning through which columns represented genuine customer behaviour versus geography or the outcome we might want to compare against later.
- The elbow chart didn't show a clear, textbook "elbow" bend, which made choosing K harder from that method alone - resolved by bringing in the silhouette score as a second, independent check.

## 🛠️ Tools Used
`Python` · `pandas` · `scikit-learn` (KMeans, PCA, silhouette_score) · `matplotlib` · `Jupyter Notebook`

---
*Level 2, Task 3 of the Codveda Data Science Internship - Intermediate*