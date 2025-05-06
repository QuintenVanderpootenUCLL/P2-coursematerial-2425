from parentheses import matching_parentheses
import pytest

@pytest.mark.parametrize("string", [
    "((((((((((()))))))))))"
    "()()()()()()()()"
    "()(((())))()((()))",
    "((())((()))))"
])
def test_matching_parentheses_true(string):
    assert matching_parentheses(string), f"parentheses {string} are not properly oppened and closed"


@pytest.mark.parametrize("string",[
   ")((()))",
   "(()))(())",
   "(((()))))",
   ")("
])
def test_matching_parentheses_true(string):
    assert not matching_parentheses(string), f"parentheses {string} are not properly oppened and closed"
