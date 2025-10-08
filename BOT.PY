import warnings
warnings.filterwarnings("ignore", category=UserWarning)
# BOT_TOKEN = "8482151806:AAH7jp2rCk6xjrUD9QddDTJpDZSUO6JFqII"
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests


BOT_TOKEN = "8482151806:AAH7jp2rCk6xjrUD9QddDTJpDZSUO6JFqII"
API_URL = "https://api.yabes-desu.workers.dev/ai/tool/txt2video?prompt="

def start(update, context):
    update.message.reply_text("👋 Hi! THIS BOT MAKE BYE QASIM JIHO.")
    update.message.reply_text("🎬 Send me a text and I’ll generate a video for you!")

def handle_message(update, context):
    prompt = update.message.text
    update.message.reply_text("⏳ Generating your video... please wait! Sorry for little wait ")

    try:
        res = requests.get(API_URL + prompt)
        video_url = res.text.strip()
        if video_url.startswith("http"):
            context.bot.send_video(chat_id=update.effective_chat.id, video=video_url,
                                   caption=f"🎥 Prompt: {prompt}")
        else:
            update.message.reply_text("⚠️ Couldn’t generate video.")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
