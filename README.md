# cheessmovv

### Verificación de movimiento de piezas de ajedrez
*Nota: este verificador no considera si hay piezas en la trayectoria o en el origen/destino.*


Este es un módulo de Python que permite verificar si los movimientos de las piezas del ajedrez son válidos o no. 

## Instalación

Para instalar el módulo desde el código fuente, sigue los siguientes pasos:

Clona el repositorio desde GitHub:

```bash
$ git clone https://github.com/adpzz/chessmovv.git
```
Entra en el directorio del proyecto:

```bash
$ cd cheessmovv
```

Instala el módulo usando:

```bash
$ python setup.py install
```
## Uso

A continuación te presentamos un ejemplo de uso

```python
import chessmovv as chm

reina = chm.Queen(8, 8)

if reina.validar_movimiento(4, 8):
  print("Movimiento válido")
else:
  print("Movimiento inválido")
```

## Contribuir

Si deseas contribuir a este proyecto, puedes hacer lo siguiente:

1. Hacer un fork del repositorio
2. Crear una nueva rama con tus cambios: `git checkout -b mi-cambio`
3. Realizar tus cambios y hacer commit: `git commit -am 'Agregué una nueva función'`
4. Hacer push a la rama: `git push origin mi-cambio`
5. Crear un pull request en GitHub
