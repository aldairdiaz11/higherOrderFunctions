### Create your Higher Order Functions

<br>
To further your understanding of functional programming, you will create your own higher-order functions and then use
them to process data from a CSV file. 

The functions you will create are:

* `count()`: will return the frequency of an element in an iterable.
* `average()`: will return the average of elements in an iterable of numbers.

The ``count()`` function will be a special type of `filter()` function that returns the number of occurrences of an
element instead of rerunning a Boolean value. The ``count()`` function will accept the following two parameters:

* ``predicate``: when evaluated to `True` will allow a counter to increment by one.
* ``itr``: the collection containing the element of interest.

The ``average()`` function will compute the arithmetic mean of a collection. You will implement this function recursively
to adhere to functional programming principles.
``average()`` will only accept one parameter: `itr`, the collection to be averaged.

Before we begin, please keep in mind the following:

The ``reduce()`` function can accept a third parameter that serves as the initial value, thereby allowing an initial
condition that is not of the same type as the collection ``reduce()`` is operating on. Syntax:

```angular2html
reduce(lambda x: x + y, some_collection, initial_value)
```

You will use these functions to process sales data from a CSV file called <b>1kSalesRec.csv</b>
