from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_TOKEN)
        updater.dispatcher.add_handler(CommandHandler("auth", self.make_aut))

        updater.start_polling()
        updater.idle()

    def make_aut(self, bot: Bot, update: Update) -> None:
        telegram_auth_token = ""  # TODO: to get it from command's args

        try:
            user: User = User.objects.get(telegram_auth_token=telegram_auth_token)

            user.telegram_chat_id = update.effective_chat["id"]
            user.telegram_username = update.effective_chat["username"]
            user.save(update_fields=["telegram_chat_id", "telegram_username"])

            # TODO: to write "OK
        except user.DoesNotExist:
            ...  # TODO: to write user was not found
        except Exception as e:
            raise e
