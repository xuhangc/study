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

