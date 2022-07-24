# Python Fun

Playing with Python and ***Functional Programming (FP)*** concepts after watching [The Power of Composition](https://www.youtube.com/watch?v=vDe-4o8Uwl8) by Scott Wlaschin.

## How do I run the tests?

To type check the code with [mypy](https://mypy.readthedocs.io/en/latest/index.html):

```sh
docker-compose run python-fun mypy /code --pretty --config-file=pyproject.toml
```

To run the unit tests:

```sh
docker-compose run python-fun pytest /code/tests -vv -s
```

## Notes

I configured mypy following this article: [Professional-grade mypy configuration](https://blog.wolt.com/engineering/2021/09/30/professional-grade-mypy-configuration/)
