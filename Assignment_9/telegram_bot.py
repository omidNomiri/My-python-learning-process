import telebot
import random
import qrcode
from persiantools.jdatetime import JalaliDate
import gtts

bot = telebot.TeleBot("6836755262:AAET97-d45Q0Ax93tcphANQ-LWrTaQg_bRk",parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
item_markup1 = telebot.types.KeyboardButton('/QRcode')
item_markup2 = telebot.types.KeyboardButton('/game')
item_markup3 = telebot.types.KeyboardButton('/age')
item_markup4 = telebot.types.KeyboardButton('/voice')
item_markup5 = telebot.types.KeyboardButton('/max')
item_markup6 = telebot.types.KeyboardButton('/argmax')
item_markup7 = telebot.types.KeyboardButton('/help')
markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f" خوش آمدید {user_name}" )

@bot.message_handler(commands=['QRcode'])
def crating_QRcode(message):
	text=bot.send_message(message.chat.id, "جمله مورد نظر خود را به انگلیسی وارد کنید")
	bot.register_next_step_handler(text, crating_QRcode)

@bot.message_handler(commands=["game"])
def game(message):
    global number
    number = random.randint(1,100)
    bot.send_message(message.chat,id ,"بازی شروع شد.یک عدد بین 1 تا 100 انتخاب کن!")
    bot.register_next_step_handler(number,user_number)

@bot.message_handler(commands=["age"])
def birthday(message):
    bot.send_message(message.chat,id ,"لطفا سال تولد خود را به هجری شمسی وارد بکنید \n مثل:(1390-11-02)")
    bot.register_next_step_handler(birthday,user_age)

@bot.message_handler(commands=["voice"])
def english_to_speak(message):
	text=bot.send_message(message.chat.id, "جمله مورد نظر خود را به انگلیسی وارد کنید")
	bot.register_next_step_handler(text, english_to_speak)

@bot.message_handler(commands=["max"])
def user_namber_list(message):
	user_nambers=bot.send_message(message.chat.id, "اعداد لیست رو با استفاده از ',' از هم جدا کنید")
	bot.register_next_step_handler(user_nambers, max_list)
      
@bot.message_handler(commands=["index_max"])
def number_list(message):
	user_nambers=bot.send_message(message.chat.id, "اعداد لیست رو با استفاده از ',' از هم جدا کنید")
	bot.register_next_step_handler(user_nambers, index_max_list)

@bot.message_handler(commands=["help"])
def help_user(message):
	bot.reply_to(message, "این گزینه هایی است که میتونی از بات استفاده کنی باهاش")
	bot.send_message(message.chat.id, "QRcode: اگر بهش یه جمله بدی برات تبدیل به QRcode میکنه"
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
	QRc = open("QrCode.png")
	bot.send_photo(message.chat.id, QRc, reply_markup=markup)

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
    user_birthday = str(message.caht.id)
    try:
        birthday_year, birthday_month, birthday_day = map(int, user_birthday.split("-"))

        JalaliDate(birthday_year, birthday_month, birthday_day)

        dob_date = JalaliDate(birthday_year, birthday_month, birthday_day)
        today_date = JalaliDate.today()

        age_timedelta = today_date - dob_date
        age_days = age_timedelta.days
        age_years = age_days // 365
        day2 = age_days - age_years * 365
        age_month = day2 // 30
        month2 = day2 % 30
        all = age_years, age_month, month2
        bot.reply_to(message, all, reply_markup=markup)
    except ValueError:
        return "تاریخ وارد شده معتبر نیست."
    
@bot.message_handler(func=lambda m:True)
def english_to_speak(message):
    user_text = str(message.chat.id)
    sound = gtts.gTTS(user_text,lang="en",slow=False)
    sound.save("Assignment_9/voice.mp3")
    voice_reader = open("Assignment_9/voice.mp3", 'rb')
    bot.send_audio(message.chat.id , voice_reader, reply_markup=markup) 

@bot.message_handler(func=lambda m:True)
def max_list(message):
    user_number = str(message.chat.id)
    list_number = user_number.split(",")
    sort_list = sorted(list_number)
    bot.reply_to(sort_list[0])

@bot.message_handler(func=lambda m:True)
def index_max_list(message):
    user_number = str(message.chat.id)
    list_number = user_number.split(",")
    max_index = list_number.index(max(list_number))
    bot.reply_to(max_index)

bot.infinity_polling()