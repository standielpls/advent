# Part 1

The thing to care about here is the `total` of the reindeer carrying the `most` calories.

Which means we can keep a counter that represents the max value seen per reindeer.

"Per reindeer" is denoted by a line break so we can use `line.isspace()` in python, or given that this file reader converts to string automatically, we can look for `\n`

We then end up solving with O(n) time and O(1) space

# Part 2

Now we have to keep a record of the top 3 total calories. We can implement a similar counter by have 3 of them.
This might get a bit messy and having to do a lot of maths between the 3 numbers.
 
We can optimize for a bit of a cleaner design.
We can keep an array of total calories that can define the top 3.
The smallest of the 3 can be popped off if something bigger is found.

This design is a bit more costly. 
We have O(3) space which translates to O(1)

For each iteration (at the worst case), we need to use `min` to loop through this array and remove the record.
