import sys
import random
random.seed()

max_count = int(sys.argv[1])

incoming_edges_count = random.randint(1,6)
outcoming_edges_count = random.randint(1,6)

incoming_edges = set([(random.randint(1, max_count), max_count) for i in range(1, incoming_edges_count + 1)])
outcoming_edges = set([(max_count, random.randint(1, max_count)) for i in range(1, outcoming_edges_count + 1)])

edges = incoming_edges.union(outcoming_edges)
edges_selects = list(map(lambda edge: "SELECT {} AS first, {} AS second ".format(edge[0], edge[1]), edges))

edges_query_part = "({})".format(" UNION ".join(edges_selects))

whole_query = "INSERT INTO link (id_from, id_to) SELECT * FROM {} AS edge WHERE NOT EXISTS (SELECT * FROM link WHERE link.id_from = edge.first AND link.id_to = edge.second);".format(edges_query_part)

print(whole_query)
