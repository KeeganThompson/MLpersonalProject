import os
import sys
import numpy as np
import pandas
import dill
from src.exception import CustomException


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

