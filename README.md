# Blockchain Transaction Analyzer

A Python tool to fetch and analyze Ethereum transactions using the Etherscan API. It exports results to CSV for easy review.

## Features
- Fetches up to 1000 transactions for any Ethereum address
- Saves transactions as a CSV file
- Simple command-line interface

## Installation

1. Install Python 3.x
2. Install required packages:

pip install requests pandas

## Usage

1. Get your Etherscan API key: https://etherscan.io/myapikey
2. Replace `"YOUR_API_KEY"` in `analyzer.py` with your actual key.
3. Run the script:
python analyzer.py

text
4. Enter the Ethereum address when prompted.
5. Open `transactions_report.csv` to view results.

