#connessione DB
from neo4j import GraphDatabase

uri = "neo4j+s://d2c276b4.databases.neo4j.io:7687"
username = "neo4j"
password = "L4CE5ZVYRiDQeXruwwvdC_keJX6VJx9dYSW4DxN2mek"

driver = GraphDatabase.driver(uri, auth=(username, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()

# QUERY TEST
query = "MATCH (n) RETURN n " 
results = run_query(query)
print(results)

driver.close()