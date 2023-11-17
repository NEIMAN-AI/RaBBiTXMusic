from Rabbit import rabbitdb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = rabbitdb.get(chat_id)
    if get:
        rabbitdb[chat_id].append(put_f)
    else:
        rabbitdb[chat_id] = []
        rabbitdb[chat_id].append(put_f)
