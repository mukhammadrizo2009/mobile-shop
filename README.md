# mobile-shopapple_bro_bot/
│
├── bot.py                   # Asosiy fayl — botni ishga tushirish
├── config.py                # Token, admin ID, boshqa sozlamalar
├── requirements.txt         # Kutubxonalar ro‘yxati
├── README.md                # Loyihaning qisqacha tavsifi
│
├── keyboards/               # Inline va Reply klaviaturalari
│   ├── __init__.py
│   ├── main_menu.py         # Asosiy menyu tugmalari
│   ├── phones_menu.py       # Telefonlar bo‘limi tugmalari
│   ├── tablets_menu.py      # Planshetlar bo‘limi tugmalari
│   ├── watches_menu.py      # Soatlar bo‘limi tugmalari
│   ├── accessories_menu.py  # Quloqchinlar va boshqa gadget tugmalari
│
├── handlers/                # Har bir bo‘lim uchun handlerlar
│   ├── __init__.py
│   ├── start.py             # /start va bosh menyu
│   ├── phones.py            # Telefonlar bo‘limi
│   ├── tablets.py           # Planshetlar bo‘limi
│   ├── watches.py           # Smart soatlar bo‘limi
│   ├── accessories.py       # Quloqchinlar va boshqa aksessuarlar
│   ├── payment.py           # To‘lov tizimi va buyurtma
│
├── data/                    # Ma'lumotlar bazasi yoki JSON fayllar
│   ├── __init__.py
│   ├── products.json        # Mahsulotlar ro‘yxati (model, narx, rang va h.k.)
│
├── utils/                   # Qo‘shimcha yordamchi funksiyalar
│   ├── __init__.py
│   ├── helpers.py           # Formatlash, log yozish va h.k.
│   ├── constants.py         # Doimiy qiymatlar (callback_data nomlari)
│
└── logs/
    └── bot.log              # Bot ishlashidagi loglar