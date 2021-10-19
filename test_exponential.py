from mail import exponential
import pytest

@pytest.mark.parametrize('num,expected', [(2,4),(3,9),(4,16)])
def test_exponential_2(num,expected):
    assert(exponential(num)==expected) 