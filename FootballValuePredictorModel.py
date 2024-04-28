# Import all needed libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import seaborn as sns


# Reads the CSV and saves it to the footballData variable
footballData = pd.read_csv("footballData.csv")

print("Original Shape of Data: ", footballData.shape)

footballData = footballData.drop_duplicates()

print("Shape of Data with no Duplicates: ", footballData.shape)

# Calculate the relevant mean and standard deviation which is used to calculate any outliers (works similar to z score)
mean = footballData.mean(axis=0)
std = footballData.std(axis=0)

# Creates a new data frame with identical data but removes all outliers more than twice the std from the mean
# Also drops any rows with empty cells
footballDataNoOutliers = footballData[(mean - 3 * std <= footballData) & (footballData <= mean + 3 * std)].dropna()

print("Shape of Data with no duplicates, empty cells or outliers", footballDataNoOutliers.shape)

# Sorts footballDataNoOutliers into x (everything but value), and y (only value). Y being the target variable
x = footballDataNoOutliers.drop("value_eur", axis=1)
y = footballDataNoOutliers["value_eur"]

# Changing this variable changes the seed that is used to train the model, this means a new set of data
randomStateSeed = 1
# Changing this variable changes what % of the data is used for training (0.3 = 30%)
testSize = 0.2

# Creates the data that the models will use. Takes into account the seed variable and test size variable
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=testSize, random_state=randomStateSeed)

# Changing this variable changes the amount of folds/estimators further down in the code (will increase processing time)
NoOfTestSamples = 10

# fits y and x to a random forest classifier for the purpose of identifying feature importance
forest = RandomForestClassifier(n_estimators=NoOfTestSamples, random_state=randomStateSeed)
forest.fit(x_train, y_train)

# Creates a panda series variable which contains every feature sorted in descending order by importance
feature_scores = pd.Series(forest.feature_importances_, index=x_train.columns).sort_values(ascending=False)

# Creates the feature importance bar plot
feature_scores.plot.bar()
plt.show()

# The below way to display data distribution for each feature was taken from the Heart Example Project
fig = plt.figure(figsize=(18, 18))
ax = fig.gca()
footballDataNoOutliers.hist(ax=ax, bins=50)
plt.show()

# Creates a heatmap that shows the correlation in % between every feature
sns.set(style="darkgrid")
plt.rcParams['figure.figsize'] = (15, 15)
sns.heatmap(footballDataNoOutliers.corr(), annot=True)
plt.title('Correlation (%) Between Every Feature')
plt.show()

# Simplifies the model names for later use
rf = RandomForestClassifier()
nb = GaussianNB()
svm = SVC()
knn = KNeighborsClassifier()
dt = DecisionTreeClassifier()

# Creates a list containing the different classifier models
models = [("rf", rf), ("nb", nb), ("svm", svm), ("knn", knn), ("dt", dt)]

# Creating all needed variables
results = []
names = []

# This method of identifying the best model was taken from:
# https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/
for name, model in models:
    kfoldValidator = KFold(n_splits=NoOfTestSamples, shuffle=True, random_state=randomStateSeed)
    CVScore = cross_val_score(model, x_train, y_train, cv=kfoldValidator, scoring="accuracy")
    results.append(CVScore)
    names.append(name)
    msg = "%s: %f: (%f)" % (name, CVScore.mean(), CVScore.std())
    print(msg)
# Using this we know the best model is a Decision Tree Classifier

# Selects Decision Tree Classifier as the best model and the one to use for our predictor
modelToUse = dt
modelToUse.fit(x_train, y_train)
y_prediction = modelToUse.predict(x_test)

# Plots the model comparison
fig = plt.figure()
fig.suptitle('Model Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
