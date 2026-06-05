# Gian-on-top - Discord Bot 🎮

Bot de Discord profesional para gestionar anuncios y actualizaciones con soporte de imágenes e embeds personalizados.

## 📋 Características

- **Comando `/anuncio`** - Crea anuncios con texto e imágenes
- **Comando `/update`** - Publica actualizaciones con detalles visuales
- **Comando `/status`** - Reporta el estado del servidor con embeds profesionales
- **Embeds personalizados** - Diseño profesional con colores y campos organizados
- **Soporte de imágenes** - Sube y muestra imágenes en los mensajes

## 🚀 Instalación Rápida

### Requisitos
- Python 3.10+
- Token de Discord Bot

### Local Setup
```bash
# Clonar repositorio
git clone https://github.com/gianfretes84-prog/Gian-on-top.git
cd Gian-on-top

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
echo "DISCORD_TOKEN=tu_token_aqui" > .env

# Ejecutar bot
python main.py
```

## 🔧 Configuración

1. **Crear Bot en Discord Developer Portal**
   - Ve a https://discord.com/developers/applications
   - Click en "New Application"
   - Ve a "Bot" y click "Add Bot"
   - Copia el TOKEN

2. **Invitar Bot a tu Servidor**
   - En OAuth2 > URL Generator selecciona:
     - `bot`
     - `applications.commands`
   - Permisos: `Send Messages`, `Embed Links`, `Attach Files`, `Read Messages/View Channels`
   - Copia la URL generada y abre en tu navegador

3. **Configurar Token**
   - Crea archivo `.env` en la raíz
   - Añade: `DISCORD_TOKEN=tu_token`

## 📝 Comandos Disponibles

### `/anuncio`
Crea un anuncio profesional
```
/anuncio título:"Mi Anuncio" descripción:"Contenido del anuncio" imagen:(opcional)
```

### `/update`
Publica una actualización
```
/update título:"Actualización" descripción:"Detalles de la actualización" imagen:(opcional)
```

### `/status`
Muestra el estado del servidor
```
/status título:"Estado" descripción:"Detalles del estado" imagen:(opcional)
```

## 🌐 Deploy a Railway.app

1. **Crear cuenta en Railway.app**
   - Ve a https://railway.app
   - Regístrate con GitHub

2. **Conectar Repositorio**
   - Dashboard > New Project > GitHub Repo
   - Selecciona tu repositorio

3. **Configurar Variables de Entorno**
   - En "Variables" añade:
   - `DISCORD_TOKEN` = tu_token

4. **Deploy Automático**
   - Railway detectará `requirements.txt`
   - Ejecutará `python main.py` automáticamente

## 📦 Estructura del Proyecto

```
Gian-on-top/
├── main.py              # Punto de entrada del bot
├── requirements.txt     # Dependencias Python
├── .env                 # Variables de entorno (NO COMMITAR)
├── .env.example         # Ejemplo de variables
├── .gitignore          # Archivos ignorados
├── Procfile            # Configuración para hosting
└── README.md           # Este archivo
```

## 🔐 Seguridad

- **NUNCA** compartas tu token de Discord
- Usa archivo `.env` para variables sensibles
- El `.gitignore` previene commits accidentales

## 📞 Soporte

Para reportar bugs o sugerencias, abre un issue en el repositorio.

---

**Bot creado con ❤️ usando discord.py**
