import unittest
import pandas as pd

# import all the defined functions from the 'main.py' file
from main import (
    read_data,
    revenue_per_month,
    revenue_per_product,
    revenue_per_customer,
    top_10_customers,
)


class TestOnlineStore(unittest.TestCase):
    def setUp(self):
        # Set up the test case with sample data, just took small cases with approx. five attributes
        data = {
            "order_id": [1, 2, 3, 4, 5],
            "customer_id": [101, 102, 101, 103, 102],
            "order_date": [
                "2023-01-10",
                "2023-02-15",
                "2023-01-20",
                "2023-03-10",
                "2023-02-25",
            ],
            "product_id": [1001, 1002, 1003, 1001, 1002],
            "product_name": [
                "Product A",
                "Product B",
                "Product C",
                "Product A",
                "Product B",
            ],
            "product_price": [10, 20, 30, 10, 20],
            "quantity": [1, 2, 3, 1, 2],
        }
        self.data = pd.DataFrame(data)
        self.data["order_date"] = pd.to_datetime(
            self.data["order_date"]
        )  # converts the strings to panda's datetime format just as mentioned in the other files of the project
        self.data["total_price"] = (
            self.data["product_price"] * self.data["quantity"]
        )  # calculates the total price i.e product price*quantity

    def test_revenue_per_month(self):
        # Test the revenue_per_month function.
        # the expected values for the revenue per month are calculated manually,
        # Expected Revenue for January 2023:
        # Order 1: 10 * 1 = 10
        # Order 3: 30 * 3 = 90
        # Total: 10 + 90 = 100

        # Expected Revenue for February 2023:
        # Order 2: 20 * 2 = 40
        # Order 5: 20 * 2 = 40
        # Total: 40 + 40 = 80

        # Expected Revenue for March 2023:
        # Order 4: 10 * 1 = 10
        # Total: 10

        result = revenue_per_month(self.data)
        expected = pd.Series(
            [100, 80, 10],  #
            index=pd.PeriodIndex(["2023-01", "2023-02", "2023-03"], freq="M"),
            # frequency is set to 'M' as the the index must be interpreted as monthly periods.
        )
        # creating a seperate series of the expected outcome, and using the pandas 'assert' to check if the functions output is matching with the expected values
        pd.testing.assert_series_equal(result, expected, check_names=False)
        # THOUGHT PROCESS : I did face the error at the start because it was checking and comparing the names too, as the names can be 'None' too i was getting error, which is why the 'check_names' is set to False.

    def test_revenue_per_product(self):
        # Test the revenue_per_product function.
        # the expected values for the revenue per product are calculated manually,
        # Expected Revenue per Product:
        # Product A:
        # Order 1: 10 * 1 = 10
        # Order 4: 10 * 1 = 10
        # Total: 10 + 10 = 20

        # Product B:
        # Order 2: 20 * 2 = 40
        # Order 5: 20 * 2 = 40
        # Total: 40 + 40 = 80

        # Product C:
        # Order 3: 30 * 3 = 90
        # Total: 90

        result = revenue_per_product(self.data)
        expected = pd.Series(
            [20, 80, 90],
            index=pd.Index(["Product A", "Product B", "Product C"]),
        )
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_revenue_per_customer(self):
        # Test the revenue_per_customer function.
        # the expected values for the revenue per customer are calculated manually,
        # Expected Revenue per customer:
        # Customer 101:
        # Order 1: 10 * 1 = 10
        # Order 3: 30 * 3 = 90
        # Total: 10 + 90 = 100

        # Customer 102:
        # Order 2: 20 * 2 = 40
        # Order 5: 20 * 2 = 40
        # Total: 40 + 40 = 80

        # Customer 103:
        # Order 4: 10 * 1 = 10
        # Total: 10

        result = revenue_per_customer(self.data)
        expected = pd.Series([100, 80, 10], index=pd.Index([101, 102, 103]))
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_top_10_customers(self):
        # Test the top_10_customers function.

        result = top_10_customers(self.data)
        expected = pd.Series([100, 80, 10], index=pd.Index([101, 102, 103]))
        pd.testing.assert_series_equal(result, expected, check_names=False)


if __name__ == "__main__":
    unittest.main()
