# Singapore  Resale Flat Prices Predicting

**Introduction**
The project addresses the challenges in accurately estimating resale flat prices in the competitive Singapore market. The predictive model leverages machine learning algorithms to analyze various factors, providing users with reliable estimates for resale prices.

**Key Technologies and Skills**
- Python
- Numpy
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- Pickle
- Streamlit

**Data Preprocessing**

Data Understanding: Before diving into modeling, it's crucial to gain a deep understanding of your dataset. Start by identifying the types of variables within it, distinguishing between continuous and categorical variables, and examining their distributions. In our dataset.


**Encoding and Data Type Conversion:** To prepare categorical features for modeling, we employ LabelEncoder encoding. This technique transforms categorical values into numerical representations based on their intrinsic nature and their relationship with the target variable. Additionally, it's essential to convert data types to ensure they match the requirements of our modeling process.

**Skewness - Feature Scaling:** Skewness is a common challenge in datasets. Identifying skewness in the data is essential, and appropriate data transformations must be applied to mitigate it. One widely-used method is the log transformation, which is particularly effective in addressing high skewness in continuous variables. This transformation helps achieve a more balanced and normally-distributed dataset, which is often a prerequisite for many machine learning algorithms.

**Outliers Handling:** Outliers can significantly impact model performance. We tackle outliers in our data by using the Interquartile Range (IQR) method. This method involves identifying data points that fall outside the IQR boundaries and then converting them to values that are more in line with the rest of the data. This step aids in producing a more robust and accurate model.

**Exploratory Data Analysis (EDA) and Feature Engineering:**

Skewness Visualization: To enhance data distribution uniformity, we visualize and correct skewness in continuous variables using Seaborn's Histplot and boxplot. By applying the Log Transformation method, we achieve improved balance and normal distribution, while ensuring data integrity.

Outlier Visualization: We identify and rectify outliers by leveraging Seaborn's Boxplot. This straightforward visualization aids in pinpointing outlier-rich features. Our chosen remedy is the Interquartile Range (IQR) method, which brings outlier data points into alignment with the rest of the dataset, bolstering its resilience.

 **Algorithm Selection**: After thorough evaluation, Random Forest Regressor, demonstrate commendable testing accuracy. Upon checking for any overfitting issues in both training and testing, both models exhibit strong performance without overfitting concerns. I choose the Decision Tree Regressor for its ability to strike a balance between interpretability and accuracy, ensuring robust performance on unseen data.

Evaluation and Prediction: Use hyperparameter tuning to choose best parameter to reduce overfitting, then predict the value using unseen data

**Contact**

📧 Email: kobalanm2705@gmail.com 




