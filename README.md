# K Means Clustering Implementation


## Overview
K-Means Clustering is an unsupervised learning algorithm that is used to solve the clustering problems in machine learning or data science. K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different clusters. It allows us to cluster the data into different groups and a convenient way to discover the categories of groups in the unlabeled dataset on its own without the need for any training.


## Author
**Sanchai Ahilan** - [LinkedIn](https://www.linkedin.com/in/sanchai-ahilan-j-k-812953222/)


## Working
It is a centroid-based algorithm, where each cluster is associated with a centroid. The main aim of this algorithm is to minimize the sum of distances between the data point and their corresponding clusters.

The algorithm takes the unlabeled dataset as input, divides the dataset into k-number of clusters, and repeats the process until it does not find the best clusters. The value of K should be predetermined in this algorithm.

The K-Means Clustering algorithm mainly performs two tasks:
* Determines the best value for K center points or centroids by an iterative process.
* Assigns each data point to its closest K-center. Those data points which are near to the particular K-center, create a cluster.

Hence each cluster has datapoints with some commonalities, and it is away from other clusters.

The working of the K-Means algorithm is explained in the below steps:

* **Step 1 :** Select the number K to decide the number of clusters.
* **Step 2 :** Select random K points or centroids. (It can be other from the input dataset).
* **Step 3 :** Assign each data point to their closest centroid, which will form the predefined K clusters.
* **Step 4 :** Calculate the variance and place a new centroid of each cluster.
* **Step 5 :** Repeat the third steps, which means reassign each datapoint to the new closest centroid of each cluster.
* **Step 6 :** If any reassignment occurs, then go to step 4, else go to FINISH.
* **Step 7 :** The model is ready.


## Screenshots
![kmeans](https://user-images.githubusercontent.com/89059194/146177460-a409b2c9-9469-4fb0-b5ee-837e409c9ce4.png)


## Dataset
The Dataset used for this project is **vgsales**.
You can download this dataset from [Kaggle](https://www.kaggle.com/kedokedokedo/vgsales).


## Requirements to compile this code
* Python *3.0*
* Pandas
* Numpy
* Matplotlib


## Contributing
Want to work on the project? Any kind of contribution is welcome!

Follow these steps:
* Fork the project.
* Create a new branch.
* Make your changes and write tests when practical.
* Commit your changes to the new branch.
* Send a pull request.
