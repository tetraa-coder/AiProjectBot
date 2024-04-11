
import discord
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import logging
 
# Téléchargement des ressources nécessaires pour nltk
nltk.download('vader_lexicon')

# Initialisation du module logging
logging.basicConfig(
    level=logging.INFO,  # Niveau global de journalisation (par exemple, INFO)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format du message de journalisation
)
 
# Initialisation de l'analyseur de sentiment
sia = SentimentIntensityAnalyzer()
 
# Création du client Discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

#ID du canal cible ou le boot doit envoyer le message
Canal_cible_id = 1227160818735517697

# Fonction pour déterminer le sentiment d'un message
def get_sentiment(message):
    scores = sia.polarity_scores(message)
    if scores['compound'] >= 0.05:
        return 'positif'
    elif scores['compound'] <= -0.05:
        return 'négatif'
    else:
        return 'neutre'
 
# Événement déclenché lorsque le bot est prêt
@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')
 
# Événement déclenché lorsqu'un message est reçu
@client.event
async def on_message(message):
    logging.info(f"Message reçu dans le canal {message.channel.name}: {message.content}")

    # Ne répondez pas aux messages du bot lui-même
    if message.author == client.user:
        return

    # Vérifier si le message a été envoyé dans le canal cible
    if message.channel.id == Canal_cible_id:
        logging.info("Message reçu dans le canal cible.")

        # Analyse du sentiment du message
        sentiment = get_sentiment(message.content)
 
        # Réponse en fonction du sentiment
        if sentiment == 'positif':
            await message.channel.send('C\'est génial que vous soyez de bonne humeur !')
        elif sentiment == 'négatif':
            await message.channel.send('Je suis désolé que vous ne vous sentiez pas bien. Besoin de parler ?')
        else:
            await message.channel.send('C\'est un message neutre.')
    else:
        logging.info("Message reçu dans un autre canal.")

# Remplacez 'YOUR_TOKEN_HERE' par votre propre jeton d'authentification
client.run("MTIyNzM5OTQwNTg1ODk3OTkyMw.GzPwtD.jnVEDbbeJFHKPV7T-Yyq7mbzjgmMcAycSdYhjs")

