# Python Fun

Playing with Python and ***Functional Programming (FP)*** concepts after watching [The Power of Composition](https://www.youtube.com/watch?v=vDe-4o8Uwl8) by Scott Wlaschin.

## Content

- **compose** function:
  - Implementation: [`src/compose.py`](src/compose.py) 👈 **Click here to check it out!**
  - Tests: [`tests/test_compose.py`](tests/test_compose.py)

- A (syntactic sugar) **pipe** function:
  - Implementation: `src/pipe.py`
  - Tests: `tests/test_pipe.py`

- The ***Think Of A Number*** game shown in Scott's presentation:
  - Implementation: [`src/think_of_a_number.py`](src/think_of_a_number.py)
  - Tests: [`tests/test_think_of_a_number.py`](tests/test_think_of_a_number.py)

- The solution to the ***Roman Numerals*** problem:
  - Implementation: [`src/think_of_a_number.py`](src/think_of_a_number.py)
  - Tests: [`tests/test_think_of_a_number.py`](tests/test_think_of_a_number.py)

- (WIP) The *"don't do this in an interview"* ***FizzBuzz*** solution:
  - Implementation: [`src/fizzbuzz.py`](src/fizzbuzz.py)
  - Tests: [`tests/test_fizzbuzz.py`](tests/test_fizzbuzz.py)

## How do I run the tests?

To type check the code:

```sh
docker-compose run python-fun mypy /code --pretty --config-file=pyproject.toml
```

To run the unit tests:

```sh
docker-compose run python-fun pytest /code/tests -vv -s
```

## Notes

To type check the code, I configured [mypy](https://mypy.readthedocs.io/en/latest/index.html) following [this article](https://blog.wolt.com/engineering/2021/09/30/professional-grade-mypy-configuration/).
