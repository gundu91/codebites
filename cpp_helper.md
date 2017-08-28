# C++ Helper
- [Flow Control (Selection and Iteration)](#flow-control)

## Flow Control
**If / Else If / Else**
```cpp
if (condition)
{
	statement;
	statement;
}
else if (condition)
{
	statement;
	statement;
}
else
{
	statement;
	statement;
}
```

**Switch**: condition must be a constant expression, more compact and easier to read than multi-branch if statements, especially useful for menus; omitting the break causes follow through; default is similar to else
```cpp
switch (expression) 
{
case 1: statement; break;
case 2: statement; break;
case 3: statement; break;
default: statement; break;
}
```

**Ternary Operator**: shorthand for a simple if-else
```cpp
max = (m > n) ? m : n;
// instead of 
if (m > n) max = m; 
else max = n; 
```

**While**: execute a statement as long as some condition is true
```cpp
int count = 0;
while (count < 5)
{
	cout << “Hello World” << endl;
	count++;
}
```

**Do While**: similar to while but check condition after executing statement 
```cpp
int count = 0;
do
{
	cout << “Hello World” << endl;
	count++;
} while (count < 5);
```

**For**: execute a statement on every element of some data, or some fixed number of times
```cpp
for (int count = 0; count < 5; count++)
{
	cout << “Hello World” << endl;
}
```
