from pyrogram import Client,filters
from random import randint
from gtts import gTTS
import requests,time,shutil
import os
from googletrans import Translator
from typing import Text
import googlesearch
from clint.textui import progress
from moviepy.editor import VideoFileClip
from PIL import Image, ImageSequence

app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")

@app.on_message(filters.regex("!stop") & filters.me)
async def conver_webp(c, m):
    chat_id=await m.chat.id
    message_id=await m.message_id
    id=await m.reply_to_message.message_id
    if (await m.reply_to_message.sticker.is_animated) == False:
        await m.delete()
        file=await m.reply_to_message.sticker.file_id
        await c.download_media(await file,await "sticker.webp")
        img = await Image.open(await 'downloads/sticker.webp').convert(await "RGBA")
        await img.save(await "image.png","PNG")
        await c.send_photo(await chat_id,await "image.png",reply_to_message_id=await id)
        await c.send_documentawait (chat_id,document=await "image.png",reply_to_message_id=await id)
        await os.remove(await "image.png")
        await os.remove(await 'downloads/sticker.webp')
    else:
        await c.edit_message_text(await chat_id, await message_id,await "opps...\nthis sticker is animated\nme can convert the stickers that are not animated🥺\n")

async def thumbnails(frames,size):
    async for frame in frames:
        thumbnail = await frame.copy()
        await thumbnail.thumbnail(await size, await Image.ANTIALIAS)
        yield await thumbnail
@app.on_message((filters.me) & filters.regex("!ftog$"))
async def f_to_gif(client,message):
    message_id=await message.message_id
    chat_id=await message.chat.id
    file_id=await message.reply_to_message.message_id
    id=await message.reply_to_message.video.file_id
    await client.delete_messages(await chat_id,await message_id)
    down=await client.download_media(await id)
    clip=await VideoFileClip(await down)
    await clip.write_gif(await "nowgif.gif")
    im = await Image.open(await "nowgif.gif")
    frames = await ImageSequence.Iterator(await im)
    size = 340, 240
    frames = await thumbnails(await frames,await size)
    om = await next(await frames) # Handle first frame separately
    om.info = await im.info # Copy sequence info
    await om.save(await "nowgif.gif", save_all=True, append_images=await list(await frames))
    await client.send_animation(await chat_id,await "nowgif.gif",reply_to_message_id=await file_id)
    await os.remove(await down)
    await os.remove(await "nowgif.gif")

@app.on_message((filters.me) & (filters.regex("لایک") | filters.regex("دوس") | filters.regex("عالیه") | filters.regex("حق") | filters.regex("👍")))
async def like(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "👍")

@app.on_message((filters.me) & (filters.regex("نموخام") | filters.regex("مزخرف")  | filters.regex("👎")))
async def not_like(client,message):
    if message.reply_to_message:
        chat_id=message.chat.id
        message_id=message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "👎")

@app.on_message((filters.me) & (filters.regex("عشق") | filters.regex("عاشق") | filters.regex("زندگیمی") | filters.regex("فداتشم") | filters.regex("❤️")))
async def love(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "❤️")

@app.on_message((filters.me) & (filters.regex("هورا") | filters.regex("جشن") | filters.regex("مبارک") | filters.regex("🎉")))
async def hoppy(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "🎉")

@app.on_message((filters.me) & (filters.regex("ریدم")| filters.regex("تف") | filters.regex("گوه") | filters.regex("💩")))
async def goh(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "💩")

@app.on_message((filters.me) & (filters.regex("شیطون") | filters.regex("شیطونی") | filters.regex("😁")))
async def lusifer(client,message):
    if message.reply_to_message:
        chat_id=message.chat.id
        message_id=message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "😁")

@app.on_message((filters.me) & (filters.regex("جووون") | filters.regex("خوشکله") | filters.regex("زیبا") | filters.regex("🤩")))
async def biutiful(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "🤩")

@app.on_message((filters.me) & (filters.regex("اتیش") | filters.regex("اتیشپاره") | filters.regex("بخورمت") | filters.regex("اتیشی") | filters.regex("🔥")))
async def fire(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "🔥")

