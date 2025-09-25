from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توکن ربات خود را اینجا قرار دهید
BOT_TOKEN = "8211985796:AAFjZkuqpGsSsnHdRKowvrkWPqAjJwRQ6VE"

# تابع برای دستور /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! به ربات من خوش آمدید.\n"
        "دستورات قابل استفاده:\n"
        "/start - نمایش این پیام\n"
        "/help - راهنمایی\n"
        "شما می‌توانید هر متنی هم ارسال کنید!"
    )

# تابع برای دستور /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "من یک ربات ساده هستم!\n"
        "فقط پیام شما را تکرار می‌کنم."
    )

# تابع برای پاسخ به پیام‌های متنی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == "group":
        if text.startswith("@YourBotUsername"):
            text = text.replace("@YourBotUsername", "").strip()
        else:
            return

    response = f"شما گفتید: {text}"
    await update.message.reply_text(response)

# تابع برای خطاها
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"خطا رخ داد: {context.error}")

# تابع اصلی
def main():
    print("ربات در حال راه‌اندازی...")
    
    # ساخت اپلیکیشن
    app = Application.builder().token(BOT_TOKEN).build()

    # اضافه کردن handlerها
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # اضافه کردن handler خطا
    app.add_error_handler(error_handler)

    # شروع ربات (Polling)
    print("ربات در حال گوش دادن...")
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()