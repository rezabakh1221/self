from pyrogram import Client,filters
from random import randint
from gtts import gTTS
import requests,time,os,googlesearch,threading
from googletrans import Translator
from typing import Text
from moviepy.editor import VideoFileClip
from PIL import Image, ImageSequence, ImageDraw, ImageFont
from datetime import datetime
from pytz import timezone
app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")
class bot(threading.Thread):
    #-------------------------------------------------------------------------------------stop
    def conver_webp(c, m):
        chat_id=m.chat.id
        message_id=m.message_id
        id=m.reply_to_message.message_id
        if (m.reply_to_message.sticker.is_animated) == False:
            m.delete()
            file=m.reply_to_message.sticker.file_id
            down=c.download_media(file,"sticker.webp")
            img = Image.open('downloads/sticker.webp').convert("RGBA")
            img.save("image.png","PNG")
            c.send_photo(chat_id,"image.png",reply_to_message_id=id)
            c.send_document(chat_id,document="image.png",reply_to_message_id=id)
            os.remove("image.png")
            os.remove('downloads/sticker.webp')
        else:
            c.edit_message_text(chat_id, message_id,"opps...\nthis sticker is animated\nme can convert the stickers that are not animated🥺\n")
    #-------------------------------------------------------------------------------------ftog
    def thumbnails(frames,size):
        for frame in frames:
            thumbnail = frame.copy()
            thumbnail.thumbnail(size, Image.ANTIALIAS)
            yield thumbnail
    def f_to_gif(client,message):
        chat_id=message.chat.id
        file_id=message.reply_to_message.message_id
        id=message.reply_to_message.video.file_id
        message.delete()
        down=client.download_media(id)
        clip=VideoFileClip(down)
        clip.write_gif("nowgif.gif")
        im = Image.open("nowgif.gif")
        frames = ImageSequence.Iterator(im)
        size = 340, 240
        frames = bot.thumbnails(frames,size)
        om = next(frames) # Handle first frame separately
        om.info = im.info # Copy sequence info
        om.save("nowgif.gif", save_all=True, append_images=list(frames))
        client.send_animation(chat_id,"nowgif.gif",reply_to_message_id=file_id)
        os.remove(down)
        os.remove("nowgif.gif")
    #------------------------------------------------------------------------------------kos
    def like(client,message):
        if message.reply_to_message:
            chat_id=message.chat.id
            message_id=message.reply_to_message.message_id
            client.send_reaction(chat_id,message_id,"👍")

    def not_like(client,message):
        if message.reply_to_message:
            chat_id=message.chat.id
            message_id=message.reply_to_message.message_id
            client.send_reaction(chat_id,message_id,"👎")

    def love(client,message):
        if message.reply_to_message:
            chat_id=message.chat.id
            message_id=message.reply_to_message.message_id
            client.send_reaction(chat_id,message_id,"❤️")

    #---------------------------------------------------------------------------------------info & infof
    def info(client,message):
        chat_id=message.chat.id
        message.delete()
        id=message.reply_to_message.message_id
        text=f"**INFO USER**\n🆔✝️ **message id :** `{id}`\n"
        text+=f"🆔 **id:** `{message.reply_to_message.from_user.id}`\n📝 **is contact:** `{message.reply_to_message.from_user.is_contact}`\n"
        text+=f"✏️ **first name:** `{message.reply_to_message.from_user.first_name}`\n"
        if message.reply_to_message.from_user.last_name:
            text+=f"✏️ **last name:** `{message.reply_to_message.from_user.last_name}`\n"
        text+=f"🆔✝️ **username:** @{message.reply_to_message.from_user.username}\n[👀 SEE PROFILE 👀](tg://openmessage?user_id={message.reply_to_message.from_user.id})"
        if message.reply_to_message.from_user.photo:
            file=message.reply_to_message.from_user.photo.big_file_id
            client.download_media(file,f"{message.reply_to_message.from_user.id}.png")
            client.send_document(chat_id,document=f"downloads/{message.reply_to_message.from_user.id}.png",caption=text,reply_to_message_id=id,parse_mode="markdown")
            os.remove(f"downloads/{message.reply_to_message.from_user.id}.png")
        else:
            client.send_message(chat_id,text,reply_to_message_id=id,parse_mode="markdown")

    def infof(client,message):
        chat_id=message.chat.id
        message.delete()
        id=message.reply_to_message.message_id
        text=f"**INFO FROM USER**\n🆔✝️ **message id :** `{id}`\n"
        if message.reply_to_message.forward_sender_name:
            text+=f"❌🔒 ooppsss... 🔒❌\nthe sender of this message has locked his profile.\n🔏 **name sender message :** `{message.reply_to_message.forward_sender_name}`\n"
            client.send_message(chat_id,text,reply_to_message_id=id)
        else:
            text+=f"🆔 **id:** `{message.reply_to_message.forward_from.id}`\n📝 **is contact:** `{message.reply_to_message.forward_from.is_contact}`\n"
            text+=f"✏️ **first name:** `{message.reply_to_message.forward_from.first_name}`\n"
            if message.reply_to_message.forward_from.last_name:
                text+=f"✏️ **last name:** `{message.reply_to_message.forward_from.last_name}`\n"
            text+=f"🆔✝️ **username:** @{message.reply_to_message.forward_from.username}\n[👀 SEE PROFILE 👀](tg://openmessage?user_id={message.reply_to_message.forward_from.id})"
            if message.reply_to_message.forward_from.photo:
                file=message.reply_to_message.forward_from.photo.big_file_id
                client.download_media(file,f"{message.reply_to_message.forward_from.id}.png")
                client.send_document(chat_id,document=f"downloads/{message.reply_to_message.forward_from.id}.png",caption=text,reply_to_message_id=id,parse_mode="markdown")
                os.remove(f"downloads/{message.reply_to_message.forward_from.id}.png")
            else:
                client.send_message(chat_id,text,reply_to_message_id=id,parse_mode="markdown")
            
    #-------------------------------------------------------------------------------------------------------colesh
    def download_image(client,message):
        if message.reply_to_message.photo:
            id=message.reply_to_message.photo.file_id
            down=client.download_media(id)
            client.send_photo("me",down)
            client.send_document("me",document=down)
            os.remove(down)
        if message.reply_to_message.video:
            id=message.reply_to_message.video.file_id
            down=client.download_media(id)
            client.send_document("me",document=down)
            os.remove(down)

    def search(client, message):
        text = message.text
        text = text[6:]
        ln = len(text)
        tex = text.replace(" ", "+")
        result = googlesearch.search(tex, num_results=20)
        tex = ""
        for i in result:
            tex += i+"\n\n__________________________________\n\n"
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id, text=tex)

    def translate(client,message):
        text=message.reply_to_message.text
        text2=message.text
        text2=text2.replace("!trans ","")
        dest=text2.split()[0]
        translator = Translator()
        result = translator.translate(text,dest=dest)
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=result.text)

    def tts(client,message):
        chat_id=message.chat.id
        message_id=message.message_id
        text = message.reply_to_message.text
        language="en"
        myobj=gTTS(text=text,lang=language,slow=False)
        myobj.save("test.ogg")
        client.send_audio(chat_id,"test.ogg",reply_to_message_id=message_id)
        os.remove('test.ogg')

    def small_write(client, message):
        text=message.text
        chat_id=message.chat.id
        tex=""
        text=text.replace("! ","")
        x=len(text)
        i=0
        while text[i]!='.':
            if text[i]=="\n":
                i=i+1
                tex+="\n" +text[i]
                i=i+1
            if text[i]!=" ":
                tex+=text[i]
                i=i+1
            else:
                tex+=text[i]
                i=i+1
                tex+=text[i]
                i=i+1
            time.sleep(0.2)
            client.edit_message_text(chat_id,message_id=message.message_id,text=tex)

    def vazhe(client,message):
        text=message.text
        chat_id=message.chat.id
        name=text.replace("!vazhe ","")
        Response=requests.post(f"https://api.codebazan.ir/vajehyab/?text={name}")
        tex=Response.json()
        fa=tex["result"]["fa"]
        en=tex["result"]["en"]
        moein=tex["result"]["Fmoein"]
        deh=tex["result"]["Fdehkhoda"]
        mo=tex["result"]["motaradefmotezad"]
        text=f"**فارسی کلمه:** `{fa}`\n**تلفظ کلمه: ** `{en}`\n\n**معنی کلمه در فرهنگ لغت معین: ** `{moein}`\n\n**معنی کلمه در فرهنگ لغت دهخدا: ** `{deh}`\n\n**مترادف و متضاد کلمه: ** `{mo}`"
        client.edit_message_text(chat_id,message_id=message.message_id,text=text)

    def webtopdf(client,message):
        text=message.text
        chat_id=message.chat.id
        name=text.replace("!pdf ","")
        tex=name[0:5]
        if tex=="https":
            name=name[8:]
            url1="https://"+name
        if tex=="http:":
            name=name[7:]
            url1="http://"+name
        Response=requests.post(f"https://api.codebazan.ir/htmltopdf/?type=json&url={url1}")
        tex=Response.json()
        url=tex["result"]["url"]
        pdf=requests.get(url)
        time.sleep(3)
        namefile="test.pdf"
        with open("webtopdf.pdf","wb") as f:
            f.write(pdf.content)
        client.send_document(chat_id,"webtopdf.pdf",reply_to_message_id=message.message_id)
        os.remove("webtopdf.pdf")

    def password_gen(client,message):
        text=message.text
        messag_id=message.message_id
        name=text.replace("!pass ","")
        Response=requests.post(f"http://api.codebazan.ir/password/?length={name}")
        client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=Response.text)

    def strrev(client,message):
        text=message.text
        messag_id=message.message_id
        name=text.replace("!. ","")
        Response=requests.post(f"http://api.codebazan.ir/strrev/?text={name}") 
        client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=Response.text)

    def font(client,message):
        text=message.text
        messag_id=message.message_id
        text=text.replace("!font ","")
        Response=requests.post(f"http://api.codebazan.ir/font/?text={text}")
        tex=Response.json()
        result=""
        for i in tex["result"]:
            font=tex["result"][i]
            result+=f"**{i}:**`{font}`\n\n"
        client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)
        
    def fontfa(client,message):
        text=message.text
        messag_id=message.message_id
        text=text.replace("!fontfa ","")
        Response=requests.post(f"https://api.codebazan.ir/font/?type=fa&text={text}")
        tex=Response.json()
        result=""
        for i in tex["Result"]:
            font=tex["Result"][i]
            result+=f"**{i}:**`{font}`\n"
        client.edit_message_text(chat_id=message.chat.id,message_id=messag_id,text=result)

    def ttr(client,message):
        text=message.reply_to_message.text
        tex=message.text
        chat_id=message.chat.id
        language=tex.replace("!ttr ","")
        myobj=gTTS(text=text,lang=language,slow=False)
        myobj.save("testvoice.ogg")
        client.send_audio(chat_id,"testvoice.ogg",reply_to_message_id=message.message_id)
        os.remove('testvoice.ogg')

    def biografi(client,message):
        Response=requests.post("https://api.codebazan.ir/bio")
        text=Response.text
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=text)

    def newyear(client,message):
        response=requests.post("https://api.codebazan.ir/new-year")
        tex=response.json()
        text=""
        day=tex["day"]
        text+=f"{day} روز و"
        hour=tex["hour"]
        text+=f"{hour} ساعت و"
        min=tex["min"]
        text+=f"{min} دقیقه و"
        sec=tex["sec"]
        text+=f"{sec} ثانیه دیگر تا نوروز مانده است."
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=text)

    def ghazalsaadi(client,message):
        response=requests.post(f"https://api.codebazan.ir/ghazalsaadi/?type=json&id={randint(0,637)}")
        tex=response.json()
        title=tex["title"]
        cont=tex["contents"]
        text=f"**عنوان: ** `{title}`\n**غزل: **`{cont}`"
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=text)

    def delete_mess(client,message):
        message.delete()
        chat_id=message.chat.id
        message_id=message.reply_to_message.message_id
        client.delete_messages(chat_id,message_id)

    def gif(client,message):
        text=message.text
        chat_id=message.chat.id
        messag_id=message.message_id
        name=text.replace("!gif ","")
        response=requests.post(f"https://api.codebazan.ir/image/?type=gif&text={name}")
        text1=response.json()
        url=text1[f"giflink{randint(1,11)}"]
        gif=requests.get(url)
        with open(f"{name}.gif","wb") as f:
            f.write(gif.content)
        client.send_animation(chat_id,f"{name}.gif",reply_to_message_id=messag_id)
        os.remove(f"{name}.gif")

    def meli(client,message):
        text=message.text
        code=text.replace("!meli ","")
        Response=requests.post(f"https://api.codebazan.ir/codemelli/?code={code}")
        tex=Response.json()
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=tex["Result"])
        
    def download(client,message):
        text=message.text
        url=text[6:]
        response=requests.get(url,stream=True)
        message_id=message.message_id
        chat_id=message.chat.id
        file_name=os.path.basename(url)
        file=response.raw
        client.edit_message_text(chat_id,message_id,f"👾 **DOWNLOADING...**\n**FILE NAME:** {file_name}\n")
        f = open(file_name, 'wb')
        for chunk in response.iter_content(chunk_size=512 * 1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
        f.close()
        client.edit_message_text(chat_id,message_id,f"👾 **UPLOADING...**\n**FILE NAME:** {file_name}\n")
        client.send_document(chat_id,file_name,reply_to_message_id=message_id)
        os.remove(file_name) 

    def change_photo(client,message):
        list_photo=["1.jpg","2.jpg","3.jpg"]
        photo=list_photo[randint(0,2)]
        iran = timezone("Asia/Tehran")
        date_time = datetime.now(iran).strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2 = time1[:8]
        hour,minutes,seconds =  time2.split(':')
        if int(hour)>12:
            f=int(hour)-12
            text=f"{f} : {minutes} PM"
        else:
            text=f"{hour} : {minutes} AM"
        if photo=="1.jpg":
            img = Image.open('1.jpg')
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype('font.ttf', 40)
            d1.text((230, 440), text, font=myFont, fill =(255, 255, 255))
            img.save("1-1.jpg")
        if photo=="2.jpg":
            img = Image.open('2.jpg')
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype('font.ttf', 40)
            d1.text((290, 130), text, font=myFont, fill =(255, 255, 255))
            img.save("2-2.jpg")
        if photo=="3.jpg":
            img = Image.open('3.jpg')
            d1 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype('font.ttf', 40)
            d1.text((220, 130), text, font=myFont, fill =(255, 255, 255))
            img.save("3-3.jpg")
        photos=app.get_profile_photos("me")
        if photos:
            app.delete_profile_photos([p.file_id for p in photos])
        else:pass
        if photo=="1.jpg":
            app.set_profile_photo(photo="1-1.jpg")
        if photo=="2.jpg":
            app.set_profile_photo(photo="2-2.jpg")
        if photo=="3.jpg":
            app.set_profile_photo(photo="3-3.jpg")
        return photo
        
    def setname(client,message):
        text=str(message.text)[8:]
        x=text.find("|")
        clo=text[x+1:] 
        bot.change_photo(client,message)
        message.delete()
        client.update_profile(first_name=text,bio=f"○━━─  {clo} •͜•   ──⇆○")
        time.sleep(1)
        message.reply("settime")

    def help(client,message):
        help=""
        help+="**command:**\n!info \n**descriptin:**\nsend info user replyed message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!infof \n**descriptin:**\nsend info user forward message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!stop \n**descriptin:**\nconvert replyed sticker to png\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!ftog \n**descriptin:**\nconvert replyed movie to gif\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!down \n**descriptin:**\nget link download and upload to telegram\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!del \n**descriptin:**\nget reply message and delete message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!srch \n**descriptin:**\nget text and show result search\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!trans \n**descriptin:**\nget text and source language and defective language so print trtanslate\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!tts \n**descriptin:**\nget text and send voice text to language english \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n! \n**descriptin:**\nget text and print it slowly\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!meli\n**descriptin:**\nsend result sending code meli\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!gif\n**descriptin:**\nget string and send gif withe string\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!saadi\n**descriptin:**\nsend one lyric from saadi\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!newyear\n**descriptin:**\nsend remaining amount until nowruz\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!bio\n**descriptin:**\nsend one bio\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!vazhe\n**descriptin:**\nget word prsion and send meaning\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!.\n**descriptin:**\nget string and send strrev\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!font\n**descriptin:**\nget name or any thing and send difrent fonts\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!fontfa\n**descriptin:**\nget persion text and send difrent font\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!ttr\n**descriptin:**\nget language and text so send voice text withe input language \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!pdf\n**descriptin:**\nget link web and send pdf shot web \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n!pass\n**descriptin:**\nget number and genereat password to len number\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        help+="**command:**\n(دانلود نمیشه|صبر کن دانلود شه)\n**descriptin:**\ndownload and send media to saved  message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
        client.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=help)

