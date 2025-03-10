import json
import yfinance as yf

def lambda_handler(event, context):

    # interval can be “1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, 
    #                 “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”
    # period can be '750d', 'max'  

    interval = '1m'
    period = '2d'
    code = '^HSI'
    ticker = yf.Ticker(code)
    histData = ticker.history(period=period,interval=interval,auto_adjust = False) 
    print(histData)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! v1')
    }

if __name__ == "__main__":
    print(lambda_handler({}, {}))