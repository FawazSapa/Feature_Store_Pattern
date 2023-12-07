class FeatureStore:
    def __init__(self):
        # Initialize an empty dictionary to store features and their metadata
        self.features = {}

    def add_feature(self, feature_name, data, metadata=None):
        # Add or update a feature in the Feature Store
        if feature_name not in self.features:
            # If the feature doesn't exist, create a new entry
            self.features[feature_name] = {'data': data, 'version': 1, 'metadata': metadata}
        else:
            # If the feature exists, update its data and version
            self.features[feature_name]['data'] = data
            self.features[feature_name]['version'] += 1

    def get_feature(self, feature_name):
        # Get the data of a specific feature from the Feature Store
        if feature_name in self.features:
            return self.features[feature_name]['data']
        else:
            print(f"Feature '{feature_name}' not found in the Feature Store.")
            return None

    def get_feature_version(self, feature_name):
        # Get the version of a specific feature from the Feature Store
        if feature_name in self.features:
            return self.features[feature_name]['version']
        else:
            print(f"Feature '{feature_name}' not found in the Feature Store.")
            return None

    def get_feature_metadata(self, feature_name):
        # Get the metadata of a specific feature from the Feature Store
        if feature_name in self.features:
            return self.features[feature_name]['metadata']
        else:
            print(f"Metadata for Feature '{feature_name}' not found in the Feature Store.")
            return None

    def serve_real_time(self, feature_name, input_data):
        # Simulate real-time serving by using the latest version of the feature
        feature_data = self.get_feature(feature_name)
        if feature_data:
            print(f"Real-time prediction using feature '{feature_name}': {input_data} -> {feature_data}")
            # In a real-world scenario, you would apply a model for prediction here
        else:
            print("Real-time prediction failed.")

    def serve_batch(self, feature_name, input_data):
        # Simulate batch serving by allowing users to specify the version of the feature
        specified_version = input_data.get('version')
        if specified_version is not None:
            feature_data = self.get_feature(feature_name)
            if feature_data and specified_version == self.get_feature_version(feature_name):
                print(f"Batch prediction using feature '{feature_name}' (Version {specified_version}): {feature_data}")
                # In a real-world scenario, you would apply a model for batch prediction here
            else:
                print("Batch prediction failed. Specified version does not match the latest version.")
        else:
            print("Batch prediction failed. Version not specified.")

class Model:
    def __init__(self):
        # Initialize a flag indicating whether the model is trained
        self.trained = False

    def train(self, features):
        # Simulate model training using the loaded features
        # In a real-world scenario, we would replace this with actual model training logic
        print("Training model using the following features:")
        for feature_name, feature_data in features.items():
            print(f"{feature_name}: {feature_data}")

        # Training logic goes here...

        print("Model training complete.")
        self.trained = True

    def predict(self, input_data):
        if not self.trained:
            print("Model not trained. Please train the model first.")
            return None

        # Simulate model prediction
        print("Model prediction Done")

# Example Usage
if __name__ == "__main__":
    # Create a FeatureStore instance
    feature_store = FeatureStore()

    # Add features with metadata
    feature_store.add_feature('age', [25, 30, 35, 40, 45], {'unit': 'years'})
    feature_store.add_feature('income', [50000, 60000, 75000, 90000, 100000], {'currency': 'USD'})

    # Get feature metadata
    age_metadata = feature_store.get_feature_metadata('age')
    income_metadata = feature_store.get_feature_metadata('income')

    print(f"Metadata for 'age': {age_metadata}")
    print(f"Metadata for 'income': {income_metadata}")

    # Simulate real-time serving
    feature_store.serve_real_time('age', input_data=28)

    # Simulate batch serving
    batch_input_data = {'feature_name': 'income', 'version': 1}
    feature_store.serve_batch('income', input_data=batch_input_data)

    # Load features for training the model
    features_for_training = {
        'age': feature_store.get_feature('age'),
        'income': feature_store.get_feature('income')
    }

    # Create a Model instance
    model = Model()

    # Train the model using the loaded features
    model.train(features_for_training)

    # Perform prediction using the trained model
    model.predict(input_data={'new_data_point': 30})
