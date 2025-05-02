# Pre-process the input

def preprocess(df, featurizer_model):
    try:

        print("Preparing features")
        X = df.drop("credit_risk", axis=1,errors='ignore')
            
        X_test = featurizer_model.transform(X)
        print(f"Features shape after preprocessing: {X_test.shape}")
        
        return X_test
        
    except Exception as e:
        print(f"Exception in processing script: {e}")
        raise e