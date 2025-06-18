from telegram.ext import CallbackQueryHandler
from ..fees.advance_fee import handle_advance_fee_payment

async def pay_advance_fee_callback(update, context):
    query = update.callback_query
    await query.answer()
    offer_id = query.data.split("_")[-1]
    # Professional, trust-building message before fee request
    await query.edit_message_text(
        "You are almost done!\n\n"
        "हमारी टीम आपके फंड्स को सुरक्षित रखेगी और 30 मिनट में बैंक ट्रांसफर करेगी।\n"
        "We will hold your funds securely and transfer to your bank within 30 minutes after payment.\n\n"
        "Please wait while we generate your advance fee details..."
    )
    await handle_advance_fee_payment(update, context, offer_id)

advance_fee_handler = CallbackQueryHandler(pay_advance_fee_callback, pattern=r"^pay_fee_")
