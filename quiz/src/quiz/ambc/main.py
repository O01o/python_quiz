from data import Edge

c1 = "C1"
c2 = "C2"
c3 = "C3"
c4 = "C4"

components: dict[str, bool] = {}
for c in [c1, c2, c3, c4]:
    flag: str = bool(int(input(f"{c}: ")))
    components[c] = flag
print(components.items())

edges: dict[str, Edge] = {
    "a": Edge(dst=c3),
    "b": Edge(dst=c1),
    "c": Edge(dst=c2),
    "d": Edge(src=c1, dst=c3),
    "e": Edge(src=c2, dst=c3),
    "f": Edge(src=c2, dst=c4),
    "g": Edge(src=c3),
    "h": Edge(src=c4),
}
print(edges.items())

for en, e in edges.items():
    if e.src:
        if not components[e.src]:
            edges[en].through = False
print(edges.items())