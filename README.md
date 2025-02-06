                                                                                                      Explaination of the code
Overview-

This program processes a list of words to identify the longest and second-longest compound words. A compound word is defined as a word that can be formed by concatenating two or more other words from the list. 
The implementation utilizes a backtracking approach with memoization to efficiently determine whether a word qualifies as a compound word.


Design Decisions & Approach-
•	Reading Words: The words are read from a file and stored in a list for processing.
•	Checking Compound Words: A recursive function with memoization is used to determine if a word is a compound word by iterating through possible prefixes and checking if the remaining suffix is also a valid word.
•	Efficiency Considerations:
o	Words are sorted in descending order by length to ensure the longest words are checked first.
o	A set is used for quick lookups to optimize performance.
o	The algorithm removes words temporarily from the set while checking to avoid false positives.
•	Performance Measurement: The execution time for processing each input file is recorded in milliseconds.


Execution Steps-
1.	Ensure the input files (Input_01.txt, Input_02.txt) are present in the same directory as the script.
2.	Run the script using Python:
python script.py
3.	The program will output:
o	The longest compound word
o	The second-longest compound word
o	The time taken for execution in milliseconds


Requirements-
•	Python 3.x
This program efficiently finds the longest compound words from large word lists and is optimized for performance using memoization and set-based lookups. 
                                                                                                                            
                                                                                                                             
                                                                                                                                                                                                                 -BY VANSHIKA KANSAL

