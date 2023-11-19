import telebot
import random
import qrcode
from persiantools.jdatetime import JalaliDate
import gtts

bot = telebot.TeleBot("6836755262:AAET97-d45Q0Ax93tcphANQ-LWrTaQg_bRk", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
item_markup1 = telebot.types.KeyboardButton("/QRcode")
item_markup2 = telebot.types.KeyboardButton("/game")
item_markup3 = telebot.types.KeyboardButton("/age")
item_markup4 = telebot.types.KeyboardButton("/voice")
item_markup5 = telebot.types.KeyboardButton("/max")
item_markup6 = telebot.types.KeyboardButton("/index_max")
item_markup7 = telebot.types.KeyboardButton("/help")
markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f" خوش آمدید {user_name}", reply_markup=markup)

@bot.message_handler(commands=["QRcode"])
def crating_QRcode(message):
    text = bot.send_message(message.chat.id, "جمله مورد نظر خود را وارد کنید")
    bot.register_next_step_handler(text, crating_QRcode)

@bot.message_handler(commands=["game"])
def game(message):
    global number
    number = random.randint(1, 100)
    user_number_input = bot.send_message(message.chat.id, "بازی شروع شد. یک عدد بین 1 تا 100 انتخاب کن!")
    bot.register_next_step_handler(user_number_input, user_number)

@bot.message_handler(commands=["age"])
def birthday(message):
    user_date = bot.send_message(message.chat.id, "لطفا سال تولد خود را به هجری شمسی وارد بکنید\nمثل:(1390-11-02)")
    bot.register_next_step_handler(user_date, user_age)

@bot.message_handler(commands=["voice"])
def english_to_speak(message):
    text = bot.send_message(message.chat.id, "جمله مورد نظر خود را به انگلیسی وارد کنید")
    bot.register_next_step_handler(text, english_to_speak)

@bot.message_handler(commands=["max"])
def user_number_list(message):
    user_numbers = bot.send_message(message.chat.id, "اعداد لیست را با استفاده از ',' از هم جدا کنید")
    bot.register_next_step_handler(user_numbers, max_list)
      
@bot.message_handler(commands=["index_max"])
def number_list(message):
    user_numbers = bot.send_message(message.chat.id, "اعداد لیست را با استفاده از ',' از هم جدا کنید")
    bot.register_next_step_handler(user_numbers, index_max_list)

def help_user(message):
    bot.reply_to(message, "این گزینه هایی است که میتونی از بات استفاده کنی")
    bot.send_message(message.chat.id, "QRcode: اگر بهش یه جمله بدی برات تبدیل به QRcode میکنه"
                                    "\n game: بازی حدس کلمات شروع میشه"
                                    "\n age: اگر تاریخ تولدت رو بگی دقیق حساب میکنه که چند سالت هست"
                                    "\n voice: اگر بهش یه جمله انگلیسی بدی بهت یهویس از همون جملت میده"
                                    "\n max: اگر یه لیست از اعداد بدی بهت میگه کدومش بزرگ تره"
                                    "\n index_max: اگر یه لیست از اعداد بدی بهت میگه توی کدوم خونه بزرگترین عدد هست"
                                    "\n help: این هم که الان زدی ولی خب این بهت لیست کامند هارو نشون میده")

@bot.message_handler(func=lambda m: True)
def user_text(message):
    QR_text = message.text
    img = qrcode.make(QR_text)
    img.save("Qrcode.png")
    bot.send_photo(message.chat.id, img, reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def user_number(message):
    chat_id = message.chat.id
    if number > int(message.text):
        bot.send_message(chat_id, "عددی که انتخاب کردی کوچکتر از عدد درسته. پس برو بالا تر!")
    elif number < int(message.text):
        bot.send_message(chat_id, "عددی که انتخاب کردی بزرگتر از عدد درسته. پس بیا پایین تر!")
    elif number == int(message.text):
        bot.send_message(chat_id, "برنده شدی!")

@bot.message_handler(func=lambda m:True)
def user_age(message):
    user_birthday = str(message.chat.id)
    try:
        birth_year, birth_month, birth_day = map(int, user_birthday.split("-"))
        dob_date = JalaliDate(birth_year, birth_month, birth_day)
        today_date = JalaliDate.today()

        age_timedelta = today_date - dob_date
        age_days = age_timedelta.days
        age_years = age_days // 365
        remaining_days = age_days % 365
        age_months = remaining_days // 30
        remaining_days %= 30

        age_info = age_years, age_months, remaining_days
        bot.reply_to(message, age_info)
    except ValueError:
        bot.reply_to(message, "تاریخ وارد شده معتبر نیست.")
    
@bot.message_handler(func=lambda m:True)
def english_to_speak(message):
    user_text = str(message.chat.id)
    sound = gtts.gTTS(user_text,lang="en",slow=False)
    sound.save("Assignment_9/voice.mp3")
    with open("Assignment_9/voice.mp3", "r") as voice_reader:
        bot.send_audio(message.chat.id , voice_reader, reply_markup=markup) 

@bot.message_handler(func=lambda m:True)
def max_list(message):
    user_number = str(message.chat.id)
    list_number = [int(num) for num in user_number.split(",")]
    sort_list = sorted(list_number)
    bot.reply_to(message, sort_list[-1])

@bot.message_handler(func=lambda m:True)
def index_max_list(message):
    user_number = str(message.chat.id)
    list_number = [int(num) for num in user_number.split(",")]
    max_index = list_number.index(max(list_number))
    bot.reply_to(message, max_index)

bot.infinity_polling()
