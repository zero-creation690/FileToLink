from pyrogram import Client

# 🚀 Your credentials (already added)
api_id = 26091026
api_hash = "f608d185d836e0405775833c6888922f"
bot_token = "7546990711:AAHC8dfxPfzJqJ3LGbF8Yqg_vxTPWYemvac"

# 🧠 Create memory client and print session
client = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
client.start()

print("Session String:\n")
print(client.export_session_string())
