CREATE EXTENSION IF NOT EXISTS timescaledb;
CREATE TABLE IF NOT EXISTS stock_prices(
    id SERIAL,
    symbol TEXT,
    last_price NUMERIC (10,2),
    volume NUMERIC (20,10),
    trade_timestamp BIGINT,
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (symbol, timestamp  )
);

SELECT create_hypertable(
    'stock_prices',
    'timestamp'
);