@app.on_message((filters.me) & (filters.regex("مشکل") | filters.regex("نکن") | filters.regex("عجیبه") | filters.regex("😱")))
async def amazing(client,message):
    if message.reply_to_message:
        chat_id=message.chat.id
        message_id=message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "😱")

@app.on_message((filters.me) & (filters.regex("مخم ترکید") | filters.regex("این چی بود") | filters.regex("وای خدا") | filters.regex("🤯")))
async def amazing(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "🤯")

@app.on_message((filters.me) & (filters.regex("تشویق") | filters.regex("تکبیر") | filters.regex("افرین") | filters.regex("👏🏻")))
async def amazing(client,message):
    if message.reply_to_message:
        chat_id=message.chat.id
        message_id=message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,"👏🏻")

@app.on_message((filters.me) & (filters.regex("فوش") | filters.regex("چرت") | filters.regex("دعوا") | filters.regex("🤬")))
async def amazing(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "🤬")

@app.on_message((filters.me) & (filters.regex("ببخشید") | filters.regex("ببشید") | filters.regex("اشتی") | filters.regex("😢")))
async def amazing(client,message):
    if message.reply_to_message:
        chat_id=message.chat.id
        message_id=message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "🤮")

@app.on_message((filters.me) & (filters.regex("حالم بهم خورد") | filters.regex("چه زشت") | filters.regex("حالت تهوع") | filters.regex("🤮")))
async def amazing(client,message):
    if await message.reply_to_message:
        chat_id=await message.chat.id
        message_id=await message.reply_to_message.message_id
        await client.send_reaction(await chat_id,await message_id,await "😢")

@app.on_message((filters.me) & (filters.regex("^!info$")))
async def info(client,message):
    chat_id=await message.chat.id
    await message.delete()
    id=await message.reply_to_message.message_id
    text=f"**INFO USER**\n🆔✝️ **message id :** `{await id}`\n"
    text+=f"🆔 **id:** `{await message.reply_to_message.from_user.id}`\n📝 **is contact:** `{await message.reply_to_message.from_user.is_contact}`\n"
    text+=f"✏️ **first name:** `{await message.reply_to_message.from_user.first_name}`\n"
    if await message.reply_to_message.from_user.last_name:
        text+=f"✏️ **last name:** `{await message.reply_to_message.from_user.last_name}`\n"
    text+=f"🆔✝️ **username:** @{await message.reply_to_message.from_user.username}\n[👀 SEE PROFILE 👀](tg://openmessage?user_id={await message.reply_to_message.from_user.id})"
    if await message.reply_to_message.from_user.photo:
        file=await message.reply_to_message.from_user.photo.big_file_id
        down=await client.download_media(await file)
        await client.send_document(await chat_id,document=await down,caption=await text,reply_to_message_id=await id,parse_mode=await "markdown")
        await os.remove(await down)
    else:
        await client.send_message(await chat_id,await text,reply_to_message_id=await id,parse_mode=await "markdown")

@app.on_message((filters.me) & (filters.regex("^!infof$")))
async def infof(client,message):
    chat_id=await message.chat.id
    await message.delete()
    id=await message.reply_to_message.message_id
    text=f"**INFO FROM USER**\n🆔✝️ **message id :** `{await id}`\n"
    if await message.reply_to_message.forward_sender_name:
        text+=f"❌🔒 ooppsss... 🔒❌\nthe sender of this message has locked his profile.\n🔏 **name sender message :** `{await message.reply_to_message.forward_sender_name}`\n"
        await client.send_message(await chat_id,await text,reply_to_message_id=await id)
    else:
        text+=f"🆔 **id:** `{await message.reply_to_message.forward_from.id}`\n📝 **is contact:** ` {await message.reply_to_message.forward_from.is_contact}`\n"
        text+=f"✏️ **first name:** `{await message.reply_to_message.forward_from.first_name}`\n"
        if await message.reply_to_message.forward_from.last_name:
            text+=f"✏️ **last name:** `{await message.reply_to_message.forward_from.last_name}`\n"
        text+=f"🆔✝️ **username:** @{await message.reply_to_message.forward_from.username}\n[👀 SEE PROFILE 👀](tg://openmessage?user_id={await message.reply_to_message.forward_from.id})"
        if await message.reply_to_message.forward_from.photo:
            file=await message.reply_to_message.forward_from.photo.big_file_id
            down=await client.download_media(await file)
            await client.send_document(await chat_id,document=await down,caption=await text,reply_to_message_id=await id,parse_mode=await "markdown")
            await os.remove(await down)
        else:
            await client.send_message(await chat_id,await text,reply_to_message_id=await id,parse_mode=await "markdown")
            
