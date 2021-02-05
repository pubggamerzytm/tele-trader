# Bot token provided by BotFather

# TOKEN_TEST = "1607441057:AAGYbipu1DURhbrQcJsBShWWaHVrwHdyTEs"
from sqlalchemy import create_engine


 PUBLIC_KEY = "9fc5e16e1f0acc50f494815ac08ba9eac39a6097227902e57691dc5c76d756f2"
 PRIVATE_KEY = "f80798E3C03b12d72a5c3e6987A1fd469F14e04d303cF7e9F1E257D475135390"
 Merchant_ID = "0a9989dabbcfdde258c70f33bb3ca123"
 IPN_secret = "premiumidseller"
 ADMIN_ID = 1053579181

DEBUG = not True

if DEBUG==False:
    print("\033[1;35;40m Running in production mode")
    TOKEN = "1607441057:AAGYbipu1DURhbrQcJsBShWWaHVrwHdyTEs" #FCX trading bot
    URL = 'https://teletradingg.herokuapp.com/'
    try:
        import os
        DATABASE_URL = os.environ['DATABASE_URL']
    except KeyError:
        # DATABASE_URL="postgres://oilzaezgbpfuad:0c38dcf0bdd1cad9456aff15f7b6ae3cb076e5911dcbb5bf266afd5a3710e608@ec2-184-72-236-57.compute-1.amazonaws.com:5432/d3u443uoa0b5os"
        DATABASE_URL="postgres://jiuyexwrlknkee:183e46190d220e36b4401f4d6d86549ba7107653bb62ddadec6bccecd02c366a@ec2-54-246-89-234.eu-west-1.compute.amazonaws.com:5432/daprusoucv4h82"
    db_url = DATABASE_URL.split(":")

    DATABASE_URI_VAR =f'postgres+psycopg2:{db_url[1]}:{db_url[2]}:{db_url[3]}'
    engine = create_engine(DATABASE_URI_VAR, echo=True)
    print(engine)

else:
    print("\033[1;32;40m Running in Development mode")
    TOKEN = "1607441057:AAGYbipu1DURhbrQcJsBShWWaHVrwHdyTEs"

    # TOKEN = "1607441057:AAGYbipu1DURhbrQcJsBShWWaHVrwHdyTEs" #fcxtrader bot
    URL = "https://3a7a746b.ngrok.io/"
    DATABASE_URL = 'postgres+psycopg2://postgres:postgres@localhost:5432'
    ADMIN_ID = 1053579181

    SQLITE = 'sqlite:///database/database.db'
    engine = create_engine(SQLITE, echo=True, connect_args={'check_same_thread': False})
    print(engine)

