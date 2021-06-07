# million-iteration
Collection of steps to compare time taken by MySQL Join statement against Python for-loops

There is a superstition among many software developers that SQL Join statements works at speed of light with zero milli-second time taken and they think SQL engine as a magic box

This benchmark is an attempt to compare the time taken by SQL Join statements against for-loops in Python programming language

Q1. So SQL Joins are not fast? 
ANS: Yes they are fast compared to subquery but not compared to native programs

The word performance is a relative term. Which means when you say SQL Join statements are fast, you also have to answer the question "Compared to what?"

# Approach
1. Run MySQL docker instance
2. Create tables, stored procedure and populated tables using tables-setup.sql script
3. Run the Python scripts and note down the time taken
4. Run respective SQL query given in the Python scripts
5. Compare the respective values to understand the performance of SQL Join statements
