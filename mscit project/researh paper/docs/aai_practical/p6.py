#pip install matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample data points for clustering
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Combine the x and y coordinates into a single dataset
data = list(zip(x, y))

# Elbow method to determine the optimal number of clusters
inertias = []  # List to store inertia values

# Loop over a range of cluster numbers (from 1 to 10)
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)  # Create a KMeans model with 'i' clusters
    kmeans.fit(data)  # Fit the model to the data
    inertias.append(kmeans.inertia_)  # Store the inertia (sum of squared distances)

# Plot the Elbow Method graph to visualize the inertia
plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# Perform KMeans clustering with the chosen number of clusters (2 in this case)
kmeans = KMeans(n_clusters=2)  # Set 2 clusters
kmeans.fit(data)  # Fit the model

# Scatter plot of the data points, colored by cluster labels
plt.scatter(x, y, c=kmeans.labels_)  # Color points by their assigned cluster
plt.title('KMeans Clustering')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.show()
