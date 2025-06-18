from telegram.ext import CommandHandler, MessageHandler, filters
from ..support.ticket import SupportTicket
from datetime import datetime

async def support(update, context):
    # Friendly, professional greeting for Indian/English-speaking users
    text = (
        "Hello! Welcome to our secure escrow service.\n"
        "How can I help you today?\n\n"
        "हमारी टीम आपकी सहायता के लिए यहाँ है।\n"
        "Please type your question or describe your issue in simple words.\n"
        "(No need to use any special commands!)"
    )
    await update.message.reply_text(text)

def detect_and_handle_support(update, context):
    # This handler will auto-create a support ticket for any message that seems like a question or issue
    user_message = update.message.text
    if user_message and len(user_message) > 10:
        ticket = SupportTicket(
            telegram_id=str(update.effective_user.id),
            question=user_message,
            status="open",
            created_at=datetime.utcnow()
        )
        ticket.save()
        reply = (
            "Thank you for reaching out! Your support request has been received.\n"
            "हमारी टीम जल्द ही आपसे संपर्क करेगी।\n"
            "Our team will get back to you soon."
        )
        return update.message.reply_text(reply)

support_handler = CommandHandler("support", support)
support_message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, detect_and_handle_support)

def register_support_handlers(application):
    application.add_handler(support_handler)
    application.add_handler(support_message_handler)
