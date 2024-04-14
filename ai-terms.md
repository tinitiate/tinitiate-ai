# AI and ML Terms Explained

## Types of AI /ML
### Neural Networks
* Neural networks are a class of machine learning models inspired by the structure and function of the human brain.
* They consist of interconnected nodes (neurons) that process input data and can learn complex patterns through training.
* Deep neural networks, with multiple layers of neurons, are capable of learning very sophisticated representations of data.

## Models
* In ML and AI, a model is a mathematical representation of the real-world process or phenomenon that you're trying to understand or predict.
* It's created by applying a learning algorithm to a dataset, which allows the model to learn patterns and relationships in the data. Once trained, the model can be used for tasks like prediction, classification, and clustering on new data.
* Models: **raw models** or **untrained models**, These models have been initialized but have not yet been exposed to any training data, so they do not have the ability to make accurate predictions or decisions.
* The process of training involves adjusting the model's parameters based on the input data and the desired output, allowing it to learn the patterns and relationships within the data.
* Once a model is trained, it can then be used for **inference** on new data.

## Inference
* Inference in the context of machine learning (ML) and artificial intelligence (AI) refers to the process of using a trained model to make predictions or decisions based on new, unseen data.
* After a model has been trained on a dataset, it can infer patterns and relationships in new data to provide outputs such as classifications, recommendations, or other insights.

## Datasets
* A dataset is a collection of data that is used to train, validate, and test machine learning models.
* It typically consists of input features (independent variables) and corresponding output labels (dependent variables) for supervised learning, or just input features for unsupervised learning.
* The quality, quantity, and relevance of the dataset significantly impact the performance of the ML models.

## AI Learning Methodologies
### Supervised Learning
* Supervised learning is a type of machine learning where the algorithm is trained on a labeled dataset, meaning each training example is paired with an output label.
* The algorithm learns a function that maps inputs to desired outputs and can then make predictions on new, unseen data.

### Semi-Supervised Learning

### Unsupervised Learning
* Unsupervised learning is a type of machine learning where the algorithm is trained on a dataset without any labels.
* The goal is to discover underlying patterns, structures, or distributions in the data, such as grouping similar data points into clusters.

### Reinforcement Learning
* Reinforcement learning is a type of machine learning where an agent learns to make decisions by taking actions in an environment to achieve a goal.
* The agent receives rewards or penalties based on the outcomes of its actions and uses this feedback to learn the optimal strategy for achieving its objective.


##
### Vector Databases

### Language Chains (Langchains)
* Language chains, or langchains, refer to the concept of chaining together multiple language models or natural language processing (NLP) tasks to achieve more complex or nuanced outcomes.
* For example, one might use a language model to generate a summary of a text, then use another model to translate that summary into a different language, effectively creating a chain of language tasks.
* Langchains can enable more sophisticated AI applications by leveraging the strengths of different models or tasks in sequence.

### Retrieval-Augmented Generation (RAG)
* Retrieval-Augmented Generation (RAG) is a natural language processing (NLP) technique that combines the strengths of two different approaches: retrieval-based methods and generative models.
* The goal of RAG is to enhance the ability of a generative model to produce more accurate and contextually relevant responses by incorporating external information retrieved from a large corpus or database.
* In a typical RAG setup, when a query or prompt is provided, the retrieval component first searches a large collection of documents or knowledge base to find relevant information.
* This retrieved information is then fed into a generative model, such as a transformer-based neural network, which uses it to generate a more informed and contextually appropriate response.
* RAG is particularly useful in applications where the generative model alone might struggle to produce accurate responses due to limited training data or the need for specialized knowledge that is not present in the training set. 
* By augmenting the generation process with retrieved information, RAG can improve the quality of the generated text, making it more relevant, factual, and informative.
* This technique has been applied in various NLP tasks, including question answering, conversational AI, and text summarization.