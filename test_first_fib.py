from main import first_fib

def test_smoke():
    assert 2+2==4

def test_single_step():
    assert first_fib(7,8) == (1,7)
    assert first_fib(2,2) == (0,2)