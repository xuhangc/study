# Applied Machine Learning Algorithms

## Review

### Defining model vs. algorithm

An algorithm is a mathematical technique or equation(that is, a framework).

A model is an equation that is formed by using data to find the parameters in the equation of an algorithm.

example:

![1](./1.png)

### Process overview

![2](./2.png)

## Logistic Regression

**Regression** is a statistical process for estimating the relationships among variables, often to make a prediction about some outcome.

**Logistic regression** is a form of regression where the target variable is binary.

Example:

![3](./3.png)

When and when not

![4](./4.png)

#### Hyperparameters

The C hyperparameter is a regularization parameter in logistic regression that controls how closely the model fits to the training data.

Regularization is a technique used to reduce overfitting by discouraging overly complex models in some way.

![5](./5.png)

Example:

![6](./6.png)

## Support Vector Machines

A support vector machine is a classifier that finds an optimal hyperplane that maximizes the margin between two classes.

Example:

![7](./7.png)

![8](./8.png)

The kernel trick (or kernel method) transforms data that is not linearly separable in n-dimensional space to a higher dimension where it is linearly separable.

Example:

![9](./9.png)

When and when not

![10](./10.png)

C

![11](./11.png)



## Multi-layer Perceptron

A multilayer perceptron is a classic feed-forward artifical neural network, the core component of deep learning.

Alternativerly: A multilayer perceptron is a connected series of nodes (in the form of a directed acyclic graph), where each node represents a function or a model.
![12](./12.png)

![13](./13.png)

The hidden layer size hyperparameter determines how many hidden layers there will be and how many nodes in each layer.

The activation function hyperparameter dictates the type of nonlinearity that is introduced to the model.

- Sigmoid
- TanH
- ReLU

![14](./14.png)

## Random Forest

A random forest merges a collection of independent decision trees to get a more accurate and stable prediction.

Ensemble methods combine several machine learning models in order to decrease both bias and variance.

Majority Voting

![15](./15.png)

The n_estimators hyperparameter controls how many individual decision trees will be built.

- width of tree

The max_depth hyperparameter controls how deep each individual decision tree can go.

- depth of tree

![16](./16.png)

## Boosting

Boosting is an ensemble method that aggregates a number of weak models to create one strong model.

A weak model is one that is only slightly better than random guessing. A strong model is one that is strongly correlated with the true classification.

Boosting effectively learns from its mistakes with each iteration.

![17](./17.png)

Training is sequential. Prediction is parallel.

Weighted Voting

![18](./18.png)

learning rate

max_depth lower than Random Forest

## Summary

