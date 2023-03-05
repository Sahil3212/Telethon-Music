import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "22212114"))
    API_HASH = os.environ.get("API_HASH", "6b352d7fe8669980210a3bd308ac42ae")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6271479380:AAEJKRv8rxZmZVvtrJqItpJjJUeki2YtCu8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGoBux1_JMd0Z0evgUeH28pLXLLSHNrY7XpOnYC34rh8XxulIg_t76rRPUvpxkHJXz11fG0Wjzn8uhfq9YRqMLuzuyYat4kmskibX7iEk8U5rWhhbIlPO8MDTn6NpZ6D1utrS6MOH527LQEco9K0TpZWrIpX-UdUgjz_V2qO5LXifb152ze3zjoM5HNNA9OGjzQgOveVYoW5aHvc1R8TqOsAXIb97pNb9idPyhsS3giakjetsZRIjYu4HAoJqCHJKpT6kevm31qlr6sKnWYQ-rRjKk5haPFqc9vjoP9UaEx9wp2yh7BQz746dUrRR8VWtRIw-M6JXpjIj-1BHqoxBiY596M=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Rajput_music_player_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
