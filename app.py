from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for Matplotlib
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! <a href="/dashboard">Go to Dashboard</a>'

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    stock_data_html = None
    plot_url = None
    ticker_symbol = 'AAPL' # Default ticker

    if request.method == 'POST':
        ticker_symbol = request.form.get('ticker', 'AAPL').upper()
    
    try:
        # Fetch stock data
        stock = yf.Ticker(ticker_symbol)
        hist_data = stock.history(period="1y") # Get 1 year of data

        if not hist_data.empty:
            # Prepare data for HTML table
            stock_data_html = hist_data.tail().to_html(classes='table table-striped')

            # Generate plot
            plt.figure(figsize=(10, 5))
            plt.plot(hist_data.index, hist_data['Close'], label=f'{ticker_symbol} Close Price')
            plt.title(f'{ticker_symbol} Stock Price Over Last Year')
            plt.xlabel('Date')
            plt.ylabel('Price (USD)')
            plt.legend()
            plt.grid(True)
            plt.tight_layout()

            # Save plot to a bytes buffer
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plt.close() # Close the plot to free memory
            
            # Encode plot to base64 string
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
            plot_url = f"data:image/png;base64,{plot_url}"
        else:
            stock_data_html = "<p>Could not retrieve data for ticker: {}</p>".format(ticker_symbol)

    except Exception as e:
        stock_data_html = f"<p>Error fetching data for {ticker_symbol}: {str(e)}</p>"

    return render_template('index.html', 
                           stock_data_html=stock_data_html, 
                           plot_url=plot_url, 
                           ticker=ticker_symbol)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)