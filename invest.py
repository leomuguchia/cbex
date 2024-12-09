from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)

def calculate_cbex_growth(initial_investment, daily_signals, growth_rate, days):
    balance = initial_investment
    total_growth = 0.0

    table = PrettyTable()
    table.field_names = [
        "Day",
        Fore.YELLOW + "Signal 1 Growth" + Style.RESET_ALL,
        Fore.CYAN + "Balance After Signal 1" + Style.RESET_ALL,
        Fore.YELLOW + "Signal 2 Growth" + Style.RESET_ALL,
        Fore.CYAN + "Balance After Signal 2" + Style.RESET_ALL,
    ]
    table.align = "r"

    for day in range(1, days + 1):
        signal_1_growth = balance * growth_rate
        balance_after_signal_1 = balance + signal_1_growth
        signal_2_growth = balance_after_signal_1 * growth_rate
        balance_after_signal_2 = balance_after_signal_1 + signal_2_growth

        balance = balance_after_signal_2
        total_growth += signal_1_growth + signal_2_growth

        table.add_row([
            f"Day {day}",
            f"${signal_1_growth:.2f}",
            f"${balance_after_signal_1:.2f}",
            f"${signal_2_growth:.2f}",
            f"${balance_after_signal_2:.2f}",
        ])

    print("\n" + Fore.GREEN + "Investment Growth Analysis (CBEX)" + Style.RESET_ALL)
    print("=" * 50)
    print(table)
    print("=" * 50)
    print(f"{Fore.GREEN}Summary:")
    print(f"Starting Balance: {Fore.YELLOW}${initial_investment:.2f}")
    print(f"Total Growth: {Fore.YELLOW}${total_growth:.2f}")
    print(f"Final Balance After {days} Days: {Fore.YELLOW}${balance:.2f}")
    print(f"Percentage Growth: {Fore.YELLOW}{(total_growth / initial_investment) * 100:.2f}%")
    print("=" * 50)

def main():
    try:
        print(Fore.CYAN + "\nWelcome to CBEX Calc!" + Style.RESET_ALL)
        initial_investment = float(input("Enter your starting investment amount (optimal = $300): "))
        total_days = int(input("Enter the number of days to calculate growth: "))
        daily_signals = 2
        growth_rate = 0.0088
        calculate_cbex_growth(initial_investment, daily_signals, growth_rate, total_days)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter valid numbers." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
