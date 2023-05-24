def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    return bitcoin_amount * bitcoin_value_usd

investment_in_bitcoin = 1.2
bitcoin_value_usd = 40000

usd_value = bitcoinToUSD(investment_in_bitcoin, bitcoin_value_usd)

if usd_value <= 30000:
    print("Your investment in Bitcoin has fallen below $30,000!")
else:
    print("Your investment in Bitcoin is above $30,000.")

# The flag is: THM{BITC0IN_INVESTOR}