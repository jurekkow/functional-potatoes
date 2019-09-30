# functional-potatoes
Learn basics of functional design by selling potatoes :sweet_potato:.

# Problem
Your client wants online shop with potatoes.
His potato suppliers provide APIs to check availability, price etc.
These APIs are inconsistent and messy.
We want to make our front-end colleagues life easier.

First, we want to integrate with provider called bestpotato.com.
Example response can be found in [this file](bestpotato.json).

Our response should be of form:
```
[
  {"name": "Russer", "priceKg": 1.1},
  {"name": "Austrian Crescent (Premium)", "priceKg": 5.08},
]
```
You can notice that we have to:
- Drop unneeded fields
- Extract kind name from inconsistent structure
- Convert price per ton to proce per kg
- Format kind name, so that each word starts with capital letter
and there is a "(Premium)" sufix for potatoes more expensive 
than 5 units
- Finally map fields to `"name`" and `"priceKG"`

# Let's code! :computer:
This repo has a working solution, so you can just read throgh it's
code to see how functional design can help you tackle this task.

Instead, I recommend you to `git checkout 4fbc87a3`, which is the last
commit without working solution, 
try it on your own and then compare with solution.

Do not remember to install [requirements](requirements.txt).

Good luch and have fun!

