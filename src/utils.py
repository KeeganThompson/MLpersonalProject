import os
import sys
import numpy as np
import pandas
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score

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
	
def evaluate_model(X_train, y_train, X_test, y_test, models: dict) -> dict:
    """Train and evaluate multiple models.

    Trains each model in `models` on the training data and evaluates it on the test data.
    Returns a report dictionary with model names as keys and their R^2 scores as values.
    Raises CustomException on failure.
    """
    try:
        report = {}

        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)

