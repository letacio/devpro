import pytest
from io import StringIO
import sys
from Task2_Inventory import sort_products



@pytest.fixture
def products(): # autouse=True means that this fixture will be used in all tests so we dont need to pass for each one.
    return [
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product C", "price": 50, "stock": 10},
        {"name": "Product B", "price": 200, "stock": 3},
    ]

def test_sort_products_by_name_ascending(products):
    sorted_products = sort_products(products, "name", True)
    assert sorted_products == [
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product B", "price": 200, "stock": 3},
        {"name": "Product C", "price": 50, "stock": 10},
    ]


def test_sort_products_by_name_descending(products):
    sorted_products = sort_products(products, "name", False)
    assert sorted_products == [
        {"name": "Product C", "price": 50, "stock": 10},
        {"name": "Product B", "price": 200, "stock": 3},
        {"name": "Product A", "price": 100, "stock": 5},
    ]


def test_sort_products_by_price_ascending(products):
    sorted_products = sort_products(products, "price", True)
    assert sorted_products == [
        {"name": "Product C", "price": 50, "stock": 10},
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product B", "price": 200, "stock": 3},
    ]


def test_sort_products_by_price_descending(products):
    sorted_products = sort_products(products, "price", False)
    assert sorted_products == [
        {"name": "Product B", "price": 200, "stock": 3},
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product C", "price": 50, "stock": 10},
    ]


def test_sort_products_by_stock_ascending(products):
    sorted_products = sort_products(products, "stock", True)
    assert sorted_products == [
        {"name": "Product B", "price": 200, "stock": 3},
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product C", "price": 50, "stock": 10},
    ]

def test_sort_products_by_stock_descending(products):
    sorted_products = sort_products(products, "stock", False)
    assert sorted_products == [
        {"name": "Product C", "price": 50, "stock": 10},
        {"name": "Product A", "price": 100, "stock": 5},
        {"name": "Product B", "price": 200, "stock": 3},
    ]


def test_sort_products_invalid_key(products):
    # Redirect stdout to a string buffer
    sys.stdout = StringIO()
    sort_products(products, "invalid_key", True)
    # Reset stdout to normal
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    assert output == "Key not found in dictionary\n"
