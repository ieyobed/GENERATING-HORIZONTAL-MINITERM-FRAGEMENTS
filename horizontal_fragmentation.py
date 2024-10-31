from itertools import product
import mysql.connector

class PHorizontalFragmentation:
    def __init__(self, predicates):
        """
        Initializes the class with a list of predicates.
        """
        self.predicates = predicates

    def generate_miniterms(self):
        """
        Generates all possible combinations of predicates (miniterms).
        """
        combinations = product(*self.predicates)
        return [" AND ".join(comb) for comb in combinations]

    def query_database(self, host, user, password, database):
        """
        Queries the MySQL database using each miniterm as a WHERE condition.
        """
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        results = {}
        miniterms = self.generate_miniterms()
        for miniterm in miniterms:
            query = f"SELECT * FROM sales_transactions WHERE {miniterm}"
            cursor.execute(query)
            results[miniterm] = cursor.fetchall()

        cursor.close()
        conn.close()
        return results
