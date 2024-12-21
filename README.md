# Pizza; OOP quiz

There are two implementations of pizzas, one using dicts and lists, the other using objects.  Both modules have tests that are failing because the source code is wrong.  Change the source code so the tests pass.  Do not change the tests.  If you need to add new classes, they should each be in their own module (file).  Add new tests to demonstrate both new and previous code works as intended.

# Running the tests

## Command line

```bash
python -m pytest
```

To run just the v1 tests

```bash
python -m pytest tests/v1
```

To run just the v2 tests

```bash
python -m pytest tests/v2
```

## vscode

On the left, there is an icon with a class beaker.  That opens the "Test Explorer".

In the test explorer, there's an with a set of trianges that run the tests.

