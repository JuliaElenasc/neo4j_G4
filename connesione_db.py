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

# QUERY1: presentare la lista di tutte le piste in ordine di difficoltà 
query = " MATCH (p:Piste) RETURN p.piste, p.dificult ORDER BY p.dificult DESC" 
results = run_query(query)
print('LISTA DELLE PISTE IN ORDINE DI DIFFICOLTA')
print("---------------------------")
print(results)

# QUERY2: presentare la lista delle sole piste aperte
query = "MATCH (p:Piste {status: 'Opened'}) RETURN p.piste, p.status" 
results = run_query(query)
print('LISTA DELLE PISTE APERTE')
print("---------------------------")
print(results)


driver.close()