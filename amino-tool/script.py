from BotAmino import BotAmino

print("wait...")
client = BotAmino()
client.prefix = "/" 
client.wait = 10  


def test(data):
    return data.authorId == ["your_user_id"]



@client.command("ping", test) 
def ping(data):
    data.subClient.send_message(data.chatId, message="pong!")


@client.command("pong")
def ping(data):
    if data.subClient.is_in_staff(data.authorId): 
        data.subClient.send_message(data.chatId, message="ping!")


@client.answer("hey")
def hello(data):
    data.subClient.send_message(data.chatId, message="Hey! Hey!")


@client.on_member_join_chat()
def say_hello(data):
    data.subClient.send_message(data.chatId, f"welcome here {data.author}!")


@client.on_member_leave_chat(["chatId"])
def say_goodbye(data):
    data.subClient.send_message(data.chatId, f"See you soon {data.author}!")



client.launch()
print("ready")
