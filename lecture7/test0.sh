# running multiple tests on the prime.py file

python3 -c "from test0 import test_prime; test_prime(3, True)"
python3 -c "from test0 import test_prime; test_prime(4, False)"
python3 -c "from test0 import test_prime; test_prime(6, False)"
python3 -c "from test0 import test_prime; test_prime(25, False)"
python3 -c "from test0 import test_prime; test_prime(83, True)"
