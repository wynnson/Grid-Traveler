from enum import StrEnum


class Status(StrEnum):
    U = "unvisited"
    V = "visited"
    E = "end"
    W = "wall"


class HeuristicCases(StrEnum):
    M = "manhattan"
    E = "euclidean"