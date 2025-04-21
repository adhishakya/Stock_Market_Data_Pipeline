# Stock_Market_Data_Pipeline

This system fetches real-time stock data from Finnhub using WebSocket, streams it via Kafka, stores it in PostgreSQL, and visualizes it through a Streamlit dashboard using Plotly.

## Flow Diagram

![StockMarketFlowDiagram](https://github.com/user-attachments/assets/a54a53f7-da90-4cd0-9f99-11ad4a3d9ff7)

## Stack Used

- WebSocket – For real-time data feed from Finnhub.

- Kafka – Handles real-time data streaming (Producer & Consumer setup).

- PostgreSQL – Stores the stock price data.

- Pandas – Used for DML statements.

- Streamlit – Builds the UI for data visualization.

- Plotly – Interactive charts for real-time stock prices.

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/adhishakya/Stock_Market_Data_Pipeline.git
cd Stock_Market_Data_Pipeline
```

### 2. Setup Environment Variables
```Python
URL= wss://your_finnhub_socket
TOKEN = your_finnhub_token
DB_NAME = your_db
DB_USER = your_user
DB_PASS = your_password
DB_HOST = localhost
DB_PORT = 5432
STREAM_TOPIC = your_kafka_topic

```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

```

### 4. Start required services
- Start Zookeeper and Kafka:
```bash
# Example (if using local install)
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties

```
- Start PostgreSQL and ensure the required table/schema is created.

### 5. Run the App
- Listener and Producer (WebSocket to Kafka):
```bash
python main.py
```

- Consumer (Kafka to PostgreSQL)
```bash
python consumer.py
```

- Streamlit Visualization
```bash
streamlit run chart.py
```

## Demo

- Data Storage into Database
  
![Database](https://github.com/user-attachments/assets/ffb3b871-d36e-48d7-a715-b97bd9935803)

- Stock Data
  
![ChartHeader](https://github.com/user-attachments/assets/84156e78-cf4d-4749-98f2-c3de2d8d6256)
![AAPL](https://github.com/user-attachments/assets/1f23e712-03ae-46b9-8ae2-e70e9d8f45f5)
![AMZN](https://github.com/user-attachments/assets/0c267525-318a-4c2e-af9e-4dc7a6bdbe47)
![GOOG](https://github.com/user-attachments/assets/46322552-9f2e-4eb1-a152-553bb5b2d4a2)
![META](https://github.com/user-attachments/assets/3162c7b0-3687-4305-aaa7-b39d130b72b8)
![NFLX](https://github.com/user-attachments/assets/cc4637b3-2e13-4a79-a6f0-0575838a4e8c)

## API Source
- [Finnhub Stock APIs](https://finnhub.io/)
