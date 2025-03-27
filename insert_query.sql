INSERT INTO stock_prices
(
    symbol, 
    last_price, 
    volume, 
    trade_timestamp, 
    timestamp
)
VALUES(%s, %s, %s, %s, NOW())  