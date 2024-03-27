import joblib

def predict(data):
    clf = joblib.load("rfclass.sav")
    return clf.predict(data)

def predict_regg(data):
    regg_rf_classifier = joblib.load("regg_rf_model.sav")
    return regg_rf_classifier.predict(data)