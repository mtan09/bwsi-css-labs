import pytest
from labs.lab_1.lab_1d import two_sum

def test():
  assert two_sum([-1,-2,0,1], 1) == [2,3]
  assert two_sum([-1,-2,0,1], -2) == [1,2]
  assert two_sum([-1,-2,0,1], 0) == [0,3]
  
if __name__ == "__main__":
    pytest.main()