@app.on_message((filters.me) & (filters.regex("^صبر کن دانلود شه$") | filters.regex("^دانلود نمیشه$")))
async def download_image(client,message):
    if await message.reply_to_message.photo:
        id=await message.reply_to_message.photo.file_id
        down =await client.download_media(await id)
        await client.send_photo(await "me",await down)
        await client.send_document(await "me",document=await down)
        await os.remove(await down)
    if await message.reply_to_message.video:
        id=await message.reply_to_message.video.file_id
        down=await client.download_media(await id)
        await client.send_document(await "me",document=await down)
        await os.remove(await down)

@app.on_message((filters.me) & filters.regex("^!srch "))
async def search(client, message):
    text = await message.text
    text = await text[6:]
    tex = await text.replace(" ", "+")
    result = await googlesearch.search(await tex, num_results=20)
    tex = ""
    async for i in result:
        tex += await i+"\n\n__________________________________\n\n"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id, text=await tex)

@app.on_message(filters.regex("^!trans ") & filters.me)
async def translate(client,message):
    text=await message.reply_to_message.text
    text2=await message.text
    text2=await text2.replace("!trans ","")
    dest=await text2.split()[0]
    translator = await Translator()
    result = await translator.translate(await text,dest=await dest)
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id,text=await result.text)

@app.on_message(filters.regex("^!tts$") &  filters.me)
async def tts(client,message):
    chat_id=await message.chat.id
    message_id=await message.message_id
    text = await message.reply_to_message.text
    language="en"
    myobj=await gTTS(text=text,lang=language,slow=False)
    await myobj.save("test.ogg")
    await client.send_audio(await chat_id,"test.ogg",reply_to_message_id=await message_id)
    await os.remove('test.ogg')

@app.on_message((filters.me) & filters.regex("^! "))
async def small_write(client, message):
    text=await message.text
    chat_id=await message.chat.id
    tex=await ""
    text=await text.replace("! ","")
    x=len(text)
    i=0
    while text[i]!='.':
        if await text[i]=="\n":
            i=await i+1
            tex+=await "\n" +await text[i]
            i=await i+1
        if await text[i]!=" ":
            tex+=await text[i]
            i=await i+1
        else:
            tex+=await text[i]
            i=await i+1
            tex+=await text[i]
            i=await i+1
        await time.sleep(0.2)
        await client.edit_message_text(await chat_id,message_id=await message.message_id,text=await tex)

@app.on_message((filters.me) & filters.regex("^!vazhe "))
async def vazhe(client,message):
    text=await message.text
    chat_id=await message.chat.id
    name=await text.replace("!vazhe ","")
    Response=await requests.post(await f"https://api.codebazan.ir/vajehyab/?text={await name}")
    tex=await Response.json()
    fa=await tex["result"]["fa"]
    en=await tex["result"]["en"]
    moein=await tex["result"]["Fmoein"]
    deh=await tex["result"]["Fdehkhoda"]
    mo=await tex["result"]["motaradefmotezad"]
    text=await f"**فارسی کلمه:** `{await fa}`\n**تلفظ کلمه: ** `{await en}`\n\n**معنی کلمه در فرهنگ لغت معین: ** `{await moein}`\n\n**معنی کلمه در فرهنگ لغت دهخدا: ** `{await deh}`\n\n**مترادف و متضاد کلمه: ** `{await mo}`"
    await client.edit_message_text(await chat_id,message_id=await message.message_id,text=await text)

