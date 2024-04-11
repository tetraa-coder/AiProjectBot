import discord
import openai
import os
import time
from flask import Flask, render_template, request, redirect

# Set the OpenAI API key
openai.api_key = "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"

# Define the name of the bot
name = 'BOT'
role = 'customer service'
impersonated_role = f"""
    From now on, you are going to act as {name}. Your role is {role}.
    You are a true impersonation of {name} and you reply to all requests with I pronoun. You never give unknown information.
    Forward them to the website for more information.
    YOU ARE NOT AN AI MODEL!
"""

# Initialize variables
chat_history = ''

# Initialize Flask app
app = Flask(__name__)

# Initialize Discord bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Function to complete chat input using OpenAI's GPT-3.5 Turbo
def chat_completion(user_input):
    global chat_history
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": f"{impersonated_role}. Conversation history: {chat_history}"},
            {"role": "user", "content": user_input},
        ]
    )
    return output['choices'][0]['message']['content']

# Fonction pour analyser un message à la recherche de harcèlement
def detect_harassment(message):
    prompt = f"Detect harassment in the following message: {message}"
    output = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.0,
    )
    return output.choices[0].text.strip()

# Fonction pour gérer les messages des utilisateurs
def handle_user_message(message):
    user_input = message.content
    harassment_analysis = detect_harassment(user_input)
    response = f"**Message**: {user_input}\n\n**Harassment Analysis**: {harassment_analysis}"
    return response

# Function to handle user chat input
def handle_user_message(message):
    global chat_history
    user_input = message.content
    chat_history += f'\nUser: {user_input}\n'
    bot_response = chat_completion(user_input)
    chat_history += f'{name}: {bot_response}\n'
    return bot_response

# Define Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return get_response(user_text)

@app.route('/refresh')
def refresh():
    time.sleep(600)  # Wait for 10 minutes
    return redirect('/refresh')

# Discord bot events
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/chat'):
        user_input = message.content[len('/chat'):].strip()
        response = handle_user_message(user_input)
        await message.channel.send(response)

# Run the Discord bot and Flask app
if __name__ == "__main__":
    client.run("MTIyNzM5OTQwNTg1ODk3OTkyMw.G5NQMd.-GlDKGXVA0FyKLmxPA4gVXegJEZYkHTn8ryjTc")
