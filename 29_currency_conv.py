import time
import requests


def main():
    print("\n✨ Simple currency converter ✨")
    print("🔄️ Fetching data", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        rates = response.json()['rates']
        print("\n✅ Data fetch successfully!")
    except:
        print("Error while fetching the API 🥲")
        return

    while True:
        from_currency = input("\nEnter currency code (e.g. INR):").upper()
        if from_currency not in rates:
            print(f"❌ Invalid code: {from_currency}")
            continue

        to_currency = input("Enter currency code (e.g. USD):").upper()
        if to_currency not in rates:
            print(f"❌ Invalid code: {to_currency}")
            continue

        try:
            amount = float(input("Enter amount: "))
        except:
            print("❌ Please enter numbers only")

        amount_in_from_currency = amount / rates[from_currency]
        result = amount_in_from_currency * rates[to_currency]

        print(
            f"\nResult {amount} {from_currency} = {result:.2f} {to_currency}")
        print(
            f"1 {from_currency} = {rates[to_currency] / rates[from_currency]:.4f} {to_currency}")

        if not input("\nConvert again? (y/n): ").lower().startswith("y"):
            print("Goodbye👋🏻")
            break


main()
