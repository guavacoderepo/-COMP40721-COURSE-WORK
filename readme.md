# Predicting and Analyzing Developer Compensation: Insights from the Stack Overflow 2024 Developer Survey

## Project Description

This project (coursework) focuses on applying various machine learning (ML) models to analyze and predict developers' annual compensation. The study leverages data from the "Stack Overflow 2024 Annual Developer Survey", which captures information about the annual salaries of developers from diverse countries, industries, skills, and experience levels. 

The primary objectives of this coursework include performing Clustering Analysis (Unsupervised Learning) to group developers based on similar compensation patterns, Classification (Supervised Learning) to categorize developers into high and low-income groups, and Regression Analysis (Supervised Learning) to predict their annual compensation. 

## Tools Used

<p align="center">
  <img src="images/skills/python.png" width="100" height="100">
  <img src="images/skills/pandas.png" width="100" height="100">
  <img src="images/skills/seaborn.png" width="100" height="100">
  <img src="images/skills/matplot.png" width="100" height="100">
  <img src="images/skills/Sklearn.png" width="100" height="100">
</p>

## Data Understanding

The dataset consisting of 113 columns and 65,437 rows, with 13 numerical and 100 categorical columns. 17 columns were selected for analysis, consisting of 16 features and 1 target variable, based on their relevance to developer compensation and domain knowledge.

## Data Preprocessing
In the initial data preparation phase, the following tasks were performed:

1. Data Loading and Inspection
    The dataset was loaded and initially inspected for understanding its structure and key features.

2. Handling Duplicate Values
    Any duplicate rows were identified and removed to ensure the integrity of the data.

3. Handling Missing or Erroneous Values
    Missing or erroneous values were addressed using appropriate strategies, such as imputation or removal, depending on the nature of the data.

4. Outlier Detection and Handling
    Outliers were identified and appropriately handled, either by capping or removing them, to prevent distortion in model performance.

5. Data Formatting and Conversion
    Non-numeric columns were converted into appropriate numeric formats where necessary, ensuring compatibility with machine learning models.