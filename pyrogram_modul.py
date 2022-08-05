from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime


app = Client(
    "MentionAll",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)




@chatbot_cmd("broadcast", is_args=True)
@god_only
async def sedlyfsir(event):
    msgtobroadcast = event.text
    msgtobroadcast = msgtobroadcast[9:]
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            await chatbot.send_message(int(starkcast.chat_id), msgtobroadcast)
        except Exception as e:
            error_count += 1
    sent_count = error_count - len(userstobc)
    await chatbot.send_message(
        event.chat_id,
        f"<b>Broadcast Done in <u>{sent_count}</u> Group/Users and I got <u>{error_count}</u> Error and Total Number Was <u>{len(userstobc)}</u></b>",
        parse_mode="HTML"
    )
    await chatbot.send_message(Config.DUMB_CHAT, f"You BroadCasted A New Message. \nMessage - {msgtobroadcast} \nSent Count - {sent_count}")








#@app.on_message(filters.command("start"))
#async def _py(client: Client, message: Message):
   # await message.reply_text('Pyrogram is a Python library for Telegram bots.')

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər⚡️` \n\n **🤖Qruplardakı Userləri Tag Edmə üçün Yaradıldım.\n🤖Kömək üçün /help yazmaq kifayətdir.✨**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('🤖 [K.M Tag Bot](https://t.me/KMTagBot)-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, Necəsən?🥰.')




#@app.on_message(filters.new_chat_members, group=1)
#async def hg(bot: Client, msg: Message):
   # for new_user in msg.new_chat_members:
    #    if str(new_user.id) == str(Config.BOT_ID):
    #        await msg.reply(
      #          f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər⚡️` \n\n **🤖Qruplardakı Userləri Tag Edmə üçün Yaradıldım.\n🤖Kömək üçün /help yazmaq kifayətdir.**''')

#elif str(new_user.id) == str(Config.OWNER_ID):
#await msg.reply('🤖 [Usta Tagger Bot](https://t.me/Ustataggerbot)-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, Necəsən?🥰.')

#elif str (new_user.id) == str(Config.OWNER_ID):
            #await msg.reply('İşte bu gelen benim sahibim.')

 
#@app.on_message(filters.command("id"))
#async def _id(_, message: Message):
 #   msg = message.reply_to_message or message
  #  out_str = "**User İnfo:**\n"
  #  out_str += f" ⚡️ __Grup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
  #  out_str += f" 💎 __Yanıtlanan Kullanıcı Adı__ : {msg.from_user.first_name}\n"
   # out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id or msg.message_id}`\n"
  #  if msg.from_user:
     #   out_str += f" 🙋🏻‍♂️ __Yanıtlanan Kullanıcı ID__ : `{msg.from_user.id}`\n"
 
   # await message.reply(out_str)

@app.on_message(filters.command("info"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**İsdifadəçi İd'si:**\n"
    out_str += f" ⚡️ __Qrup İd'si__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 🙋🏻‍♂️ __Cavab verən İstifadəçi Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj İd'si__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Cavab verən İstifadəçi İd'si__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)

@app.on_message(filters.command("ping"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"🤖[KM Tag Bot](https://t.me/KMTagBot)\nPing...!\nᖽᐸöᕼᘉə ᘻəᖽᐸᗩᘉ\nｱ尺のﾌ乇ᄃｲ...\n**◤✞Ping✞◥⇎ {round(ms)}**\n\nhttps://t.me/KMBots")
    
#elif str(new_user.id) == str(Config.OWNER_ID):
#await msg.reply('🤖 [Usta Tagger Bot](https://t.me/Ustataggerbot)-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, Necəsən?🥰.')
 
app.start()
print(f"Bot pyrogram ( {pyrogram.__version__} sürümü ile başlatıldı. ")
idle()
