## Credity Test

### 1. Pythagorean Triplet:
This exercise is base on the Pythagoras theorem and trigonometric identities:
<div class="begin-examples"></div>
 <div class="row">
  <div class="column" markdown="1">
    <img width="200" src="https://i.imgur.com/4hoInkK.png">
  </div>
  <div class="column" markdown="1">
    <img width="200" src="https://study.com/cimages/multimages/16/926405-ids4246826883428030385.png">
  </div>
</div> 
<div class="end-examples"></div>

So "a" and "b" was moved in function of "c" and the 'angle'.
And the hypotenuse "c" increase in an interval of 335 to 500. The lower interval was choose because
the condition a < b < c is mandatory in the triplets so c must be at least 335 to achive that.
The round function was used to get an "integer" (is float type but rounded to zero decimals.)
and the angle didn't start at 1 because with the rounded function b is always equal to c.

The code was made with python3 and in order to use trigonometric identities It was needed the math library.

```sh
$ python3 1-pythagoras.py
```

R/ The product of the pythagorean triplet that satisfies all conditions is: 
    a*b*c = 31875000


Here is a great source to understand more deeply the theory: 
-> https://www.youtube.com/watch?v=QJYmyhnaaek


### 2. How many sundays:

To get the number of sundays in the XXth century knowing that january 1, 1900 is a monday, first we need a list to iterate the 12 month of the year with the number of days of every month, that never changes except for one month in leap-year. 
Then we iterate through the range 1901 to 2000 (include) and the operation that tell us what day is the first of the next month is:
```sh
for month in oneyear: 
        #number of days of the month module 7(number of days of the week)
        #plus the number of the first day(from 1: monday to 7:sunday) of the last month
        newday = month % 7 + first
        #if new day is greater than seven we apply a second module operation to get the number of the week
        if newday > 7:
            newday = newday % 7
````

Run the script:
```sh
$ python3 2-sunday.py
```

R/ The number of months that start in a sunday in the XXth century are 171.
