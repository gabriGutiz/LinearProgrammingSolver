
from enum import Enum

class LinProgVarTypes(Enum):
    BINARY = "Binary"
    INTEGER = "Integer"
    CONTINUOUS = "Continuous"

class LinProgOptimizations(Enum):
    MIN = -1
    MAX = 1
    EQUALS = 0

