# Day 25 — Matplotlib Sales Visualization
# pip install matplotlib

import matplotlib.pyplot as plt

def plot_sales():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [1200, 1500, 1100, 1800, 2200, 2000]

    plt.figure(figsize=(9, 5))
    bars = plt.bar(months, sales, color="#4cc9f0", edgecolor="#0a1a35")
    plt.title("Monthly Sales (in USD)")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    # Annotate bars
    for bar in bars:
        y = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y + 30, f"{y}", ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig("sales_plot.png", dpi=120)
    print("📊 Plot saved as sales_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_sales()
