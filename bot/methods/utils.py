import json

from telegram import Update


class Utils:

    @staticmethod
    async def send_msg(update: Update, msgs: list[str], reply_markup, markdown: bool = True) -> None:
        for msg in msgs:
            msg = msg.replace(".", "\\.")
            if markdown:
                await update.message.reply_text(msg,
                                                parse_mode='MarkdownV2',
                                                reply_markup=reply_markup)
            else:
                await update.message.reply_text(msg,
                                                reply_markup=reply_markup)

    @staticmethod
    def pretty_print_json(data: dict) -> list[str]:
        if len(json.dumps(data)) > 3200:
            result: list = []
            for key, value in data.items():
                result.append(f"```\n{json.dumps({key: value}, indent=2)}\n```")
            return result
        else:
            return [f"```\n{json.dumps(data, indent=2)}\n```"]