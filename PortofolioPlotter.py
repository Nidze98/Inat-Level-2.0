import matplotlib.pyplot as plt

class PortfolioPlotter:
    @staticmethod
    def plot_token_values(token_values):
        tokens = list(token_values.keys())
        values = list(token_values.values())

        plt.figure(figsize=(10, 6))
        bars = plt.bar(tokens, values, color='skyblue')
        plt.xlabel('Token')
        plt.ylabel('Value (USD)')
        plt.title('Token values in Portfolio')
        plt.xticks(rotation=45)

        for bar, value in zip(bars, values):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10, round(value, 2), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_token_distribution(token_balances):
        tokens = list(token_balances.keys())
        balances = list(token_balances.values())

        plt.figure(figsize=(10, 6))
        bars = plt.bar(tokens, balances, color='skyblue')
        plt.xlabel('Token')
        plt.ylabel('Balance')
        plt.title('Token Distribution in Portfolio')
        plt.xticks(rotation=45)

        for bar, value in zip(bars, balances):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10, round(value, 2), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_token_value_percentage(token_values):
        total_portfolio_value = sum(token_values.values())

        token_percentages = {token: (value / total_portfolio_value) * 100 for token, value in token_values.items()}

        threshold_percentage = 2
        significant_tokens = {token: percentage for token, percentage in token_percentages.items() if percentage >= threshold_percentage}
        other_percentage = 100 - sum(significant_tokens.values())

        if other_percentage > 0:
            significant_tokens['Others'] = other_percentage

        plt.figure(figsize=(8, 8))
        patches, texts, _ = plt.pie(significant_tokens.values(), labels=significant_tokens.keys(), autopct='%1.1f%%', startangle=140)

        for text in texts:
            text.set_color('lightblue')
            text.set_fontsize(12)

        plt.title('Token Value percentage in Portfolio (USD)', fontsize=16, color='lightblue')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_portfolio_value(portfolio_values):
        plt.figure(figsize=(10, 6))
        addresses = ["Address 1 EOA", "Address 2 EOA",
                    "Address contract" ] 
        bars = plt.bar(addresses, portfolio_values, color='lightgreen')
        plt.xlabel('Addresses')
        plt.ylabel('Portfolio Value (USD)')
        plt.title('Portfolio Value by Address')
        for bar, value in zip(bars, portfolio_values):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10, round(value, 2), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()
