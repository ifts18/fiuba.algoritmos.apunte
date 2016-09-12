class Cola:
    """Representa a una cola, con operaciones de encolar y
       desencolar. El primero en ser encolado es también el primero
       en ser desencolado."""

    def __init__(self):
        """Crea una cola vacía."""
        self.items = []

    def encolar(self, x):
        """Agrega el elemento x como último de la cola."""
        self.items.append(x)

    def desencolar(self):
        """Desencola el primer elemento y devuelve su
           valor. Si la cola está vacía, levanta ValueError."""
		if self.esta_vacia():
			raise ValueError("La cola está vacía")
        return self.items.pop(0)

    def esta_vacia(self):
        """Devuelve True si la cola esta vacía, False si no."""
        return len(self.items) == 0
