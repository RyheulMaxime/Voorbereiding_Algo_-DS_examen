## Voorbereiding_Algo_-DS_examen

## links
Link repo lessen:
https://github.com/UGent-AlgoData-BusinessEngineering/Code_lectures_2526


## class builed in functions:

<h3>Object Lifecycle & Representation:</h3>
<p>__init__(self) – Initialize instance.</p>
<p>__new__(cls) – Create instance (before __init__).</p>
<p>__str__(self) – User-friendly string (for print()).</p>
<p>__repr__(self) – Developer representation.</p>

<h3>Attribute Handling:</h3>
<p>__getattr__(self, name) – Called only if attribute not found.</p>
<p>__getattribute__(self, name) – Called for every attribute access.</p>
<p>__setattr__(self, name, value) – When setting an attribute.</p>
<p>__delattr__(self, name) – When deleting an attribute.</p>

<h3>Callable:</h3>
<p>__call__(self) – Makes an object callable like a function.</p>

<h3>Container Protocol:</h3>
<p>__len__(self) – len(obj)</p>
<p>__getitem__(self, key) – obj[key]</p>
<p>__setitem__(self, key, value) – obj[key] = value</p>
<p>__delitem__(self, key) – del obj[key]</p>
<p>__iter__(self) – Iterator start.</p>
<p>__next__(self) – Iterator step.</p>
<p>__contains__(self, item) – item in obj</p>

<h3>Comparisons:</h3>
<p>__eq__(self, other) → ==</p>
<p>__ne__(self, other) → !=</p>
<p>__lt__(self, other) → <</p>
<p>__le__(self, other) → <=</p>
<p>__gt__(self, other) → ></p>
<p>__ge__(self, other) → >=</p>

<h3>Arithmetic:</h3>
<p>__add__(self, other) → +</p>
<p>__sub__(self, other) → -</p>
<p>__mul__(self, other) → *</p>
<p>__truediv__(self, other) → /</p>

<h3>Context Managers:</h3>
<p>__enter__(self) – Enter with block.</p>
<p>__exit__(self, exc_type, exc_val, exc_tb) – Exit with block.</p>
