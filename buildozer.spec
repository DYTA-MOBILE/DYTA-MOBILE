[app]

# (section) Title of your application
title = DYTA MUSICA

# (section) Package name
package.name = dytamusica

# (section) Package domain (needed for android packaging)
package.domain = org.dyta

# (section) Source code where the main.py live
source.dir = .

# (section) Source files to include (let's include everything)
source.include_exts = py,png,jpg,kv,atlas

# (section) Application version
version = 0.1

# (section) Application requirements
# Importante: Incluimos python3, kivy y yt-dlp
requirements = python3,kivy,yt-dlp

# (section) Supported orientations
orientation = portrait

# (section) Permissions
android.permissions = INTERNET

# (section) Android specific configurations
# Usamos la API 33 que es muy compatible actualmente
android.api = 33
android.minapi = 21
android.sdk = 33
# NDK estable para Python 3
android.ndk = 25b
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a

# (section) Icon of the application
icon.filename = dyta.png

# (section) Presplash of the application
# Si no tienes uno, usaremos el mismo icono
presplash.filename = dyta.png

# (section) Fullscreen mode
fullscreen = 0

# (section) Log level (2 = error only, 1 = info, 0 = debug)
log_level = 2

[buildozer]
# (section) Path to build artifacts
bin_dir = ./bin

# (section) Log level
log_level = 2

# (section) Display warning if buildozer is run as root
warn_on_root = 1
