#Bot Discord d'Analyse de Sentiments avec ChatGPT

Ce bot Discord utilise l'analyse de sentiments pour détecter les émotions des messages des utilisateurs dans un canal spécifique. Le bot répond ensuite en conséquence avec des messages appropriés. De plus, il utilise ChatGPT pour interpréter les résultats des analyses de sentiments.

#Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre système :

##Python 3.x
##discord.py


#Installation

Clonez ce dépôt sur votre machine locale :

##bash
##Copy code
git clone https://github.com/votre-utilisateur/le_lien_de_notre_depot

##Téléchargez les dépendances Python en exécutant la commande suivante dans le terminal :
##bash
Copy code
pip install -r requirements.txt


#Configuration

Ouvrez le fichier boot.py et remplacez "YOUR_TOKEN_HERE" par le token de votre bot Discord. (on a tout mis dans le meme fichier , pas besoin de faire l'appel au fichier qui se trouve dans le folder private)

Ouvrez le fichier mots_cles.py et ajoutez/modifiez les mots-clés que vous souhaitez utiliser pour détecter les sujets spécifiques dans les messages des utilisateurs.

#Utilisation

Exécutez le fichier boot.py pour démarrer le bot Discord. Vous pouvez le faire en utilisant la commande suivante dans le terminal :

##bash
##Copy code
python boot.py

Une fois que le bot est en ligne, il écoute les messages dans le canal spécifié. Il analysera le sentiment de chaque message et répondra en conséquence.

Vous pouvez modifier le comportement du bot en ajustant les règles dans le fichier boot.py et les mots-clés dans le fichier mots_cles.py.

Pour interpréter les résultats des analyses de sentiments, exécutez le fichier chatgpt.py et suivez les instructions pour saisir un message et voir l'interprétation.
