# Telegram Xabarni O'zgartiruvchi Bot

Ushbu bot kanalga yuborilgan xabarlarni avtomatik ravishda o'zgartiradi va maxsus formatga keltiradi.

## O'rnatish

1. Kodni klonlang:
   ```bash
   git clone https://github.com/jasurhaydarovcode/autoTahrirlaBot.git
   cd autoTahrirlaBot
   ```
2. Kutubxonalarni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```
3. `.env` faylini yarating va quyidagi ma'lumotlarni kiriting:
   ```
   BOT_TOKEN=telegram_bot_tokeningiz
   CHANNEL_LINK=@kanal_nomi_yoki_id_maxviy_url
   ```
4. Botni ishga tushiring:
   ```bash
   python main.py
   ```