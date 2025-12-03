def main():
    try:
        original = float(input("Introduce el precio original: ").strip())
        discount_pct = float(input("Introduce el porcentaje de descuento: ").strip())
    except ValueError:
        print("Entrada no válida. Introduce valores numéricos.")
        return

    final_price = original * (1 - discount_pct / 100)
    print(f"Precio final: {final_price:.2f}")

if __name__ == "__main__":
    main()
