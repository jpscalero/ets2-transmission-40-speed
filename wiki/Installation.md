# Guía de Instalación y Despliegue

Esta guía cubre todo, desde la instalación básica del mod hasta las builds de código fuente avanzadas para el proyecto Antigravity.

## 📥 Método 1: Instalación Estándar (Recomendado)

1.  **Descarga**: Ve a la sección de [Releases](../../releases) y descarga el archivo `.scs` más reciente.
2.  **Localizar Carpeta de Mods**: Abre el explorador de archivos de Windows y ve a:
    `%USERPROFILE%\Documents\Euro Truck Simulator 2\mod`
3.  **Despliegue**: Copia el archivo `.scs` en esta carpeta.
4.  **Activación**:
    - Inicia ETS2.
    - Abre el **Gestor de Mods**.
    - Busca "Antigravity 40-Speed Transmission Pack".
    - Haz clic en la flecha para activar y asegúrate de que tenga **Prioridad Alta** (arriba en la lista).

## 🛠️ Método 2: Build para Desarrolladores

Si deseas modificar la lista de camiones o los ratios de marcha tú mismo, sigue estos pasos:

1.  **Requisitos**: Instala [Python 3.x](https://www.python.org/).
2.  **Clonar**: `git clone https://github.com/jpscalero/ets2-transmission-40-speed.git`
3.  **Generar**:
    - Abre una terminal en el directorio del proyecto.
    - Ejecuta `python generator.py`.
    - Esto creará un directorio `mod_files` con la estructura `/def` actualizada.
4.  **Empaquetar**:
    - Usa una herramienta como 7-Zip o WinRAR.
    - Selecciona el **contenido** de la carpeta `mod_files`.
    - Añade al archivo, elige el formato **ZIP** y el nivel de compresión **Almacenar** (Sin compresión).
    - Cambia el nombre de `.zip` a `.scs`.

## ❓ Solución de Problemas

- **¿El mod no aparece?** Verifica que estés en la v1.58. Revisa el archivo `game.log.txt` para buscar errores de "Entry point not found".
- **¿Física extraña?** Asegúrate de usar un mod de motor compatible con Antigravity. Los motores estándar pueden tardar mucho en cambiar con 40 marchas.

Para más ayuda, abre un [Reporte de Error](../../issues).
