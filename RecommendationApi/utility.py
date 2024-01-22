import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Assuming you have a DataFrame with template data
data = {
    'TemplateID': [1, 2, 3, 4, 5],
    'Feature1': [0.2, 0.4, 0.6, 0.8, 1.0],
    'Feature2': [0.1, 0.3, 0.5, 0.7, 0.9],
}

df = pd.DataFrame(data)

# Assuming you have a new template for which you want recommendations
new_template = {
    'Feature1': [0.45],
    'Feature2': [0.55],
}

# Convert the new template into a DataFrame
new_template_df = pd.DataFrame(new_template)

# Extract features from the DataFrame
X = df[['Feature1', 'Feature2']]

# Fit a k-nearest neighbors model
knn = NearestNeighbors(n_neighbors=3, algorithm='auto')
knn.fit(X)

# Find k-nearest neighbors for the new template
distances, indices = knn.kneighbors(new_template_df)

# Create a dictionary to store the recommendations
recommendations = {'template_id': [], 'distance': []}

# Populate the recommendations dictionary
for i in range(len(indices[0])):
    template_id = df.loc[indices[0][i], 'TemplateID']
    distance = distances[0][i]
    recommendations['template_id'].append(template_id)
    recommendations['distance'].append(distance)

# Convert the recommendations dictionary to a DataFrame
recommendations_df = pd.DataFrame(recommendations)

# Convert the DataFrame to a JSON file
json_file_path = 'recommendations.json'
recommendations_df.to_json(json_file_path, orient='records', lines=True)

print(f'Recommendations saved to {json_file_path}')
