## Voorbereiding_Algo_-DS_examen

## links
Link repo lessen:
https://github.com/UGent-AlgoData-BusinessEngineering/Code_lectures_2526


## class builed in functions:

<p>Object Lifecycle & Representation:
__init__(self) – Initialize instance.
__new__(cls) – Create instance (before __init__).
__str__(self) – User-friendly string (for print()).
__repr__(self) – Developer representation.
</p>

<p>Attribute Handling:
__getattr__(self, name) – Called only if attribute not found.
__getattribute__(self, name) – Called for every attribute access.
__setattr__(self, name, value) – When setting an attribute.
__delattr__(self, name) – When deleting an attribute.
</p>

<p>Callable:
__call__(self) – Makes an object callable like a function.</p>

<p>Container Protocol:
__len__(self) – len(obj)
__getitem__(self, key) – obj[key]
__setitem__(self, key, value) – obj[key] = value
__delitem__(self, key) – del obj[key]
__iter__(self) – Iterator start.
__next__(self) – Iterator step.
__contains__(self, item) – item in obj</p>

<p>Comparisons:
__eq__(self, other) → ==
__ne__(self, other) → !=
__lt__(self, other) → <
__le__(self, other) → <=
__gt__(self, other) → >
__ge__(self, other) → >=</p>

<p>Arithmetic:
__add__(self, other) → +
__sub__(self, other) → -
__mul__(self, other) → *
__truediv__(self, other) → /</p>

<p>Context Managers:
__enter__(self) – Enter with block.
__exit__(self, exc_type, exc_val, exc_tb) – Exit with block.</p>
