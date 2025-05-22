PURPOSE OF PROJECT 
Suppose that you are given a data file titled “books_dataset.txt” which includes some book data. 
Each book (or record) includes id, title, author name, category of the book. Implement fast 
searching on title, author name and category. You are supposed to select and implement the 
most appropriate indexing mechanism (Simple indexing/multilevel indexing and correct data 
strucure for this mechanism) for the given problem. 
A) ALGORITHM DESIGN AND DETAILED EXPLANATION 
1. Problem Definition: 
The file named "books_dataset.txt" contains over 1 million book records. Each record includes 
an ID, title, author, category, and publication year. The goal is to perform fast and efficient 
searches based on title, author name, or category. 
2. Selected Method: 
To efficiently search through the book dataset, a B+ Tree Indexing method was selected. This 
method is ideal for fast searching and retrieval operations. B+ Trees allow for efficient insertion, 
deletion, and search operations by maintaining sorted keys and linked nodes. The dataset is 
indexed on three fields: title, author, and category, enabling fast lookups by any of these 
attributes. The bisect algorithm is used for fast insertion and searching within the B+ Tree. This 
approach optimizes the search performance, especially for large datasets.
