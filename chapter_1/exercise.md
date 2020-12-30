### 1.How Would You Define Machine Learning?

Machine Learning is a subfield of computer science where is in charge to programm computers with the main reason to allow them learn from a collection of data. Whereas in the core, machine learning is the algorithmic implementation of statistical learning theory.

### 2.Can you name four types of problems where it shines?

- Digit recognition
- Spam email detection
- Speech recognition
- Face Recognition

### 3.What is a labeled training set?

A labeled training is a subset of the total collection of data where each instance or observation (feature vector, $x$) has its corresponding true answer (label, $y$).

### 4.What are the two most common supervised tasks?

- Classification
- Regression

### 5.Can you name four common unsupervised tasks?

- Dimensionality Reduction: It has the main purpose to reduce the amount of features merging those that are strong correlated with each other. To make a single new feature and improving the memory use, computational speed, and also may perform better predicting.
    - ![cc6148baf4edc37a4d2c65b55f2e4e79.png](_resources/3b25e8c68db4421bba7343bcbc28fe37)
- Cluestering: This group of algorithms seeks to find patterns or similarities between observations in order to segmentize them withouth the need of a labeled dataset.
- Association Rule Learning: The goal is to dig in a large amount of data to discover correlation between attributes.
    - ![fc85d30a265773f46257568f034b326c.png](_resources/0a657f27b8f1499697ea1da31403ce7e)
- Anomaly Detection: The goal of this task is to find instances that are out from the normal behavior of the training set.

### 6.What type of Machine Learning algorithm would you use to allow a robot to walk in various unknown terrains?

A reinforcement learning algorithm, because the environment is something unknown and also it is stochastic due to the fact that are "various unknown" terrains. Therefore the nature of the problem itself apperantly tends that the robot have to make desicions by its own on a terrain that must learn.

### 7.What type of algorithm would you use to segment your customers into multiple groups?

If I know what the multiple groups are, and I count with the enough labeled collection of data to classify them. I will go with Multiple Discriminant Analysis (MDA) or Support Vector Machines (SVM) algorithms.  
If the learning problem turns out to be unsupervised. I will go first with an Association Rule to know what attributes are more correlated with each other, to then with Dimensionality Reduction make a feature extraction, if it is possible. Then use Hierarchical Cluester Analysis(HCA) or some other cluster algorithm.

### 8\. Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?

Mainly, for a classical implementantion I frame the spam detection problem as supervised learning problem. But it also can be solved with the constraint of being a unsupervised learning problem.

### 9.What is an online learning system?

It is a type of machine learning system where the algorithm is able to learn in an incremental fashion. Meaning that the algorthim can learn on the fly, in contrast with the batch learning.

### 10.What is out-of-core learning?

It is the case when the size of the dataset cannot fit in the machine memory an thus it is prefer to use online learning algorithms due to this constraint.

### 11.What type of learning algorithm relies on a similarity measure to make predictions?

Supervised Learning, Regression

### 12\. What is the difference between a model parameter and a learning algorithm’s hyperparameter?

A model parameter is a value that is setup in the training process in order to reduce the error that the models generate. An Hyperparameter is a parameter that is extern from the learning algorithm and can be manipulated for us in order to improve the model, it remains constant along the learning process.

### 13.What do model-based learning algorithms search for? What is the most common strategy they use to succeed? How do they mae predictions?

Model-based learning algorithms search for building a statistical model that describes a certain behavior base on the training data that goes in. The most common strategy of its succeed is because they do not need instances to make a prediction as instance-based learning algorithms. Once the statistical model was built and thus the parameters were defined, you can use it like mathematical functions $\hat{y}=f(x)$ where $x$ represents an observation and $\hat{y}$ the prediction.

### 14.Can you name four of the main challenges in Machine Learning?

- poor Quality and low quantity of data
- Nonrepresentative training data (the data does not represent the new unknown instances and thus do not generalize)
- Irrelevant features (it can be solve with feature engineering->feature selection, feature extraction, gathering more data to make new features )

### 15\. If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?

Overfitting.

- Constraining the model (regularitazion: reducing the model's degree freedom)
- Apply a crossvalidation as a validation technice to customize the hyperparameters that best perfom to reduce the generalization error.

### 16\. What is a test set and why would you want to use it?

The test set is mainly use to calculate the generalized error to have an idea about model's accuracy in front new instances. Using cost functions (how bad) or utiliy functions (how good).

### 17.What is the purpose of a validation set?

Firstly, the validation set is subset from training set that is used for measure the accuracy during the trainig phase. This validation set also has the purpose of avoiding the problematic to only setup our hyperameters to the test set. Because in contrast if we do not count with a validation set, maybe we will had a low generalized error, but in production the model has a higher generelization error from the expected. The reason is becase we only tunep our model base on a single same test set and not using a second holdout set.

### 18\. What can go wrong if you tune hyperparameters using the test set?

As I said in the previous question if we only setup our hyperparameters for the test set we can easily fall on the problamtic of a high generalization error in production. Because we didn't use another "test set" (validation set) to measure the performance with differents hyperparameters.

### 19\. What is cross-validation and why would you prefer it to a validation set?

In simple words, Cross-Validation is model validation technique. Where the training set is splitted into two new subsets, a new training set and a validation set. All this apart from the test set. In cross validation there is another variant that is called ***Leave-One-Out Cross-Validation*** (LOOCV), but the most popular is ***K-Fold Cross-Validation*** (k-fold CV) here at below is a representation of this variant:

![26f01c431480ab1025cbee4002b65e98.png](_resources/787941b150c341c3b54273a5d97741d8)

It is divide the training set in K substets called folds, and one of these folds will be the validation set. Thus it can be made K combinations where it can be selected different validation sets and therefore it is prefered to train the model with these K different combinations to have a more robust measure.

And Cross-validation is use mainly for the next reasons:

- When we do not count with a considerable amount of data.
- When the data itself is to critical to be wasted on splitting the dataset to make measuremnts about model's performance/accuracy.
- To make a more accurate, robust, and solid measurement about model's accuracy.  
    And it is prefered using it when we have a validation set becasue we obtain more confident results. Using a cross-validation technique we reuse this validation set to feed the model.k
