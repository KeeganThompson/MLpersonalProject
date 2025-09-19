import os
import sys
import pickle
from src.exception import CustomException


def save_object(file_path: str, obj) -> None:
	"""Serialize `obj` to `file_path` using pickle.

	Creates parent directories if they don't exist.
	Raises CustomException on failure.
	"""
	try:
		dir_path = os.path.dirname(file_path)
		if dir_path and not os.path.exists(dir_path):
			os.makedirs(dir_path, exist_ok=True)

		with open(file_path, 'wb') as f:
			pickle.dump(obj, f)
	except Exception as e:
		raise CustomException(e, sys)

