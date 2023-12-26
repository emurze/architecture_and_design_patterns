# Pytest

### -v --verbose

#### Without

![without_verbose.png](images/without_verbose.png)

#### With

![with_verbose.png](images/with_verbose.png)

### -r... - info settings

f - failed

E - error

s - skipped

x - xfailed

X - xpassed

p - passed

P - passed with output

### --tb short | long (error table)

### -s -> prints

### -x -> stop after first failure

### --maxfail 3 -> stop after fourth failure

### pytest -m slow + you should register marker

### pytest --fixtures

### pytest -x --pdb -l (short vars) --showlocals (vars)

### Run concrete test

![run_concrete_test.png](images/run_concrete_test.png)

![concrete_class_test.png](images/concrete_class_test.png)

### Parametrize tests

![parametrize_tests.png](images/parametrize_tests.png)

![parametrize_tests_result.png](images/parametrize_tests_result.png)

### Class tests

![class_tests.png](images/class_tests.png)


### Code without dependencies

![fixtures](images/fixtures.png)

### Setup fixtures

![setup_fixtures](images/setup_fixtures.png)

### Auto scope fixture

![auto_fixture.png](images/auto_fixture.png)


### Test Settings for DB

* pytest.env lib

![test_env.png](images/test_env.png)


### Conftest.py

This file contains all global or local *fixtures*ss

![conftest.png](images/conftest.png)
