from sagemaker.predictor import Predictor
from sagemaker.serializers import CSVSerializer

# Create predictor
predictor = Predictor(
    endpoint_name = endpoint_name,
    component_name = component_name,
    serializer = CSVSerializer()
)