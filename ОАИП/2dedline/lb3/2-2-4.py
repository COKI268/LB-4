products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}

top_sold = max(products, key=lambda x: products[x]["sold"])
print(f"Топ продаж: {top_sold} ({products[top_sold]['sold']} шт.)")

total = sum(p["price"] * p["sold"] for p in products.values())
print(f"Выручка: {total} руб.")

top_profit = max(products, key=lambda x: products[x]["price"] * products[x]["sold"])
cash = products[top_profit]["price"] * products[top_profit]["sold"]
print(f"Топ по выручке: {top_profit} ({cash} руб.)")
