OpenCVODOS
==========

Repositorio para el Plugin de procesado visual (OpenCV) en OpenDomo OS

El proyecto consiste en el desarrollo de un plugin que permita usar el sistema de procesado de imagen OpenCV desde OpenDomo OS, abriendo la posibilidad a la futura incorporación de plugins y filtros específicos (reconocimiento facial, detección de movimiento, etc).

Instalación
===========

$ plugin_add_from_gh.sh alherca OpenCVODOS

Filtros
=======
circle = Filtro de prueba para detectar circulos.

facedet = Detecta rostros en una imagen generada en alguna cámara del sistema.

motiondet = Detecta movimiento en una cámara, comparando 2 imagenes.

persons = Detecta personas en una imagen generada en alguna cámara del sistema.

