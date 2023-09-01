import sqlite3

conn = sqlite3.connect('guild_settings.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS guild (
        guild_id INT PRIMARY KEY,
        welcome_channel_id INT,
        welcome_message VARCHAR(255)
    )
''')
               

def setGuildWelcome(guildid : int, channelid : int, message : str):
    cursor.execute('''
        INSERT OR REPLACE INTO guild(guild_id, welcome_channel_id, welcome_message)
        VALUES(?, ?, ?)
    ''', (guildid, channelid, message))
    conn.commit()

def getGuildWelcome(guildid : int) -> tuple:
    cursor.execute('''
        SELECT welcome_channel_id, welcome_message
        FROM guild
        WHERE guild_id = ?
    ''', (guildid,))
    result = cursor.fetchone()
    if result == None:
        return None, None
    return result
