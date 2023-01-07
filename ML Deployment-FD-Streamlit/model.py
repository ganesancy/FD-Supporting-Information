import pandas as pd
import pickle
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
# Load the csv file
df = pd.read_excel("FDCWOA-Final.xlsx")

X_OS = df[['Ge', 'Al', 'OH', 'H2O', 'F', 'OSDA', "B", "Na2O", "Cl", "Temperature", "time", "AR", "Area", "CN", "rpm"]]
Y_OS= df['FDC']
cv = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
for train_index, test_index in cv.split(X_OS, Y_OS):
    X_Train, X_Test= X_OS.iloc[train_index], X_OS.iloc[test_index]
    Y_Train, Y_Test= Y_OS[train_index], Y_OS[test_index]

GB = GradientBoostingClassifier(random_state=1, min_samples_leaf=2, n_estimators=1500, learning_rate=0.01)
gb_model=GB.fit(X_Train, Y_Train)

pickle.dump(gb_model, open("model.pkl", "wb"))