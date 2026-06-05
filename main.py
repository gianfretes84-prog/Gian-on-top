import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Intents
import os
from dotenv import load_dotenv
from datetime import datetime

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurar intents
intents = Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

# Crear bot
bot = commands.Bot(command_prefix='!', intents=intents)

# ===== COLORES PARA EMBEDS =====
COLOR_ANUNCIO = discord.Color.blue()
COLOR_UPDATE = discord.Color.green()
COLOR_STATUS = discord.Color.purple()
COLOR_ERROR = discord.Color.red()

# ===== EVENTOS =====
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'✅ {len(synced)} comandos sincronizados')
    except Exception as e:
        print(f'❌ Error sincronizando comandos: {e}')

# ===== COMANDOS SLASH =====

@bot.tree.command(name="anuncio", description="Crea un anuncio profesional para el servidor")
@app_commands.describe(
    titulo="Título del anuncio",
    descripcion="Descripción o contenido del anuncio",
    imagen="Imagen para el anuncio (opcional)"
)
async def anuncio(
    interaction: discord.Interaction,
    titulo: str,
    descripcion: str,
    imagen: discord.Attachment = None
):
    """Comando para crear anuncios con texto e imágenes"""
    
    try:
        # Validar longitudes
        if len(titulo) > 256:
            await interaction.response.send_message(
                "❌ El título es demasiado largo (máximo 256 caracteres)",
                ephemeral=True
            )
            return
        
        # Crear embed
        embed = discord.Embed(
            title=f"📢 {titulo}",
            description=descripcion,
            color=COLOR_ANUNCIO,
            timestamp=datetime.now()
        )
        
        # Añadir imagen si se proporciona
        if imagen:
            # Validar que sea una imagen
            if not imagen.content_type.startswith('image/'):
                await interaction.response.send_message(
                    "❌ El archivo debe ser una imagen (PNG, JPG, GIF, etc.)",
                    ephemeral=True
                )
                return
            embed.set_image(url=imagen.url)
        
        # Añadir detalles profesionales
        embed.add_field(
            name="👤 Publicado por",
            value=interaction.user.mention,
            inline=True
        )
        embed.add_field(
            name="⏰ Fecha",
            value=f"<t:{int(datetime.now().timestamp())}:f>",
            inline=True
        )
        embed.set_footer(
            text=f"Gian-on-top | {interaction.guild.name}",
            icon_url=interaction.guild.icon.url if interaction.guild.icon else None
        )
        embed.set_author(
            name=interaction.user.name,
            icon_url=interaction.user.avatar.url if interaction.user.avatar else None
        )
        
        # Enviar anuncio
        await interaction.response.send_message(embed=embed)
        
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Error al crear el anuncio: {str(e)}",
            ephemeral=True
        )

@bot.tree.command(name="update", description="Publica una actualización del servidor")
@app_commands.describe(
    titulo="Título de la actualización",
    descripcion="Detalles de la actualización",
    imagen="Imagen para la actualización (opcional)"
)
async def update(
    interaction: discord.Interaction,
    titulo: str,
    descripcion: str,
    imagen: discord.Attachment = None
):
    """Comando para publicar actualizaciones con embeds profesionales"""
    
    try:
        # Validar longitudes
        if len(titulo) > 256:
            await interaction.response.send_message(
                "❌ El título es demasiado largo (máximo 256 caracteres)",
                ephemeral=True
            )
            return
        
        # Crear embed
        embed = discord.Embed(
            title=f"🔄 {titulo}",
            description=descripcion,
            color=COLOR_UPDATE,
            timestamp=datetime.now()
        )
        
        # Añadir imagen si se proporciona
        if imagen:
            # Validar que sea una imagen
            if not imagen.content_type.startswith('image/'):
                await interaction.response.send_message(
                    "❌ El archivo debe ser una imagen (PNG, JPG, GIF, etc.)",
                    ephemeral=True
                )
                return
            embed.set_image(url=imagen.url)
        
        # Añadir detalles profesionales
        embed.add_field(
            name="👤 Publicado por",
            value=interaction.user.mention,
            inline=True
        )
        embed.add_field(
            name="⏰ Fecha",
            value=f"<t:{int(datetime.now().timestamp())}:f>",
            inline=True
        )
        embed.set_footer(
            text=f"Gian-on-top | {interaction.guild.name}",
            icon_url=interaction.guild.icon.url if interaction.guild.icon else None
        )
        embed.set_author(
            name=interaction.user.name,
            icon_url=interaction.user.avatar.url if interaction.user.avatar else None
        )
        
        # Enviar actualización
        await interaction.response.send_message(embed=embed)
        
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Error al crear la actualización: {str(e)}",
            ephemeral=True
        )

@bot.tree.command(name="status", description="Muestra el estado actual del servidor")
@app_commands.describe(
    titulo="Título del estado",
    descripcion="Descripción del estado",
    imagen="Imagen para el estado (opcional)"
)
async def status(
    interaction: discord.Interaction,
    titulo: str,
    descripcion: str,
    imagen: discord.Attachment = None
):
    """Comando para reportar estado del servidor con embeds profesionales"""
    
    try:
        # Validar longitudes
        if len(titulo) > 256:
            await interaction.response.send_message(
                "❌ El título es demasiado largo (máximo 256 caracteres)",
                ephemeral=True
            )
            return
        
        # Crear embed
        embed = discord.Embed(
            title=f"✅ {titulo}",
            description=descripcion,
            color=COLOR_STATUS,
            timestamp=datetime.now()
        )
        
        # Añadir imagen si se proporciona
        if imagen:
            # Validar que sea una imagen
            if not imagen.content_type.startswith('image/'):
                await interaction.response.send_message(
                    "❌ El archivo debe ser una imagen (PNG, JPG, GIF, etc.)",
                    ephemeral=True
                )
                return
            embed.set_image(url=imagen.url)
        
        # Añadir detalles profesionales
        embed.add_field(
            name="👤 Reportado por",
            value=interaction.user.mention,
            inline=True
        )
        embed.add_field(
            name="⏰ Hora",
            value=f"<t:{int(datetime.now().timestamp())}:f>",
            inline=True
        )
        embed.add_field(
            name="👥 Miembros en línea",
            value=f"{len([m for m in interaction.guild.members if m.status != discord.Status.offline])} usuarios",
            inline=True
        )
        embed.set_footer(
            text=f"Gian-on-top | {interaction.guild.name}",
            icon_url=interaction.guild.icon.url if interaction.guild.icon else None
        )
        embed.set_author(
            name=interaction.user.name,
            icon_url=interaction.user.avatar.url if interaction.user.avatar else None
        )
        
        # Enviar estado
        await interaction.response.send_message(embed=embed)
        
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Error al crear el estado: {str(e)}",
            ephemeral=True
        )

# ===== EJECUTAR BOT =====
if __name__ == '__main__':
    if not TOKEN:
        print("❌ ERROR: DISCORD_TOKEN no configurado en .env")
        exit(1)
    
    print("🚀 Iniciando bot...")
    bot.run(TOKEN)
