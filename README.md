# Labb1
Purpose of this lab is to use fundamentals of python to transform raw data to representable format. More
 specifically, you will perform a step in decoding DNA data. This can be a common topic for a data analyst or
 data scientist in a medtech company. You do not need prior knowledge about DNA for this lab. 


 Task 1
 You are given several simplified sequences of DNA codes*. Your task is to count the number of different
 DNA letters in each sequence. In reality, this is an essential step for scientists to understand the genetic
 information from the human cell**. Following the instructions below:
 read the text file called dna_raw.txt
 each sequene is composed of two lines of data: the first line beginning with > sign is the
 sequence ID, while the following line is the actual sequence
 the actual sequence is not case-sensitive, which means that lower and upper case letters are
 treated the same
 for each sequence, create a dictionary to count the number of each DNA letter in that sequence
 for each sequence, graph the frequency of DNA letters for each sequence.

 Task 2 (bonus)
Lab 1 python fundamentals.md
 2025-02-11
 there can be raw DNA data files with different number of sequences. Based on your solution code
 above, create a function that is able to take in new data files in similar format as dna_raw.txt with
 different number of sequences, and produce the same results above
 you have received also another DNA codes that is more complicated. The file is called
 dna_raw_complicated.txt. In this file, each DNA sequence can be composed of multiple lines of data in
 the text file. In this case, are you able to solve the task in the same way as before? If not, update your
 code to solve the same task with the new data
