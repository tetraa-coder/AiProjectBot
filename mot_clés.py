import discord
from discord.ext import commands
import spacy
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Charger le modèle de langue en français
nlp = spacy.load("fr_core_news_sm")

# Créer le client Discord
intents = discord.Intents.all()
client =commands.Bot(command_prefix="/", intents=intents, case_insensitive=True, self_bot=True)

# ID du canal cible pour l'analyse de mots-clés
canal_cible_id = 1227160818735517697  # Remplacez par l'ID du canal souhaité

# Fonction pour extraire les mots-clés d'un message
def extract_keywords(message_content):
    doc = nlp(message_content)
    # Collecter les mots-clés à partir des lemmes des tokens
    keywords = [token.lemma_ for token in doc if not token.is_stop and token.pos_ in ["NOUN", "PROPN"]]
    return keywords
# faire une fonction
@client.command(name="cannal")
async def cannal(context, cannal_repport):
    global cannal_cible_id
    cannal_cible_id = cannal_repport
    await context.send(f"cannal_repport:{cannal_cible_id}")
@client.event
async def on_message(message):
    # Vérifier que le message provient du canal cible
    if message.channel.id == canal_cible_id:
        log.debug("message")
        log.debug(f"client:{client}")   
        log.debug(f"message:{message}")
        if message.author.id == client.user:
            return
        # Extraire les mots-clés du contenu du message
        keywords = extract_keywords(message.content)
        #if keywords:
        # Envoyer les mots-clés extraits dans le canal
        #await message.channel.send(f"Mots-clés détectés : {', '.join(keywords)}")

        # Toujours appeler le comportement par défaut pour les événements on_message

        #await client.process_commands(message)

       # Remplacez 'YOUR_TOKEN_HERE' par votre propre jeton d'authentification
client.run("MTIyNzM5OTQwNTg1ODk3OTkyMw.GLPZjD.HV46_o-68jPSQHcx81a4OxLSXJaLay0iI6Jszg")
