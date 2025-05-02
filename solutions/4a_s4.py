# Load xgboost model from MLFlow model registry
creditrisk_model = mlflow.xgboost.load_model(logged_creditrisk_model.model_uri)