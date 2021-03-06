# Test-Driven Development with Python
Code from book

## Testing Code
1. We start by writing a functional test, describing the new functionality from the
user’s point of view.
2. Once we have a functional test that fails, we start to think about how to write
code that can get it to pass (or at least to get past its current failure). We now use
one or more unit tests to define how we want our code to behave—the idea is that
each line of production code we write should be tested by (at least) one of our
unit tests.
3. Once we have a failing unit test, we write the smallest amount of application code
we can, just enough to get the unit test to pass. We may iterate between steps 2
and 3 a few times, until we think the functional test will get a little further.
4. Now we can rerun our functional tests and see if they pass, or get a little further.
That may prompt us to write some new unit tests, and some new code, and so on.