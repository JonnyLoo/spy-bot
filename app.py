import requests, json
from chalice import Chalice

app = Chalice(app_name='spy-bot')

# alpaca
BASE_URL = 'https://paper-api.alpaca.markets'
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)

# creds
API_KEY = 'PK0ADGX9KSS5RP4DNXP7'
SECRET_KEY = 'fTGr26MzQvK8l8bNc6hbuZ1lzgJ7ciaX9LnsdL8U'
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

#buy stock
@app.route('/buy', methods=['POST'])
def buy():
    request = app.current_request
    webhook_message = request.json_body

    data = {
        'symbol': webhook_message['ticker'],
        'qty': 1,
        'side': 'buy',
        'type': 'limit',
        'limit_price': webhook_message['close'],
        'time_in_force': 'gtc',
        'order_class': 'bracket',
        'take_profit': {
            'limit_price': webhook_message['close'] * 1.05
        },
        'stop_loss': {
            'stop_price': webhook_message['close'] * 0.98,
        }
    }

    response = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return {
        'message': 'bought something',
        'webhook_message': webhook_message,
        'response': json.loads(response.content)
    }

# sell stock
@app.route('/sell', methods=['POST'])
def sell():
        return {
            'message': 'sold something'
        }
