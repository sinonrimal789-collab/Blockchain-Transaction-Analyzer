import requests
import pandas as pd

API_KEY = "4QYZQNDE95G4UKP4NPBA1Y1K5W9FU2CQXN"


def get_transactions(address):
    url = (
        f"https://api.etherscan.io/v2/api"
        f"?chainid=1"
        f"&module=account"
        f"&action=txlist"
        f"&address={address}"
        f"&startblock=0&endblock=latest"
        f"&page=1&offset=1000&sort=asc"
        f"&apikey={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    if data["status"] == "1":
        print(f"Fetched {len(data['result'])} transactions successfully!")
        return pd.DataFrame(data["result"])
    else:
        print("API Error:", data["message"], "| Reason:", data.get("result"))
        return pd.DataFrame()


address = input("Enter Ethereum address: ").strip()
tx_df = get_transactions(address)

tx_df.to_csv('ethereum_transactions.csv', index=False)
print("Saved transactions to ethereum_transactions.csv")
