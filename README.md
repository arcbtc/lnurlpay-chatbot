# lnurlpay-chatbot

## Simple LNURL webhook chatbot webpage

### Installation

Install Redis:

    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    sudo make install
    redis-server

Install lnurlpay-chatbot:
    
    git clone https://github.com/arcbtc/lnurlpay-chatbot.git
    lnurlpay-chatbot
    cd ~/lnurlpay-chatbot
    sudo apt install pipenv
    pipenv install flask-sse gunicorn gevent pyqrcode
    pipenv shell
    gunicorn sse:app --worker-class gevent --bind 0.0.0.0:8000

Open `http://0.0.0.0:8000`

When creating the LNURL-pay in lnbits.com set the webhook to `http://0.0.0.0:8000/message/`

Send the LNURL-pay to be turned into a QR using `http://0.0.0.0:8000/lnurl/LNURLNIH983h49834....`
