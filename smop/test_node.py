import pytest
from smop.node import encode, postorder, node

class TestEncode:
    def test_encode_with_uppercase_and_underscores(self):
        assert encode("Hello_World") == "H__ELLO___W__ORLD"

    def test_encode_no_uppercase_no_underscores(self):
        assert encode("helloworld") == "HELLOWORLD"

class TestPostorder:
    def setup_method(self):
        self.simple_node = node()
        self.nested_node = node()
        self.nested_node.child = [node()]

    def test_postorder_simple_node(self):
        assert list(postorder(self.simple_node)) == [self.simple_node]

    def test_postorder_nested_node(self):
        nodes = list(postorder(self.nested_node))
        assert nodes == [self.nested_node.child[0], self.nested_node]

