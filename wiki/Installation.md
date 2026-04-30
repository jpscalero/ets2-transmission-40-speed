# Installation Guide / Guía de Instalación

[🇺🇸 English](#english) | [🇪🇸 Español](#espanol)

---

<a name="english"></a>
## 🇺🇸 English: Standard Installation

1.  **Download**: Navigate to the [Releases](../../releases) section and download the latest `.scs` file.
2.  **Locate Mod Folder**: Open your Windows Explorer and go to:
    `%USERPROFILE%\Documents\Euro Truck Simulator 2\mod`
3.  **Deploy**: Copy the `.scs` file into this folder.
4.  **Activate**: Launch ETS2, open the **Mod Manager**, and find "Antigravity 40-Speed Transmission Pack". Set it to **High Priority**.

---

<a name="espanol"></a>
## 🇪🇸 Español: Instalación Estándar

1.  **Descarga**: Ve a la sección de [Releases](../../releases) y descarga el archivo `.scs` más reciente.
2.  **Localizar Carpeta de Mods**: Abre el explorador de archivos y ve a:
    `%USERPROFILE%\Documents\Euro Truck Simulator 2\mod`
3.  **Despliegue**: Copia el archivo `.scs` en esta carpeta.
4.  **Activación**: Inicia ETS2, abre el **Gestor de Mods** y busca "Antigravity 40-Speed Transmission Pack". Dale **Prioridad Alta**.

---

## 🛠️ Developer / Source Build (Desarrolladores)

1.  **Clone**: `git clone https://github.com/jpscalero/ets2-transmission-40-speed.git`
2.  **Generate**: Run `python generator.py`.
3.  **Pack**: Use `python packer.py` to generate the `.scs` file automatically.

## ❓ Troubleshooting / Solución de Problemas

- **Mod not appearing? / ¿El mod no aparece?**: Verify that you are on v1.58. Check `game.log.txt`.
- **Physics Glitches? / ¿Física extraña?**: Ensure you are using an Antigravity-compatible engine mod.
