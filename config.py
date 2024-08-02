from os import getenv

class Config(object):
      API_HASH = getenv("dbf930927f239982765d29cf6cb9a579")
      API_ID = int(getenv("12557431", 0))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "7029065576:AAHReOT0L-nZDYdB2nlrqbRHkmfKVwZwYek")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-2159055946:-2185890867").replace("\n", "").split(' '))
