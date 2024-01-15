#connessione DB
from neo4j import GraphDatabase
import traceback
import pandas as pd


uri = "neo4j+s://d2c276b4.databases.neo4j.io:7687"
username = "neo4j"
password = "L4CE5ZVYRiDQeXruwwvdC_keJX6VJx9dYSW4DxN2mek"

driver = GraphDatabase.driver(uri, auth=(username, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()


#Inizio dalla App
print('----------------------------------------------------')
print('----------------------------------------------------')
print('Benvenuto alla app per sciatori, scegli una opzione:')
print('1. Vedere piste in ordine di difficoltà')
print('2. Vedere piste aperte')
print('3. Cercare il miglior percorso')
print('4. Uscire')


while True:
    menu= int(input('inserisci il numero dalla opzione (1,2,3 o 4):'))
    if menu ==1:
        # QUERY1: presentare la lista di tutte le piste in ordine di difficoltà 
        query = "MATCH (p:Piste)-[r:PATH]->() RETURN p.piste AS pist, r.difficolta AS dificult ORDER BY r.difficolta DESC" 
        results = run_query(query)
        print('LISTA DELLE PISTE IN ORDINE DI DIFFICOLTA')
        print("---------------------------")
        print(results)
        input("Premi Enter per tornare al menu...")
    elif menu==2:
        # QUERY2: presentare la lista delle sole piste aperte
        query = "MATCH (p:Piste {status: 'Opened'}) RETURN p.piste, p.status" 
        results = run_query(query)
        print('LISTA DELLE PISTE APERTE')
        print("---------------------------")
        for result in results:
            print(f"Pista: {result['p.piste']}, Stato: {result['p.status']}")

        input("Premi Enter per tornare al menu...")
            
    elif menu==3:
        print('opzione in lavoro')
        input("Premi Enter per tornare al menu...")

    elif menu == 4:
        print('Grazie per la visita, arrivederci')
        break 

driver.close()