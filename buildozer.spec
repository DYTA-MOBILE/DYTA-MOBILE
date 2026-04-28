[app]

# (section) Title of your application
title = DYTA MUSICA

# (section) Package name
package.name = dytamusica

# (section) Package domain
package.domain = org.dyta

# (section) Source code where the main.py live
source.dir = .

# (section) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (section) Application version
# Cambiado a 1.0 para evitar problemas con el punto decimal inicial
version = 1.0

# (section) Application requirements
# AGREGADO: certifi y openssl son obligatorios para conectar yt-dlp a internet
requirements = python3,kivy,yt-dlp,certifi,openssl

# (section) Supported orientations
orientation = portrait

# (section) Permissions
android.permissions = INTERNET

# (section) Android specific configurations
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a

# (section) Icon of the application
icon.filename = dyta.png

# (section) Presplash of the application
presplash.filename = dyta.png

# (section) Fullscreen mode
fullscreen = 0

# (section) Log level (Asegúrate de que no haya espacios extra o ceros iniciales)
log_level = 2

[buildozer]
# (section) Path to build artifacts
bin_dir = ./bin

# (section) Log level
log_level = 2

# (section) Display warning if buildozer is run as root
warn_on_root = 1
