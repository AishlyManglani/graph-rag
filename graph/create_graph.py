from py2neo import Graph
from utils.entity_extractor import extract_triples

graph = Graph("bolt://localhost:7687", auth=("neo4j", "test1234"))


def create_graph_from_text(text):
    triples = extract_triples(text)
    for s, p, o in triples:
        graph.run(
            "MERGE (a:Entity {name:$s}) MERGE (b:Entity {name:$o}) MERGE (a)-[:RELATION {type:$p}]->(b)",
            s=s, o=o, p=p
        )