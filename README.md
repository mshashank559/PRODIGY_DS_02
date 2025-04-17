# 🚢 Titanic - Exploratory Data Analysis (EDA)

This project performs "Exploratory Data Analysis (EDA)" on the Titanic dataset using Python. The goal is to understand the data, clean it, and visualize survival trends among passengers.



## 📁 Project Structure

Titanic_EDA_Project/ 
    ├── titanic_eda.py # Python script for data loading, cleaning, and visualization 
    └── Data/
        ├── train.csv # Training data
        ├── test.csv # Testing data
        ├──gender_submission.csv # Sample submission (for future prediction tasks)
    ├── chart/ # (Optional) Folder to save generated charts
    ├── venv/ # Virtual environment


## 📌 Task 2 - Goals

- ✅ Load the dataset (`train.csv` and `test.csv`)
- ✅ Check data types and missing values
- ✅ Clean the data (fill missing values, drop unnecessary columns)
- ✅ Visualize key insights
- ✅ Prepare the dataset for further analysis or model building



## 🧼 Data Cleaning

- Filled missing "Age" with median
- Filled missing "Embarked" with mode
- Dropped the "Cabin" column (too many null values)
- Filled missing "Fare" in test data with median



## 📊 Visualizations

1. Survival Count (0 = Died, 1 = Survived)
2. Survival by Gender
3. Survival by Passenger Class (Pclass)
4. Age Distribution



## 🔍 Key Observations

- Most passengers did "not survive"
- "Females" had a higher survival rate than males
- "1st class passengers" had better chances of survival
- Majority of passengers were aged between "20–40"



## 🛠️ Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn



## 🚀 Next Steps 

- Feature Engineering (create new features like FamilySize)
- Build a machine learning model to predict survival
- Submit predictions using `gender_submission.csv`



## Beginner Friendly

This project is ideal for beginners learning:
- Data analysis
- Python programming
- Working with CSV files
- Data visualization



## Author

Made with by Shashank
Feel free to fork, clone, or explore!


