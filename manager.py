from config import TOKEN
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , CallbackQueryHandler
from start import start
from help import help
from stop import stop
from register import register_uz , register_en , register_ru
from send_name import send_name_uz , send_name_en , send_name_ru
from gender import gender_uz , gender_en , gender_ru
from location import location_uz , location_en , location_ru
from menu import menu_uz , to_menu_uz , menu_en , to_menu_en , menu_ru , to_menu_ru
from desktop import menu_desktops_uz , menu_desktops_en , menu_desktops_ru
from phones import phones_uz , iphones_uz , samsung_uz , xiomi_uz , phones_en , iphones_en , samsung_en , xiomi_en , phones_ru , iphones_ru , samsung_ru , xiomi_ru
from airpods import airpods_uz , airpods_en , airpods_ru
from tablets import tablet_uz , samsung_tablet_uz , apple_tablet_uz , tablet_en , samsung_tablet_en , apple_tablet_en , tablet_ru , samsung_tablet_ru , apple_tablet_ru
from watches import watches_uz , watches_en ,watches_ru
from send_idea import send_idea_uz , send_idea_en , send_idea_ru
from settings import (settings_uz , change_language_uz , change_phone_number_uz , settings_en , change_language_en ,
change_phone_number_en , settings_ru , change_language_ru , change_phone_number_ru)
from order import order_uz , order_en , order_ru
from info import (about_phone_number_uz , about_phone_number_en , about_phone_number_ru )


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    # CommandHandler
    dispatcher.add_handler(CommandHandler("start" , start))
    dispatcher.add_handler(CommandHandler("help" , help))
    dispatcher.add_handler(CommandHandler("stop" , stop))
    
    # MessageHandler
    dispatcher.add_handler(CallbackQueryHandler(register_uz, pattern="^uz$"))
    dispatcher.add_handler(CallbackQueryHandler(register_en, pattern="^us$"))
    dispatcher.add_handler(CallbackQueryHandler(register_ru, pattern="^ru$"))
    
    # With Uzbek
    dispatcher.add_handler(MessageHandler(Filters.text("Ma'lumotni yuborish!🪪") , send_name_uz))
    dispatcher.add_handler(MessageHandler(Filters.regex("^(Erkak 👨🏻|Ayol 👩🏻‍🦱)$") , gender_uz))
    dispatcher.add_handler(MessageHandler(Filters.contact , location_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Tashlab ketish! ⏩") , location_uz))
    dispatcher.add_handler(MessageHandler(Filters.location , menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("O'tkazib yuborish!⏩") , menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Orqaga qaytish ⏪") , to_menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Dasturni to'xtatish!🤔") , stop))
    dispatcher.add_handler(MessageHandler(Filters.text("Qurulmalar🌐") , menu_desktops_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Sozlammalar⚙️") , settings_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Tilni o'zgartirish!🔃") , change_language_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Ingliz 🇺🇸") , menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Rus 🇷🇺") , menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Telfon raqamni o'zgartirish!") , change_phone_number_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Raqamni o'zgartirish!") , about_phone_number_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Buyurtmalar 📦") , order_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Fikr qoldirish✍🏻") , send_idea_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Telefonlar 📱") , phones_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Apple 🍎") , iphones_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Samsung ✨") , samsung_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Xiomi 🔮") , xiomi_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Quloqchinlar 🎧") , airpods_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Planshetlar 📟") , tablet_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Apple 🍏") , apple_tablet_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Samsung 📱") , samsung_tablet_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Smart Watchlar ⌚") , watches_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Iphone 16 Pro Max") , to_menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Galaxy S25 Ultra") , to_menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Xiomi 15 ultra") , to_menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Mi Band 6") , to_menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Galaxy Tab 4") , to_menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("IPad Pro") , to_menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Air Pods Max 🎧") , to_menu_uz))
    
    #With English
    dispatcher.add_handler(MessageHandler(Filters.text("Submit information!🪪") , send_name_en))
    dispatcher.add_handler(MessageHandler(Filters.regex("^(Men 👨🏻|Women 👩🏻‍🦱)$") , gender_en))
    dispatcher.add_handler(MessageHandler(Filters.contact , location_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Skip! ⏩") , location_en))
    dispatcher.add_handler(MessageHandler(Filters.location , menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Skipping!⏩") , menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Come Back ⏪") , to_menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Stop the program!🤔") , stop))
    dispatcher.add_handler(MessageHandler(Filters.text("Structures🌐") , menu_desktops_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Settings⚙️") , settings_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Change the language!🔃") , change_language_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Uzbek 🇺🇿") , menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Russian 🇷🇺") , menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Change phone number!") , change_phone_number_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Change number!") , about_phone_number_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Orders 📦") , order_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Send Idea✍🏻") , send_idea_en))  
    dispatcher.add_handler(MessageHandler(Filters.text("Phones 📱") , phones_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Apple 🌐") , iphones_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Samsung 📟") , samsung_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Xiomi ✅") , xiomi_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Air Pods 🎧") , airpods_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Tablets 📟") , tablet_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Apple ✨") , apple_tablet_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Samsung 🪶") , samsung_tablet_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Smart Watches ⌚") , watches_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Iphone 15 Pro Max") , to_menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Galaxy S24 Ultra") , to_menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Xiomi 14 ultra") , to_menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Mi Band 5") , to_menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Galaxy Tab 3") , to_menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("IPad Max") , to_menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Air Pods Pro 🎧") , to_menu_en))
    
    #With Russian
    dispatcher.add_handler(MessageHandler(Filters.text("Отправить информацию!🪪") , send_name_ru))
    dispatcher.add_handler(MessageHandler(Filters.regex("^(Мужчины 👨🏻|Женщины 👩🏻‍🦱)$") , gender_ru))
    dispatcher.add_handler(MessageHandler(Filters.contact , location_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Пропускать! ⏩") , location_ru))
    dispatcher.add_handler(MessageHandler(Filters.location , menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Пропуск!⏩") , menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Возвращаться ⏪") , to_menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Остановить программу!🤔") , stop))
    dispatcher.add_handler(MessageHandler(Filters.text("Структуры🌐") , menu_desktops_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Настройки⚙️") , settings_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Изменить язык!🔃") , change_language_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Узбекский 🇺🇿") , menu_uz))
    dispatcher.add_handler(MessageHandler(Filters.text("Английский 🇺🇸") , menu_en))
    dispatcher.add_handler(MessageHandler(Filters.text("Изменить номер телефона!") , change_phone_number_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Изменить номер!") , about_phone_number_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Заказы 📦") , order_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Отправить идею✍🏻") , send_idea_ru))  
    dispatcher.add_handler(MessageHandler(Filters.text("Телефоны 📱") , phones_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Apple 📱") , iphones_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Samsung 🖐🏻") , samsung_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Xiomi 🤩") , xiomi_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Наушники 🎧") , airpods_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Планшеты 📟") , tablet_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Apple 📟") , apple_tablet_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Samsung 🤖") , samsung_tablet_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Умные часы ⌚") , watches_ru))    
    dispatcher.add_handler(MessageHandler(Filters.text("Iphone 14 Pro Max") , to_menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Galaxy S23 Ultra") , to_menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Xiomi 13 ultra") , to_menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Mi Band 9") , to_menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Galaxy Tab 2") , to_menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("IPad Mini") , to_menu_ru))
    dispatcher.add_handler(MessageHandler(Filters.text("Air Pods Pro 5 🎧") , to_menu_ru))
    

    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()