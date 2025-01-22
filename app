import time
import threading
from mc import MinecraftBot

def create_bot(username, server_ip):
    bot = MinecraftBot(username, server_ip, port=25565, offline=True)

    try:
        bot.connect()
        print(f"Bot '{username}' has successfully logged in!")
    except Exception as e:
        print(f"Error: {e}")
        return

    def listen_for_chat():
        while True:
            try:
                message = bot.read_chat()
                if message:
                    print(f"[{message['sender']}] {message['message']}")
            except Exception as e:
                print(f"Error listening to chat: {e}")
                break

    chat_thread = threading.Thread(target=listen_for_chat)
    chat_thread.daemon = True
    chat_thread.start()

    while True:
        user_input = input(f"{username}> ")
        if user_input:
            if user_input.lower() == "#stop":
                bot.chat("Bot is disconnecting.")
                bot.disconnect()
                break
            else:
                bot.chat(user_input)
        time.sleep(0.1)

def main():
    print("Minecraft Offline Bot")
    server_ip = input("Enter the server IP: ")
    username = input("Enter the username: ")
    
    create_bot(username, server_ip)

if __name__ == "__main__":
    main()
