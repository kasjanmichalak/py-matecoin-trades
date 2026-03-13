import json


from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is None:
            trade["bought"] = 0
        if trade["sold"] is None:
            trade["sold"] = 0
        matecoin_account += Decimal(trade["bought"]) - Decimal(trade["sold"])
        earned_money += ((Decimal(trade["bought"]) - Decimal(trade["sold"]))
                         * Decimal(trade["matecoin_price"]))

    matecoin_account = str(matecoin_account)
    earned_money = str(earned_money)
    result = {"earned_money": earned_money,
              "matecoin_account": matecoin_account}

    with open("profit.json", "w") as f:
        json.dump(result, f)
