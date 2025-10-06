import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# تنظیمات
BOT_TOKEN = os.environ.get('BOT_TOKEN')
MINIAPP_URL = os.environ.get('MINIAPP_URL', '')  # بعد از دیپلوی تنظیم می‌شود

# لاگینگ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /start"""
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("🎮 باز کردن مینی اپ", web_app={'url': MINIAPP_URL})],
        [InlineKeyboardButton("ℹ️ راهنما", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_html(
        f"سلام {user.mention_html()}! 👋\n\n"
        "به ربات نمونه مینی اپ خوش آمدید!\n"
        "روی دکمه زیر کلیک کن تا مینی اپ باز شود:",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /help"""
    await update.message.reply_text(
        "🤖 ربات مینی اپ نمونه\n\n"
        "دستورات:\n"
        "/start - شروع ربات\n"
        "/help - راهنما\n"
        "/miniapp - باز کردن مینی اپ"
    )

async def miniapp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """دستور /miniapp"""
    keyboard = [[InlineKeyboardButton("🎮 باز کردن مینی اپ", web_app={'url': MINIAPP_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مینی اپ را باز کن:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """مدیریت کلیک روی دکمه‌ها"""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'help':
        await query.edit_message_text(
            "📖 راهنمای مینی اپ:\n\n"
            "1. روی 'باز کردن مینی اپ' کلیک کن\n"
            "2. در مرورگر داخلی مینی اپ باز میشه\n"
            "3. میتونی از امکاناتش استفاده کنی\n"
            "4. داده‌ها به ربات ارسال میشن"
        )

def main():
    """اجرای ربات"""
    if not BOT_TOKEN:
        logger.error("لطفا BOT_TOKEN را تنظیم کنید")
        return
    
    # ساخت اپلیکیشن
    application = Application.builder().token(BOT_TOKEN).build()
    
    # افزودن هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("miniapp", miniapp_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # اجرای ربات
    logger.info("ربات در حال اجراست...")
    application.run_polling()

if __name__ == '__main__':
    main()
