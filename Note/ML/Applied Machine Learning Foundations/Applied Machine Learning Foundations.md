# Applied Machine Learning: Foundations

## Basics

Fitting a function to examples and using that function to generalize and make predictions about new examples.

### Pattern matching

- Does it require a prediction or bucketing something into categories?
- Is the problem relatively self-contained?
- Do I have data with labels?
- Do I have the ability to assess the quality of the model?
- Can I determine an acceptable accuracy threshold?

### Why Python

- popularity
- more machine learning packages
- easy to learn, easy to use

### Deep learning

Fitting functions to examples where those functions are connected layers of nodes; with the intent to generalize and make predictions about new examples

connected pattern matching

### Artifical Intelligence

Weak AI - intelligence specifically designed to focus on a narrow task

Strong/general AI - a machine with consciousness, sentience, and a mind; general intelligence capable of any and all cognitive functions and reasoning that a human is capable of

### Challenges

#### Problem scoping
- The right problem isn't being solved
- Tolerance threshold is undetermined
- Impact in real environment can't be measured

#### Data
- Lack of data/data sensitivity
- Too much data
- Data doesn't have labels
- Data is too biased, dirty, noisy, incomplete, etc.

#### Infrastructure
- Lack skills to robustly automate
- Not enough computer power
- Inability to A/B test with existing solution
- Inability to continously track model quality

#### Latency
- Model takes too long to train
- Model takes too long at inference time

## Exploratory data analysis and data cleaning

#### Why Exploratory data analysis
- Understand the shape of data
- Learn which features might be useful
- Inform the cleaning that will come next

#### What
- Counts or distributions of all variables
- Data type for each feature
- Missing data
- Correlations
- Duplicates

#### Why data cleaning
- Shape data in a way a model can best pick up on the signal
- Remove irrelevant data
- Adjust features to be acceptable for a model

#### What
- Anonymize
- Encode categorical variables
- Fill missing data if necessary
- Prune/scale data to account for skewed data/outliers

## Measurement

#### Split up data
- Training dataset - 60% - data used to train the model(allow the algorithm to learn from this data)
- Validation dataset - 20% - data used to select the best model(optimal algorithm and hyperparameter settings)
- Test dataset - 20% - data used to provide an unbiased evaluation of what the model will look like in its real environment

#### Risk of not splitting up
- Overfitting or underfitting to the data
- Inaccurate representation of how the model will generalize

#### Holdout test set
Sample of data not used in fitting a model; used to evaluate the model's ability to generalize to unseen data

#### K-Fold Cross-Validation
Data is divided into k subsets and the holdout method is repeated k times. Each time, one of the k subsets is used as the test set and the other k-1 subsets are combined to be used to train the model.

#### Evaluation Framework
- Evaluation metrics
  - Accuracy
  - Precision
  - Recall
- Process
    1. Run fivefold cross-validation and select the best models
    2. Re-fit models on full training set, evaluate those models on the validation set and pick the best one.
    3. Evaluate that best model on the test set to gauge its ability to generalize to unseen data.

## Optimizing

#### Bias/variance tradeoff

Bias is the algorithm's tendency to consistently learn the wrong thing by not taking into account all the information in the data.

High bias is a result of the algorithm missing the relevant relations between features and target outputs.

Variance refers to an algorithm's sensitivity to small fluctuations in the training set.

High variance is a result of the algorithm fitting to random noise in the training data.

Total Error = (Bias + Variance) + Irreducible Error

Underfitting occurs when an algorithm cannot capture the underlying trend of the data.

Overfitting occurs when an algorithm fits too closely to a limited set of data.

