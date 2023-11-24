import random
import datetime
import datetime
from persiantools.jdatetime import JalaliDate
import qrcode
import gtts
import telebot
from telebot import types

bot = telebot.TeleBot("Token place", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
item_markup1 = telebot.types.KeyboardButton("/game")
item_markup2 = telebot.types.KeyboardButton("/age")
item_markup3 = telebot.types.KeyboardButton("/voice")
item_markup4 = telebot.types.KeyboardButton("/max")
item_markup5 = telebot.types.KeyboardButton("/index_max")
item_markup6 = telebot.types.KeyboardButton("/qrcode")
item_markup7 = telebot.types.KeyboardButton("/help")
markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)

#start message
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f" خوش آمدید {user_name}", reply_markup=markup)

number = random.randint(1, 100)
chat_id = None

#game
@bot.message_handler(commands=["game"])
def start_game(message):
    global chat_id
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_markup1 = types.KeyboardButton("/new_game")
    markup.add(item_markup1)
    msg = bot.send_message(chat_id, "یک عدد بین 1 تا 100 حدس بزنید", reply_markup=markup)
    bot.register_next_step_handler(msg, guess_number)

def guess_number(message):
    global number
    guess = int(message.text)
    if guess > number:
        msg = bot.send_message(chat_id, "عددی که انتخاب کردی بزرگتر از عدد درسته. پس بیا پایین تر!")
        bot.register_next_step_handler(msg, guess_number)
    elif guess < number:
        msg = bot.send_message(chat_id, "عددی که انتخاب کردی کوچکتر از عدد درسته. پس برو بالا تر!")
        bot.register_next_step_handler(msg, guess_number)
    elif guess == number:
        bot.send_message(chat_id, "برنده شدی!")
        markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)

@bot.message_handler(commands=["new_game"])
def new_game(message):
    global number
    number = random.randint(1, 100)
    msg = bot.send_message(chat_id, "یک عدد جدید بین 1 تا 100 حدس بزنید")
    bot.register_next_step_handler(msg, guess_number)

#age 
@bot.message_handler(commands=["age"])
def get_birthday(message):
    msg = bot.send_message(message.chat.id, "لطفا تاریخ تولد خود را به صورت YYYY-MM-DD وارد کنید")
    bot.register_next_step_handler(msg, calculate_age)

def calculate_age(message):
    birthday_year, birthday_month, birthday_day = map(int, message.text.split("-"))
    miladi_date = JalaliDate(birthday_year, birthday_month, birthday_day).to_gregorian()
    age_timedelta = datetime.date.today() - miladi_date
    age_years = age_timedelta.days // 365
    bot.send_message(message.chat.id, f"سن شما {age_years} سال است")

#text to voice
@bot.message_handler(commands=["voice"])
def get_text(message):
    msg = bot.send_message(message.chat.id, "لطفا یک جمله به انگلیسی وارد کنید")
    bot.register_next_step_handler(msg, text_to_voice)

def text_to_voice(message):
    user_text = message.text
    voice = gtts.gTTS(user_text, lang="en", slow=False)
    voice.save("/home/voice.mp3")
    with open("/home/voice.mp3", "rb") as voice_file:
      bot.send_voice(message.chat.id, voice_file)

#max
@bot.message_handler(commands=["max"])
def get_numbers(message):
    msg = bot.send_message(message.chat.id, "لطفا یک آرایه از اعداد را وارد کنید (مثلا: 14,7,78,15,8,19,20)")
    bot.register_next_step_handler(msg, print_max)

def print_max(message):
    numbers = list(map(int, message.text.split(",")))
    max_number = max(numbers)
    bot.send_message(message.chat.id, f"بزرگترین عدد: {max_number}")

#max index
@bot.message_handler(commands=["index_max"])
def get_numbers(message):
    msg = bot.send_message(message.chat.id, "لطفا یک آرایه از اعداد را وارد کنید (مثلا: 14,7,78,15,8,19,20)")
    bot.register_next_step_handler(msg, print_index_max)

def print_index_max(message):
    numbers = list(map(int, message.text.split(",")))
    max_index = numbers.index(max(numbers))
    bot.send_message(message.chat.id, f"اندیس بزرگترین عدد: {max_index}")

#QRcode
@bot.message_handler(commands=["qrcode"])
def get_text(message):
    msg = bot.send_message(message.chat.id, "لطفا متن وارد کنید")
    bot.register_next_step_handler(msg, create_QRCode)

def create_QRCode(message):
    qr_img = qrcode.make(message.text)
    qr_img.save("/home/qrcode.png")
    with open("/home/qrcode.png", "rb") as qr_file:
        bot.send_photo(message.chat.id, qr_file)

#help
@bot.message_handler(commands=["help"])
def help_user(message):
    bot.reply_to(message, "این گزینه هایی است که میتونی از بات استفاده کنی")
    bot.send_message(message.chat.id, "qrcode: اگر بهش یه جمله بدی برات تبدیل به QRcode میکنه"
                                    "\n game: بازی حدس کلمات شروع میشه"
                                    "\n age: اگر تاریخ تولدت رو بگی دقیق حساب میکنه که چند سالت هست"
                                    "\n voice: اگر بهش یه جمله انگلیسی بدی بهت یهویس از همون جملت میده"
                                    "\n max: اگر یه لیست از اعداد بدی بهت میگه کدومش بزرگ تره"
                                    "\n index_max: اگر یه لیست از اعداد بدی بهت میگه توی کدوم خونه بزرگترین عدد هست"
                                    "\n help: این هم که الان زدی ولی خب این بهت لیست کامند هارو نشون میده")

bot.infinity_polling()
