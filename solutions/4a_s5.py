# Run predictions on the pre-processed payload

predictions = creditrisk_model.predict(xgboost.DMatrix(payload_input))
predictions