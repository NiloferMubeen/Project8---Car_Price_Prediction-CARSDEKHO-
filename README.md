# CARDEKHO Used Car Price Prediction
The main objective of this project is to build a data science model to accuratelt predict the used car prices by analyzing the features like model, age of car, kms_driven, mileage, engine displacement etc.
# Tools Used
1. Python
2. Pandas, Numpy
3. Matplotlit, Seaborn
4. Power BI
5. Scikit learn (Regression Algorithms, Label Encoder)
6. Streamlit
# Data Preprocessing
* The data collected from the cardekho website in the form of dictionaries is preprocessed and the relevant features were collected from the data set.
* The dataset was checked for nulls and duplicates. The duplicates were dropped and null values were replaced with the correct values by analysing the dataset.
* Features like mileage, engine displacement, kms driven were formatted to numercial columns
# Exploratory Data Analysis 
* Visualizations using Matplotlib and Seaborn were used to further understand the data and some insights were derived
* The following dashboards were built with PowerBI
  
  ![image](https://github.com/NiloferMubeen/Project8---Car_Price_Prediction-CARSDEKHO-/assets/143819770/c9594783-3072-4c6a-9fc8-23db967a9e26)

  
  ![image](https://github.com/NiloferMubeen/Project8---Car_Price_Prediction-CARSDEKHO-/assets/143819770/45ad6809-3b1d-4f5d-88fb-8e11bc7e6bda)
# Label Encoding
Label Encoding was used to encode all the categorical columns and the final dataset was saved as a csv file.
# Treating Skewness and Outliers
* Most of the features were positively skewed. Hence the Cuberoot transformation was used to fix the skewness in Data.
* The IQR method was used to fix the outliers in the data
### Skewness before and after Transformation
![image](https://github.com/NiloferMubeen/Project8---Car_Price_Prediction-CARSDEKHO-/assets/143819770/8ee51c79-23e4-4ca1-9e0a-c60a453a407e)

![image](https://github.com/NiloferMubeen/Project8---Car_Price_Prediction-CARSDEKHO-/assets/143819770/5903e096-dca1-45e2-854e-492e16f9f729)

### Before and After the treat emnt of Outliers
![image](https://github.com/NiloferMubeen/Project8---Car_Price_Prediction-CARSDEKHO-/assets/143819770/224ee59f-691c-4ecb-9c1a-eaff07a9644c)

![image](https://github.com/NiloferMubeen/Project8---Car_Price_Prediction-CARSDEKHO-/assets/143819770/4a2f802b-e29a-4fc9-92b8-d274de0fc7f5)

# Feature Importance
The Extra Trees Regressor is used to find the important features in the dataset
### Train Test Split
The data is then split with 20% allocated for testing data that will be used to evaluate the final model’s performance after model selection and the rest of the data 80% us allocated for training data that is used to evaluate model performance during training.
### Model Selection
In this project, the target variable , price, is a continuous variable. Hence 5 different ML regression algorithms were used for building.
> Linear Regression
> Decision Trees
> Extra Trees 
> Random Forest
> XGBoost

By comparing the model's performances, the Random Forest regressionmodel was selected as the ideal model. 
# Model Performances
![image](https://github.com/NiloferMubeen/Project8---Car_Price_Prediction-CARSDEKHO-/assets/143819770/fb9a036d-ba6a-4853-ba2e-4531766947ab)

# HyperParameter Tuning
Comparitively the Random Forest Model gave a better R2 score. Hence after HyperParameter tuning the model using the Random Search CV, the model's r2 score increased and the MSE decreased to some extent. The model was then saved as a pickle file and was deployed using Streamlit Apllication to predict the Prices.
  