@app.on_message(filters.regex("!stop") & filters.me)
async def conver_webp(c, m):
    t1=threading.Thread(target=bot.conver_webp,name=str("conver"),args=(c,m))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("!ftog$"))
async def f_to_gif(client,message):
    t1=threading.Thread(target=bot.f_to_gif,name=str("ftog"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & (filters.regex("لایک") | filters.regex("دوس") | filters.regex("عالیه") | filters.regex("حق") | filters.regex("👍")))
async def like(client,message):
    t1=threading.Thread(target=bot.like,name=str("like"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & (filters.regex("نموخام") | filters.regex("مزخرف")  | filters.regex("👎")))
async def not_like(client,message):
    t1=threading.Thread(target=bot.not_like,name=str("not like"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & (filters.regex("عشق") | filters.regex("عاشق") | filters.regex("زندگیمی") | filters.regex("فداتشم") | filters.regex("❤️")))
async def love(client,message):
    t1=threading.Thread(target=bot.love,name=str("love"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & (filters.regex("^!info$")))
async def info(client,message):
    t1=threading.Thread(target=bot.info,name=str({"info"}),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & (filters.regex("^!infof$")))
async def infof(client,message):
    t1=threading.Thread(target=bot.infof,name=str("infof"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & (filters.regex("^صبر کن دانلود شه$") | filters.regex("^دانلود نمیشه$")))
async def download_image(client,message):
    t1=threading.Thread(target=bot.download_image,name=str("download_image"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!srch "))
async def search(client, message):
    t1=threading.Thread(target=bot.search,name=str("srch"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message(filters.regex("^!trans ") & filters.me)
async def translate(client,message):
    t1=threading.Thread(target=bot.translate,name=str("translate"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message(filters.regex("^!tts$") &  filters.me)
async def tts(client,message):
    t1=threading.Thread(target=bot.tts,name=str("tts"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^! "))
async def small_write(client, message):
    t1=threading.Thread(target=bot.small_write,name=str("small"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!vazhe "))
async def vazhe(client,message):
    t1=threading.Thread(target=bot.vazhe,name=str("vazhe"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!pdf "))
async def webtopdf(client,message):
    t1=threading.Thread(target=bot.webtopdf,name=str("webtopdf"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!pass "))
async def password_gen(client,message):
    t1=threading.Thread(target=bot.password_gen,name=str("pasword"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!. "))
async def strrev(client,message):
    t1=threading.Thread(target=bot.strrev,name=str("strv"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!font "))
async def font(client,message):
    t1=threading.Thread(target=bot.font,name=str("font"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!fontfa "))
async def fontfa(client,message):
    t1=threading.Thread(target=bot.fontfa,name=str("fontfa"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!ttr "))
async def ttr(client,message):
    t1=threading.Thread(target=bot.ttr,name=str("ttr"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!bio$"))
async def biografi(client,message):
    t1=threading.Thread(target=bot.biografi,name=str("biografi"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!newyear$"))
async def newyear(client,message):
    t1=threading.Thread(target=bot.newyear,name=str("newyear"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!saadi$"))
async def ghazalsaadi(client,message):
    t1=threading.Thread(target=bot.ghazalsaadi,name=str("ghazal"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("!del$"))
async def delete_mess(client,message):
    t1=threading.Thread(target=bot.delete_mess,name=str("delete"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!gif "))
async def gif(client,message):
    t1=threading.Thread(target=bot.gif,name=str("gif"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!meli"))
async def meli(client,message):
    t1=threading.Thread(target=bot.meli,name=str("meli"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("!down "))
async def download(client,message):
    t1=threading.Thread(target=bot.download,name=str("download"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.user(760148720)) & filters.regex("^setname "))
async def setname(client,message):
    t1=threading.Thread(target=bot.setname,name=str("setname"),args=(client,message))
    t1.start()
    t1.join()
@app.on_message((filters.me) & filters.regex("^!help$"))
async def help(client,message):
    t1=threading.Thread(target=bot.help,name=str("help"),args=(client,message))
    t1.start()
    t1.join()

app.run()
