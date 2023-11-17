from Rabbit import rabbitdb
from Rabbit.Powers import remove_active_chat

# creating database code for clear command plugin
async def _clear_(chat_id):
    try:
        rabbitdb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
