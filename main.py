import telebot
from constants import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)


# start
@bot.message_handler(commands=["Hello"])
def selamat_datang(msg):
    bot.reply_to(
        msg, 'Selamat datang di bot kami, apa kamu butuh kata motivasi belajar?')
    chatid = msg.chat.id
    bot.send_message(
        chatid,  "Pendidikan bukan cuma pergi ke sekolah dan mendapatkan gelar. Tapi juga soal memperluas pengetahuan dan menyerap ilmu kehidupan")


@bot.message_handler(commands=["iya"])
def selamat_datang(msg):
    bot.reply_to(
        msg, 'Jangan pernah menyerah jika kamu masih ingin mencoba. Jangan biarkan penyesalan datang karena kamu selangkah lagi untuk menang. Terkadang kesulitan harus kamu rasakan lebih dulu sebelum kebahagiaan yang sempurna datang kepadamu')


@bot.message_handler(commands=["lagi"])
def selamat_datang(msg):
    bot.reply_to(
        msg, 'Kalau mau menunggu sampai kita siap, kita akan menghabiskan sisa hidup kita hanya untuk menunggu')


@bot.message_handler(commands=["cukup"])
def selamat_datang(msg):
    bot.reply_to(
        msg, 'Terima kasih sudah berkunjung di bot kami')
    chatid = msg.chat.id
    bot.send_message(
        chatid,  "Jangan pernah pantang menyerah yaaaa")


bot.polling()
