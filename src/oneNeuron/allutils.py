import numpy as np
import pandas as pd
import joblib # FOR SAVING MY MODEL AS A BINARY FILE
import os
import logging

def prepare_data(df):
  """ it is used to prepare dependent and independent features seprately from dataframe

  Args:
      df (pd.DataFrame): This method takes dataframe as input

  Returns:
      [tuple]: This method returns tuples
  """
  logging.info("preparing the data for training")
  X = df.drop("y", axis=1)

  y = df["y"]

  return X, y

def save_model(model, filename):
  """ This Method saves the model with the filename provided and in the mentioned location.

  Args:
      model ([python object]): Model should be a trained Model so that we can dump it.
      filename ([str]): [This is name of the file to save the model]
  """
  logging.info("saving the trained model with filename")
  model_dir = "models"
  os.makedirs(model_dir, exist_ok=True) # ONLY CREATE IF MODEL_DIR DOESN"T EXISTS
  filePath = os.path.join(model_dir, filename) # model/filename
  joblib.dump(model, filePath)
  logging.info(f"saved the trained model at path : {filePath}")