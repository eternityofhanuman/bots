from telegram.ext import MessageHandler, filters
from ..support.ticket import SupportTicket
from datetime import datetime

async def submit_ticket(update, context):
    question = update.message.text.strip()
    if not question or len(question) < 10:
        await update.message.reply_text("Please describe your issue in detail.\nकृपया अपनी समस्या विस्तार से लिखें।")
        return
    ticket = SupportTicket(
        telegram_id=str(update.effective_user.id),
        question=question,
        status="open",
        created_at=datetime.utcnow()
    )
    ticket.save()
    await update.message.reply_text("Your support ticket has been submitted.\nआपका सपोर्ट टिकट सबमिट हो गया है। हमारी टीम जल्द ही आपसे संपर्क करेगी।")

submit_ticket_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, submit_ticket)
