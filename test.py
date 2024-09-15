from bot import bot
from knowledge_hub  import knowledge

information = knowledge.query()
bot.ask(f'from the given information: {information}, who likes robotics?')

