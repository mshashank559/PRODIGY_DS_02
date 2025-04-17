import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style='whitegrid')

# -----------------------------
# 1. Load the data
# -----------------------------
train = pd.read_csv('Data/train.csv')
test = pd.read_csv('Data/test.csv')

# -----------------------------
# 2. Preview the data
# -----------------------------
print("Train Data Sample:")
print(train.head())

print("\nTrain Data Info:")
print(train.info())

print("\nTrain Missing Values:")
print(train.isnull().sum())

# -----------------------------
# 3. Clean Training Data
# -----------------------------
train['Age'].fillna(train['Age'].median(), inplace=True)
train['Embarked'].fillna(train['Embarked'].mode()[0], inplace=True)
train.drop('Cabin', axis=1, inplace=True)

print("\nTrain Missing Values After Cleaning:")
print(train.isnull().sum())

# -----------------------------
# 4. Clean Test Data
# -----------------------------
test['Age'].fillna(test['Age'].median(), inplace=True)
test['Fare'].fillna(test['Fare'].median(), inplace=True)
test['Embarked'].fillna(test['Embarked'].mode()[0], inplace=True)
if 'Cabin' in test.columns:
    test.drop('Cabin', axis=1, inplace=True)

print("\nTest Missing Values After Cleaning:")
print(test.isnull().sum())

# -----------------------------
# 5. Visualizations
# -----------------------------

# Plot: Survival Count
sns.countplot(x='Survived', data=train)
plt.title('Survival Count')
plt.show()

# Plot: Survival by Gender
sns.countplot(x='Survived', hue='Sex', data=train)
plt.title('Survival by Gender')
plt.show()

# Plot: Survival by Class
sns.countplot(x='Survived', hue='Pclass', data=train)
plt.title('Survival by Passenger Class')
plt.show()

# Plot: Age Distribution
train['Age'].hist(bins=30, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
