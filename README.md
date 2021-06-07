# million-iteration
Collection of steps to compare time taken by MySQL join vs Python loop

Superstition: There is a superstition in the IT industry that SQL Join works at speed of light and they think SQL engine is a magix box. 

Q1. So SQL Joins are not fast? 
Yes they are fast compared to subquery but not compared to native  programs

The word performance is a relative term. Which means when you say SQL Join statements are fast, you also have to answer the question "Compared to what?"

# Approach
1. Run MySQL docker instance
2. Create tables, stored procedure and populated tables using tables-setup.sql script
3. Run the Python scripts and note down the time taken
4. Run respective SQL query given in the Python scripts
5. Compare the respective values to understand the performance of SQL Join statements
