import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

def train_logistic_regression(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def train_random_forest(X_train, y_train, n_estimators=200, random_state=42):
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)
    return model

def save_model(model, path):
    joblib.dump(model, path)

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    results = {
        'accuracy': accuracy_score(y_test, y_pred),
        'report': classification_report(y_test, y_pred, output_dict=True)
    }
    try:
        y_proba = model.predict_proba(X_test)[:,1]
        results['roc_auc'] = roc_auc_score(y_test, y_proba)
    except Exception:
        results['roc_auc'] = None
    return results
