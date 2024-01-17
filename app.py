#connessione DB
from neo4j import GraphDatabase
import traceback
import pandas as pd
from tabulate import tabulate



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


while True:
    menu= int(input('''Sceglie una opzione:
                    1: Vedere piste in ordine di difficoltà
                    2: Vedere piste aperte
                    3. Cercare il miglior percorso
                    4: Uscire
                    scrive qui: '''))
    if menu ==1:
        # QUERY1: presentare la lista di tutte le piste in ordine di difficoltà 
        query = "MATCH (p:Piste)-[r:PATH]->() RETURN DISTINCT p.piste AS pista, r.difficolta AS dificult ORDER BY r.difficolta DESC" 
        results = run_query(query)
        print('LISTA DELLE PISTE IN ORDINE DI DIFFICOLTA')        
        headers = ['Pista', 'Difficoltà']
        rows = [(result['pista'], result['dificult']) for result in results]
        table = tabulate(rows, headers=headers, tablefmt='pretty')
        print(table)
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
        query_o="MATCH (p:Piste)RETURN p.piste;"
        risultato= run_query(query_o)
        nomi= [posto['p.piste'] for posto in risultato]
        for nome in sorted(nomi):
            print(nome)
        origine=input('Inserisci il nome del punto di partenza dalla lista precedente:')
        destino=input('incerisci il nome del punto di destinazione:')
        
        print(f'I percorsi migliore da {origine} a {destino} sono:')
        query= f"""
                MATCH percorso=(origin:Piste {{piste:'{origine}'}})-[:PATH*]-(destination:Piste {{piste:'{destino}'}})
                WHERE ALL(rel IN RELATIONSHIPS(percorso) WHERE rel.status = 'Opened')
                RETURN 
                    REDUCE(tempo = 0, tratta IN RELATIONSHIPS(percorso) | tempo + tratta.durata) AS tempototale, 
                    REDUCE(descrizione = '', piste IN NODES(percorso) | descrizione + '/' + piste.piste) AS piste 
                ORDER BY tempototale 
                LIMIT 5;
            """
        results = run_query(query)
        if results:
            headers = ['Tempo Totale', 'Descrizione']
            rows = [(result['tempototale'], result['piste']) for result in results]
            table = tabulate(rows, headers=headers, tablefmt='pretty')
            print(table)
        else: print('non ci sono routes disponibiles')
        input("Premi Enter per tornare al menu...")

    elif menu == 4:
        print('Grazie per la visita, arrivederci')
        break 

driver.close()