@app.on_message((filters.me) & filters.regex("^!logo "))
async def logo2(client,message):
    text=await message.text
    chat_id=await message.chat.id
    name=await text.replace("!logo ","")
    num=await randint(58,109)
    Response=await requests.post(await f"https://api.codebazan.ir/ephoto/writeText?output=image&effect=create-online-black-and-white-layerlogo-{await num}.html&text={await name}")
    async with await open("logo2.jpg","wb") as f:
        await f.write(await Response.content)   
    await client.send_photo(await chat_id,await "logo2.jpg",reply_to_message_id=await message.message_id)
    await os.remove(await "logo2.jpg")

@app.on_message((filters.me) & filters.regex("^!num "))
async def numtofa(client,message):
    text=await message.text
    chat_id=await message.chat.id
    nume=await text.replace("!num ","")
    Response=await requests.post(f"https://api.codebazan.ir/num/?num={await nume}")
    tex=await Response.json()
    await client.edit_message_text(await chat_id,message_id=await message.message_id,text=await tex["result"]["num"])

@app.on_message((filters.me) & filters.regex("^!pdf "))
async def webtopdf(client,message):
    text=await message.text
    chat_id=await message.chat.id
    name=await text.replace("!pdf ","")
    tex=await name[0:5]
    if tex=="https":
        name=await name[8:]
        url1=await "https://"+await name
    if tex=="http:":
        name=await name[7:]
        url1=await "http://"+await name
    Response=await requests.post(await f"https://api.codebazan.ir/htmltopdf/?type=json&url={await url1}")
    tex=await Response.json()
    url=await tex["result"]["url"]
    pdf=await requests.get(await url)
    await time.sleep(3)
    async with await open("webtopdf.pdf","wb") as f:
        await f.write(await pdf.content)
    await client.send_document(await chat_id,await "webtopdf.pdf",reply_to_message_id=await message.message_id)
    await os.remove(await "webtopdf.pdf")

@app.on_message((filters.me) & filters.regex("^!proxy$"))
async def proxy(client,message):
    messag_id=await message.message_id
    Response=await requests.post(await "http://api.codebazan.ir/mtproto/json/") 
    tex=await Response.json()
    tex=await tex["Result"]
    text=await ""
    async for i in await range(0,20):
        server=await tex[i]["server"]
        port=await tex[i]["port"]
        secret=await tex[i]["secret"]
        text+=await f"{await i+1}- https://t.me/proxy?server={await server}&port={await port}&secret={await secret}\n\n/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/\n"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await messag_id,text=await text)

@app.on_message((filters.me) & filters.regex("^!pass "))
async def password_gen(client,message):
    text=await message.text
    messag_id=await message.message_id
    name=await text.replace("!pass ","")
    Response=await requests.post(await f"http://api.codebazan.ir/password/?length={await name}")
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await messag_id,text=await Response.text)

@app.on_message((filters.me) & filters.regex("^!. "))
async def strrev(client,message):
    text=await message.text
    messag_id=await message.message_id
    name=await text.replace("!. ","")
    Response=await requests.post(await f"http://api.codebazan.ir/strrev/?text={await name}") 
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await messag_id,text=await Response.text)

@app.on_message((filters.me) & filters.regex("^!arz$"))
async def arz(client,message):
    messag_id=await message.message_id
    Response=await requests.post(await "http://api.codebazan.ir/arz/?type=arz")
    tex=await Response.json()
    result=await ""
    async for i in await range(0,15):
        name=await tex[i]["name"]
        price=await tex[i]["price"]
        change=await tex[i]["change"]
        percent=await tex[i]["percent"]
        result+=await f"**name:**{await name}\n**price:**{await price}\n**change:**{await change}{await percent}\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await messag_id,text=await result)

