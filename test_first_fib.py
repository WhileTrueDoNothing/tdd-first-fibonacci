from main import first_fib

def test_smoke():
    assert 2+2==4

def test_single_step():
    assert first_fib(7,8) == (1,7)
    assert first_fib(2,2) == (0,2)

def test_first_nums():
    assert first_fib(1,3) == (1,3)
    assert first_fib(23,47) == (23,47)

def test_multi_step():
    assert first_fib(398,644) == (2,6)
    assert first_fib(2462,3984) == (44,90)