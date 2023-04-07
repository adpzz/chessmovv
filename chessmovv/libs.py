"""
Parte de las funciones de chessmovv
Aquí se encuentran clases de las diferentes fichas del ajedrez

Fichas disponibles
    - Reina
    - Rey
    - Torre

** Pendiente icluir las demás fichas **
"""

class Queen:
    def __init__(self, fila_inicial: int, columna_inicial: int) -> None:
        """
        Inicializa una instancia de la clase Queen.

        Args:
            fila_inicial (int): Fila inicial de la reina.
            columna_inicial (int): Columna inicial de la reina.
        """
        self.fila = fila_inicial
        self.columna = columna_inicial

    def validar_movimiento(self, fila_final: int, columna_final: int) -> int:
        """
        Verifica si un movimiento de la reina es válido.

        Args:
            fila_final (int): Fila final del movimiento.
            columna_final (int): Columna final del movimiento.

        Returns:
            int: 1 si el movimiento es válido, 0 si no lo es.
        """

        # verificar si el movimiento está dentro de las dimensiones del tablero (8x8)
        if self.fila < 1 or self.fila > 8 or self.columna < 1 or self.columna > 8 \
            or fila_final < 1 or fila_final > 8 or columna_final < 1 or columna_final > 8:
            return 0
    
        # verificar si la reina se mueve horizontalmente o verticalmente
        if self.fila == fila_final or self.columna == columna_final:
            return 1
    
        # verificar si la reina se mueve diagonalmente
        if abs(self.fila - fila_final) == abs(self.columna - columna_final):
            return 1
    
        # si la reina no se mueve horizontal, vertical o diagonalmente, el movimiento es inválido
        return 0
    
class King:
    def __init__(self, fila_inicial: int, columna_inicial: int) -> None:
        """
        Inicializa una instancia de la clase King.

        Args:
            fila_inicial (int): Fila inicial del rey.
            columna_inicial (int): Columna inicial del rey.
        """
        self.fila = fila_inicial
        self.columna = columna_inicial

    def validar_movimiento(self, fila_final: int, columna_final: int) -> int:
        """
        Verifica si un movimiento del rey es válido.

        Args:
            fila_final (int): Fila final del movimiento.
            columna_final (int): Columna final del movimiento.

        Returns:
            int: 1 si el movimiento es válido, 0 si no lo es.
        """
        # verificar si el movimiento está dentro de las dimensiones del tablero (8x8)
        if self.fila < 1 or self.fila > 8 or fila_final < 1 or fila_final > 8 \
            or self.columna < 1 or self.columna > 8 or columna_final < 1 or columna_final > 8:
            return 0
        
        # Verificar si la distancia es de 1 o menos en ambas direcciones
        if abs(fila_final - self.fila) <= 1 and abs(columna_final - self.columna) <= 1:
            return 1
        
        return 0
        
class Tower:
    def __init__(self, fila_inicial: int, columna_inicial: int) -> None:
        """
        Inicializa una instancia de la clase Tower.

        Args:
            fila_inicial (int): Fila inicial de la torre.
            columna_inicial (int): Columna inicial de la torre.
        """
        self.fila = fila_inicial
        self.columna = columna_inicial

    def validar_movimiento(self, fila_final: int, columna_final: int) -> int:
        """
        Verifica si un movimiento de la torre es válido.

        Args:
            fila_final (int): Fila final del movimiento.
            columna_final (int): Columna final del movimiento.

        Returns:
            int: 1 si el movimiento es válido, 0 si no lo es.
        """
        # verificar si el movimiento está dentro de las dimensiones del tablero (8x8)
        if not (1 <= self.fila <= 8) or not (1 <= self.columna <= 8) \
            or not (1 <= fila_final <= 8) or not (1 <= columna_final <= 8):
            return 0
        
        # Validar si la torre se mueve a lo largo de la fila o columna en la que se encuentra
        if self.fila == fila_final or self.columna == columna_final:
            return 1
        
        # En cualquier otro caso, el movimiento es inválido
        return 0