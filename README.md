# About ISE
ISE is a 2d Esolang designed to be an easy stack-based language for beginner esolang programmers to get started with. The name ISE (Pronounced: eez) comes from "[I]ntroduction to [S]tack-based [E]solangs". I am just starting to learn esolangs myself and I wanted there to be a good solution for people who find the idea of a stack a little confusing. This is the reason for the functionality of being able to write a single-digit number to the stack by just writing it in your code. It is also the reason for the & operator, which does the string concatenation of the top 2 numbers on the stack, and then converts it back to an int. Being a beginner myself helped me grasp what would feel most natural to a new esolangist. It also is a fairly simple interpreter, so it could also be a relatively easy programming language to write your own compiler/interpreter for.
for.

## Syntax
Note that you start in the upper lefthand corner of the file

| Syntax | Description |
| :----: | :---------- |
| + | Add top 2 nums |
| - | Subtract top 2 nums |
| * | Multiply top 2 nums |
| / | Divide top 2 nums |
| % | Mod top 2 nums |
| $ | Removes the top value of the Stack |
| ? | Skips the next value in the current Move Directon if the top number on the stack == 0 |
| c | Print ASCII Char of top num |
| n | Print top num |
| , | Add ASCII Code of input onto the Stack |
| # | Add int of input onto the Stack |
| : | Duplicate the top number onto the Stack |
| Integers<br/>0-9 | Add typed number onto the Stack |
| & | Int of the String Concatenation of the top 2 nums |
| \ | Switch the data stored at the index of the top 2 nums and remove the top 2 nums |
| \|| Switch the data stored at the index of the top 2 nums |

## Example Code
### Truth Machine:
#### What Does it Do:
If the user's input == 0, print a 0, else print 1s forever

#### Steps:
1. Ask for an Input
2. Adds input onto the stack
3. If your input == 0, print 0, else print 1s forever
   
#### Implementation in ISE:
```
#?v>n!
  n
  ^
```

### 99 Bottles of Beer:
#### What Does it Do:
It prints the lyrics of 99 Bottles of Beer in the format:<br/>
99 bottles of beer on the wall, 99 bottles of beer.<br/>
Take one down and pass it around, 98 bottles of beer on the wall.<br/><br/>
98 bottles of beer on the wall, 99 bottles of beer.<br/>
Take one down and pass it around, 98 bottles of beer on the wall.<br/>
<br/>
...
<br/><br/>
1 bottle of beer on the wall, 1 bottle of beer.<br/>
Take one down and pass it around, 0 bottles of beer on the wall.<br/><br/>
No more bottles of beer on the wall, no more bottles of beer.<br/>
Go to the store and buy some more, 99 bottles of beer on the wall.<br/>

#### Steps:
1. Ask for an Input
2. Adds input onto the stack
3. If your input == 0, print 0, else print 1s forever
   
#### Implementation in ISE:
```
#?v>n!
  n
  ^
```