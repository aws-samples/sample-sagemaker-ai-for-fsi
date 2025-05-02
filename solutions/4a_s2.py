# Load featurizer sklearn model from MLFlow model registry

featurizer_model = mlflow.sklearn.load_model(logged_featurizer_model.model_uri)