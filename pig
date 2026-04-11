Pig

create a file
type 
vi student.txt
press i to enable insert mode
paste / write / type data
to save data enable command mode in vi
press esc(escape key)
press :wq [enter]

001,Rajiv,Reddy,21,9848022337,Hyderabad
002,siddarth,Battacharya,22,9848022338,Kolkata
003,Rajesh,Khanna,22,9848022339,Delhi
004,Preethi,Agarwal,21,9848022330,Pune
005,Trupthi,Mohanthy,23,9848022336,Bhuwaneshwar
006,Archana,Mishra,23,9848022335,Chennai
007,Komal,Nayak,24,9848022334,trivendram
008,Bharathi,Nambiayar,24,9848022333,Chennai

#student.txt


///before executing upload student.txt on hdfs
hdfs dfs -put data.txt /user/raj_ops/
/////////////////////////script start pig script
vi mypiggy.pig

student = LOAD 'data.txt' USING PigStorage(',')
   as (id:int, firstname:chararray, lastname:chararray, age:int, phone:chararray, city:chararray);
student_order = ORDER student BY age DESC;
 
student_limit = LIMIT student_order 4;
Dump student_limit;
////////script end
to run the program exceute this command
pig mypiggy.pig
