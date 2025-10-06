import os
from bot import main as bot_main
from miniapp.app import app as miniapp_app
import threading

def run_bot():
    """اجرای ربات در یک thread جداگانه"""
    bot_main()

def run_miniapp():
    """اجرای مینی اپ"""
    port = int(os.environ.get('PORT', 5000))
    miniapp_app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == '__main__':
    # اجرای همزمان ربات و مینی اپ
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # اجرای مینی اپ در thread اصلی
    run_miniapp()
