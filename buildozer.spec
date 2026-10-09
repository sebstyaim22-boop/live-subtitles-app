[app]

# Nombre de tu aplicación
title = Live Subtitles Gemini
package.name = livesubtitles
package.domain = org.test

# Archivos de código fuente a incluir
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versión
version = 0.1

# Dependencias requeridas en Python
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,urllib3,chardet,certifi,idna

# Permisos requeridos en Android
android.permissions = INTERNET, RECORD_AUDIO, SYSTEM_ALERT_WINDOW

# Orientación de la pantalla
orientation = portrait

# Ajustes de Android SDK / NDK
fullscreen = 0
android.archs = arm64-v8a

[buildozer]

# Nivel de detalle en la consola de compilación (2 = detallado)
log_level = 2
warn_on_root = 1