# Project: ML Based Book Recommendation System ! | Collaborative Filtering Based


![image](https://github.com/user-attachments/assets/7c041c27-ef9d-488c-8c48-74db7a0b79af)
Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

# About this project:
This is a collaborative filtering based books recommender system & a streamlit web application that can recommend various kinds of similar books based on an user interest.

# Demo:
![Screenshot (277)](https://github.com/user-attachments/assets/0ab16513-406b-4e78-a6ac-038b47858d1e)


![Screenshot (276)](https://github.com/user-attachments/assets/4c58b6c7-8a9e-4bf0-8276-19f4d6aee6f7)


![Screenshot (275)](https://github.com/user-attachments/assets/7fe4be27-fbc4-415e-9403-7e6c4aa5cf68)



# Dataset has been used:
<a href="https://www.kaggle.com/ra4u12/bookrecommendation"
rel="nofollw">Dataset link</a> 


# Concept used to build the model.pkl file : NearestNeighbors

1 . Load the data

2 . Initialise the value of k

3 . For getting the predicted class, iterate from 1 to total number of training data points

4 . Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our distance metric since it’s the most popular method.

5 . Sort the calculated distances in ascending order based on distance values

6 . Get top k rows from the sorted array

# Built With

1.streamlit

2.Machine learning

3.sklearn








