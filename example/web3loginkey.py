from eth_account import Account

private_key = "0xYOUR_PRIVATE_KEY"
account = Account.from_key(private_key)

print(f"Login successful! Account address: {account.address}")