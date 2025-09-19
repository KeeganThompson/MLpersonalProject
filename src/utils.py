import os
import sys
import numpy as np
import pandas
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path: str, obj) -> None:
	"""Serialize `obj` to `file_path` using pickle.

	Creates parent directories if they don't exist.
	Raises CustomException on failure.
	"""
	try:
		dir_path = os.path.dirname(file_path)
		os.makedirs(dir_path, exist_ok=True)

		with open(file_path, 'wb') as file_obj:
			dill.dump(obj, file_obj)
	except Exception as e:
		raise CustomException(e, sys)
	
def evaluate_model(X_train, y_train, X_test, y_test, models, param):
    """Train and evaluate multiple models.

    Trains each model in `models` on the training data and evaluates it on the test data.
    Returns a report dictionary with model names as keys and their R^2 scores as values.
    Raises CustomException on failure.
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path: str):
    """Deserialize `obj` from `file_path` using pickle.
    
    Raises CustomException on failure.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)

