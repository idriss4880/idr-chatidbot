from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# ضع التوكن الخاص بك هنا
BOT_TOKEN = "7387194747:AAGQGiA1TYcMsGMbIDDEbnnvJ3HLG8NC-io"



# دالة لمعالجة أمر /start
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    update.message.reply_text(f"{chat_id}")

# دالة لمعالجة أي رسالة نصية
def send_chat_id(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    update.message.reply_text(f"{chat_id}")

def main():
    # إعداد البوت
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # ربط أمر /start بالدالة start
    dispatcher.add_handler(CommandHandler("start", start))

    # ربط جميع الرسائل النصية بالدالة send_chat_id
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, send_chat_id))

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
