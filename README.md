# 📊 Data Analysis Projects Portfolio

Welcome to my Data Analysis Projects Portfolio! This repository showcases **5 diverse, real-world data projects** using Python and key data libraries like Pandas, NumPy, Matplotlib, Seaborn, and SciPy.

Each project demonstrates practical data handling, transformation, and visualization — from raw data to meaningful insights. These are beginner-to-intermediate projects, and they reflect tasks similar to what data analysts do in real roles.

---

## 🔧 Technologies Used

- Python 🐍
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Jupyter Notebook / VS Code

---

## 📁 Project List

### 📌 1. Demographic Income Data Analysis
**Dataset**: UCI Adult Census Data  
**Tools**: Pandas  
**Highlights**:
- Cleaned whitespace from categorical columns
- Analyzed race distribution, education levels, and income brackets
- Calculated BMI-based filters
- Country-level income insights
- Real-world application: Used to understand income inequality and workforce demographics

📄 `https://github.com/Zic-09/Data-Analysis/blob/master/demographic_data_analyzer.py`

---

### 📌 2. Matrix Statistics Calculator
**Dataset**: Custom numeric input  
**Tools**: NumPy  
**Highlights**:
- Built a function to compute mean, variance, standard deviation, max, min, and sum
- Output in row-wise, column-wise, and overall formats
- Real-world application: Intro to building analytic functions used in finance, health, and science dashboards

📄 `https://github.com/Zic-09/Data-Analysis/blob/master/mean_var_std.py`

---

### 📌 3. Cardiovascular Health Visualization
**Dataset**: Synthetic medical dataset  
**Tools**: Pandas, Seaborn, Matplotlib  
**Highlights**:
- Created new features like BMI and overweight status
- Normalized cholesterol and glucose levels
- Plotted categorized health indicators against cardiovascular risk
- Generated a heatmap of feature correlations
- Real-world application: Basic data preprocessing and health risk visualization used in healthcare analytics

📄 `https://github.com/Zic-09/Data-Analysis/blob/master/medical_data_visualizer.py`

---

### 📌 4. Sea Level Rise Prediction
**Dataset**: EPA Sea Level Data  
**Tools**: Pandas, Matplotlib, SciPy  
**Highlights**:
- Built two linear regression models (1880–2050 and 2000–2050)
- Visualized climate change trends
- Real-world application: Predictive analysis for climate science and policy planning

📄 `https://github.com/Zic-09/Data-Analysis/blob/master/sea_level_predictor.py`

---

### 📌 5. Time Series Web Traffic Analysis
**Dataset**: freeCodeCamp Forum Pageviews  
**Tools**: Pandas, Seaborn, Matplotlib  
**Highlights**:
- Cleaned outliers (top/bottom 2.5%)
- Generated line, bar, and box plots for page view trends
- Seasonal and yearly traffic trends analyzed
- Real-world application: Useful for web analytics, marketing insights, and trend forecasting

📄 `https://github.com/Zic-09/Data-Analysis/blob/master/time_series_visualizer.py`

---

## 🚀 How to Use

1. Clone the repo:
```bash
git clone https://github.com/Zic-09/Data-Analysis.git

```

---

### 🔍 Insights & Observations

Each project in this repository led to unique and valuable insights derived from real or realistic datasets. Here's a summary of key findings:

---

### 📌 1. Demographic Income Analysis
- **Race Distribution**: The dataset revealed significant disparities in race representation.
- **Education Impact**: Only a small percentage of individuals with Bachelor’s degrees earn above 50K.
- **Advanced Education vs. Income**: Individuals with Bachelors, Masters, or Doctorate degrees were more likely to earn >50K, though the difference was not extreme.
- **Work Hours & Earnings**: Even among those working the minimum weekly hours, a small fraction still earned above 50K.
- **Geographic Insight**: India stood out for having the highest percentage of high earners among its respondents.
- **Occupation Insight**: Tech-related roles (e.g., Prof-specialty) dominated among high earners in India.

---

### 📌 2. Matrix Statistics Calculator
- **Matrix-Wise Statistics**: Explored mean, variance, standard deviation, and other statistics by rows, columns, and total — reinforcing how data distribution shifts depending on orientation.
- **Educational Use**: This project serves as a basic tool to demonstrate the power of NumPy for vectorized computation.

---

### 📌 3. Cardiovascular Health Visualization
- **BMI & Overweight Flagging**: Overweight individuals were clearly flagged using BMI > 25.
- **Cholesterol & Glucose Risk**: Normalizing these values helped simplify risk classification for analysis.
- **Lifestyle Factors**: Categorical plots revealed a correlation between lifestyle habits (smoking, alcohol, activity) and cardiovascular disease.
- **Heatmap Patterns**: Showed strong positive correlation between systolic and diastolic pressure, and weaker correlations among other indicators.

---

### 📌 4. Sea Level Rise Prediction
- **Trend Prediction (1880–2050)**: The sea level has shown a clear long-term rising trend.
- **Recent Acceleration**: Data since the year 2000 indicates a steeper rate of rise, suggesting climate change impact is accelerating.
- **Policy Relevance**: Visualization supports the need for urgent climate action based on historical and projected trends.

---

### 📌 5. Time Series Analysis of Web Traffic
- **Traffic Trend (2016–2019)**: Overall steady growth in forum engagement.
- **Monthly Patterns**: January and October consistently had higher pageviews, suggesting seasonality.
- **Outliers Removed**: Cleaning top and bottom 2.5% helped improve the accuracy of trend analysis.
- **Box Plots**: Revealed rising median pageviews year over year and distinct monthly distributions — helpful for marketing and content planning.

---

These insights showcase how simple code and clean data can uncover powerful stories that help drive smarter decisions.
