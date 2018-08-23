# Documentation

Syntaxes of YTScript, behivour will be explained in this md file.

### Basic Syntaxes
***
#### init


initialize the YTScript Runtime

Running this code is needed before runnning anything.

>What it does:

 - Changes the `runmode` to `stand`

 - Changes the `outputmode` to `print`

   (Will be explain in detail later)

 - Undefine all variables

>Syntax

```
init
```

***

#### output

output text based on different output mode

>syntax

```
output <text>
```

>Example

```
init
output 'The quick brown fox jumps over the lazy dog.'
```

output:

```
The quick brown fox jumps over the lazy dog.
```
***
#### setvar

Set an value and data type of an variable

>syntax
```
init
setvar <variable name> <datatype> <value>
```
>example
```
setvar a int 3
```
***
#### outputvar

output an variable's value

>syntax
```
outputvar <variable name>
```
>example
```
init
setvar a int 1
outputvar a
```
output:
```
1
```
***
#### setvarmath

Set a variable value by using math expression between two other variables

>syntax
```
setvarmath <target variable> <first variable> <+|-|*|/|^|%> <second variable>
```
>example
```
init
setvar a int 1
setvar b int 2
setvarmath c a + b
outputvar c
```
output:
```
3
```
***
#### copyvar

Copy the value of an variable to another

>syntax
```
copyvar <source variable> <target variable>
```
>example
```
init
setvar a int 1
copyvar a b
outputvar b
```
output:
```
1
```
***
#### inputvar

Define variable by user input

>syntax
```
inputvar <variable name> <datatype> <text prompt>
```
>example
```
init
inputvar a int 'Please enter an integer:'
outputvar a
```
output:
```
Please enter an integer: [User inputs 2 and presses enter]
2
```
***
#### outputnl

output an new line(`\n`)

>syntax
```
outputnl
```
***
#### goto 

This is only for scripts in a file, not in runtime

execute starting from a line

>syntax
```
goto <line number>
```
>example
```
init
inputvar a int 'a='
outputvar a
goto 2
```
output:
```
a= [User inputs 2 and presses enter]
2
a= [User inputs 3 and presses enter]
3
a= [User inputs 10 and presses enter]
10
...
```
***
#### exit

Exit the program

>syntax
```
exit
```
>example
```
init
output 1
output 2
exit
output 3
output 4
```
output:
```
1
2
```
***
#### _pass

comment. does not mean anything

>syntax
```
_pass <text>
```
>example
```
init
output 1
_pass
output 2
_pass the line above outputs 2 and a new line
```
output:
```
1
2
```
***
#### sleep

wait for a certain time

>syntax
```
sleep <time>
```
>example
```
init
output 1
sleep 1
output 2
```
output:
```
1 [stops for 1 sec]
2
```
***
#### os

execute system commands

>syntax
```
os <command>
```
>example
```
os 'ping www.google.com'
```
output:
```
Pinging www.google.com [172.217.194.99] with 32 bytes of data:
Reply from 172.217.194.99: bytes=32 time=17ms TTL=47
Reply from 172.217.194.99: bytes=32 time=15ms TTL=47
Reply from 172.217.194.99: bytes=32 time=14ms TTL=47
Reply from 172.217.194.99: bytes=32 time=14ms TTL=47

Ping statistics for 172.217.194.99:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 14ms, Maximum = 17ms, Average = 15ms
```
***
#### setmode

Sets a certain mode to a certain value

mode types:
 - Output mode  `output` can be setted to value `print` `std` or `null`
 - Execute mode `runmode` can be setted to value `stand` or `fullarg`

>syntax
```
setmode <modetype> <value>
```
>example
```
init
setmode output std
```
***
#### script

Runs a file contains YTScript Syntaxs

>syntax
```
script <file path>
```
>example
```
init
script 'text.txt'
```
***
***
### Logic
***
#### if

This is only for scripts in a file, not in runtime

To see if two variable meets the criteria

if true, it will continue to the next line

if false, it will skip the next line

>syntax
```
if <variable 1> <=|<|>|>=|<=|!=> <variable 2>
```
>example
```
init
setvar a int 1
setvar b int 2
if a = b
output 1
output 2
```
output:
```
2
```
***
### Modes

how the YTScript behives
***
#### Execute mode

the `runmode` has 2 types:
 - `stand`
 - `fullarg`

>stand

it will breake arguments from spaces, but will not breake the ones in single quote marks

>example
```
_pass running in stand mode
output 1   2
output 1 2
output 12
output '1  2'
output "1  2"
```
output:
```
12
12
12
1  2
"12"
```

>fullarg

passes all charactors

this is handy when using output

>example

```
_pass running in fullarg mode
output 1  2
output 1   2
output 12
output '1  2'
output "1  2"
```
output:
```
1  2
1   2
12
'1  2`
"1  2"
```
***
#### output mode

the `output` mode has 3 types:
 - `print`
 - `std`
 - `null`
 
>print
outputs text with an newline behind
>example
```
_pass running in print mode
output 1
output 2
output 3
```
output:
```
1
2
3
```
>std
output without newline behind
>example
```
_pass running in std mode
output 1
output 2
outputnl
output 3
```
output:
```
12
3
```
>null
does not output any output but newline
>example:
```
_pass running in null mode
output 1
output 2
outputnl
output 3
```
output:
```
[newline]
```
***
### Examples:
***
>The hello world
```
init
output hello, world
```
or
```
init
setmode output std
output hello, world
outputnl
```
output:
```
hello, world
```
***
> counting sheeps
```
init
setvar a int 6
setvar b int 0
setvar c int 0
setvar d int 1
setmode output std
if a = b
goto 16
output 'there are '
outputvar b
output ' sheeps'
outputnl
setvarmath c b + d
copyvar c b
goto 7
exit
```
output:
```
there are 0 sheeps
there are 1 sheeps
there are 2 sheeps
there are 3 sheeps
there are 4 sheeps
there are 5 sheeps
```
***