@app.on_message((filters.me) & filters.regex("^!font "))
async def font(client,message):
    text=await message.text
    messag_id=await message.message_id
    text=await text.replace("!font ","")
    Response=await requests.post(await f"http://api.codebazan.ir/font/?text={await text}")
    tex=await Response.json()
    result=await ""
    async for i in await tex["result"]:
        font=await tex["result"][i]
        result+=await f"**{await i}:**`{await font}`\n\n"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await messag_id,text=await result)
     
@app.on_message((filters.me) & filters.regex("^!fontfa "))
async def fontfa(client,message):
    text=await message.text
    messag_id=await message.message_id
    text=await text.replace("!fontfa ","")
    Response=await requests.post(await f"https://api.codebazan.ir/font/?type=fa&text={await text}")
    tex=await Response.json()
    result=await ""
    async for i in await tex["Result"]:
        font=await tex["Result"][i]
        result+=await f"**{await i}:**`{await font}`\n"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await messag_id,text=await result)

@app.on_message((filters.me) & filters.regex("^!ttr "))
async def ttr(client,message):
    text=await message.reply_to_message.text
    tex=await message.text
    chat_id=await message.chat.id
    language=await tex.replace("!ttr ","")
    myobj=await gTTS(text=await text,lang=await language,slow=await False)
    await myobj.save(await "testvoice.ogg")
    await client.send_audio(await chat_id,await "testvoice.ogg",reply_to_message_id=await message.message_id)
    await os.remove(await 'testvoice.ogg')

@app.on_message((filters.me) & filters.regex("^!bio$"))
async def biografi(client,message):
    Response=await requests.post(await "https://api.codebazan.ir/bio")
    text=await Response.text
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id,text=await text)

@app.on_message((filters.me) & filters.regex("^!newyear$"))
async def newyear(client,message):
    response=await requests.post(await "https://api.codebazan.ir/new-year")
    tex=await response.json()
    text=await ""
    day=await tex["day"]
    text+=await f"{await day} روز و"
    hour=await tex["hour"]
    text+=await f"{await hour} ساعت و"
    min=await tex["min"]
    text+=await f"{await min} دقیقه و"
    sec=await tex["sec"]
    text+=await f"{await sec} ثانیه دیگر تا نوروز مانده است."
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id,text=await text)

@app.on_message((filters.me) & filters.regex("^!saadi$"))
async def ghazalsaadi(client,message):
    response=await requests.post(await f"https://api.codebazan.ir/ghazalsaadi/?type=json&id={await randint(0,637)}")
    tex=await response.json()
    title=await tex["title"]
    cont=await tex["contents"]
    text=await f"**عنوان: ** `{await title}`\n**غزل: **`{await cont}`"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id,text=await text)

@app.on_message((filters.me) & filters.regex("!del$"))
async def delete_mess(client,message):
    chat_id=await message.chat.id
    await message.delete()
    message_id=await message.reply_to_message.message_id
    await client.delete_messages(await chat_id,await message_id)

@app.on_message((filters.me) & filters.regex("^!gif "))
async def gif(client,message):
    text=await message.text
    chat_id=await message.chat.id
    messag_id=await message.message_id
    name=await text.replace("!gif ","")
    response=await requests.post(await f"https://api.codebazan.ir/image/?type=gif&text={await name}")
    text1=await response.json()
    url=await text1[f"giflink{await randint(1,11)}"]
    gif=await requests.get(await url)
    async with await open(f"{name}.gif","wb") as f:
        await f.write(await gif.content)
    await client.send_animation(await chat_id,await f"{await name}.gif",reply_to_message_id=await messag_id)
    await os.remove(await f"{await name}.gif")

@app.on_message((filters.me) & filters.regex("^!meli"))
async def meli(client,message):
    text=await message.text
    code=await text.replace("!meli ","")
    Response=await requests.post(await f"https://api.codebazan.ir/codemelli/?code={await code}")
    tex=await Response.json()
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id,text=await tex["Result"])

