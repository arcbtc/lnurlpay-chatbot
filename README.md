# lnurlpay-chatbot

## Simple LNURL webhook chatbot webpage

### Installation

Clone this repo:

    git clone https://github.com/arcbtc/lnurlpay-chatbot.git

Install Redis:

    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    sudo make install
    nohup redis-server &

Install pipenv and libraries:

    cd ~/lnurlpay-chatbot
    sudo apt install pipenv
    pipenv install flask-sse gunicorn gevent pyqrcode
    pipenv shell
    gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8000
