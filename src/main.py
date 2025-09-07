from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from src.services.tg_service import start_command, show_help, handle_message
from src.core.config import tg_settings


app = Application.builder().token(tg_settings.token).build()
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", show_help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print("Polling Telegram API...")
app.run_polling(poll_interval=1.0)
print("Bot stopped.")