@app.on_message((filters.me) & filters.regex("^!air "))
async def air(client,message):
    text=await message.text
    city=await text.replace("!air ","")
    Response=await requests.post(await f"https://api.codebazan.ir/weather/?city={await city}")
    tex=await Response.json()
    ostan=await tex["result"]["استان"]
    shahr=await tex["result"]["شهر"]
    dama=await tex["result"]["دما"]
    sorat=await tex["result"]["سرعت باد"]
    vaziat=await tex["result"]["وضعیت هوا"]
    fdama=await tex["فردا"]["دما"]
    fvaziat=await tex["فردا"]["وضعیت هوا"]
    text=await f"**استان: ** {await ostan}\n**شهر: ** {await shahr}\n**          امروز **\n**دما: ** {await dama}\n**سرعت باد: ** {await sorat}\n**وضعیت هوا: ** {await vaziat}\n\n      **فردا **\n**دما: ** {await fdama}\n**وضعیت هوا: ** {await fvaziat}"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id,text=await text)
    
@app.on_message((filters.me) & filters.regex("!down "))
async def download(client,message):
    text=await message.text
    url=await text[6:]
    response=await requests.get(await url,stream=await True)
    message_id=await message.message_id
    chat_id=await message.chat.id
    file_name=await os.path.basename(url)
    file=await response.raw
    await client.edit_message_text(await chat_id,await message_id,await f"👾 **DOWNLOADING...**\n**FILE NAME:** {await file_name}\n")
    f = open(file_name, 'wb')
    async for chunk in await response.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            await f.write(await chunk)
    await f.close()
    await client.edit_message_text(await chat_id,await message_id,await f"👾 **UPLOADING...**\n**FILE NAME:** {await file_name}\n")
    await client.send_document(await chat_id,await file_name,reply_to_message_id=await message_id)
    await os.remove(await file_name)

@app.on_message((filters.me) & filters.regex("^!help$"))
async def help(client,message):
    help=await ""
    help+=await "**command:**\n!info \n**descriptin:**\nsend info user replyed message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!infof \n**descriptin:**\nsend info user forward message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!stop \n**descriptin:**\nconvert replyed sticker to png\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!ftog \n**descriptin:**\nconvert replyed movie to gif\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!down \n**descriptin:**\nget link download and upload to telegram\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!del \n**descriptin:**\nget reply message and delete message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!srch \n**descriptin:**\nget text and show result search\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!trans \n**descriptin:**\nget text and source language and defective language so print trtanslate\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!tts \n**descriptin:**\nget text and send voice text to language english \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n! \n**descriptin:**\nget text and print it slowly\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!air\n**descriptin:**\nget city and send climatic condition\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!meli\n**descriptin:**\nsend result sending code meli\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!card\n**descriptin:**\nsend credit card\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!gif\n**descriptin:**\nget string and send gif withe string\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!saadi\n**descriptin:**\nsend one lyric from saadi\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!newyear\n**descriptin:**\nsend remaining amount until nowruz\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!bio\n**descriptin:**\nsend one bio\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!vazhe\n**descriptin:**\nget word prsion and send meaning\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!num\n**descriptin:**\nget number and send number to persion\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!.\n**descriptin:**\nget string and send strrev\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!arz\n**descriptin:**\nsend list from name , price and change currency\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!font\n**descriptin:**\nget name or any thing and send difrent fonts\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!fontfa\n**descriptin:**\nget persion text and send difrent font\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!logo\n**descriptin:**\nget text and send logo withe text\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!ttr\n**descriptin:**\nget language and text so send voice text withe input language \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!pdf\n**descriptin:**\nget link web and send pdf shot web \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!proxy\n**descriptin:**\nsend 20 MTproxy for telegram\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n!pass\n**descriptin:**\nget number and genereat password to len number\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help+=await "**command:**\n(دانلود نمیشه|صبر کن دانلود شه)\n**descriptin:**\ndownload and send media to saved  message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    await client.edit_message_text(chat_id=await message.chat.id,message_id=await message.message_id,text=await help)
app.run()  # Automatically start() and idle()
