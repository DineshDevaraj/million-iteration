# million-iteration
Collection of steps to compare time taken by MySQL Join statement against Python for-loops

There is a ***superstition*** among many software developers that SQL Join statements works at speed of light with zero milli-second time taken and they think SQL engine as a magic box. This benchmark is an attempt to compare the time taken by SQL Join statements against for-loops in Python programming language

So are SQL Joins not fast? Yes they are fast compared to subquery but not compared to native programs

The word performance is a relative term. Which means when you say SQL Join statements are fast, you also have to answer the question "Compared to what?"

# Pre Requisite 
1. Docker installed
2. Run MySQL docker instance and name it as mysql-inst
3. Clone this repo into /home folder in mysql-inst
4. Install Python 3.X latest in mysql-inst

# Initialize the Database
1. Connect to mysql-inst **$>** docker exec -it mysql-inst bash
2. Connect mysql client to dbms **$>** mysql -h 127.0.0.1 -u <username> -p
3. Create tables, stored procedure and populated tables using tables-setup.sql script 

# Run the Commands
1. Open a new terminal to run the Python scripts
2. Run the Python script **$>** python3 without-alloc.py
3. After execution note down the values shown on screen
4. In without-alloc.py script you can find the code for different combinations of for-loop and their respective SQL Join statements 
5. You can copy the respective SQL Join statements and run it in mysql client terminal and note down the time taken
6. Now you can compare the respective time taken to know the difference in perfromance
