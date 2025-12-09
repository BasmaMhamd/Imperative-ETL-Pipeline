import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -------------------------
# 4. Utility: save plot
# -------------------------
def save_plot(fig, filename: str):
    """Save figure to plots folder, create folder if not exists."""
    if not os.path.exists("plots"):
        os.makedirs("plots")
    path = os.path.join("plots", filename)
    fig.savefig(path)
    print(f"[INFO] Plot saved to {path}")

# -------------------------
# 1. Bar Chart
# -------------------------
def plot_bar(df: pd.DataFrame, x_col: str, y_col: str):
    """Create and save a basic bar chart."""
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x=x_col, y=y_col, data=df, ax=ax)
    ax.set_title(f"{y_col} by {x_col}")
    plt.tight_layout()
    save_plot(fig, f"{y_col}_by_{x_col}_bar.png")
    plt.show()

# -------------------------
# 2. Line Chart
# -------------------------
def plot_line(df: pd.DataFrame, x_col: str, y_col: str):
    """Create and save a line chart for trends."""
    fig, ax = plt.subplots(figsize=(8,5))
    sns.lineplot(x=x_col, y=y_col, data=df, marker="o", ax=ax)
    ax.set_title(f"{y_col} Trend over {x_col}")
    plt.tight_layout()
    save_plot(fig, f"{y_col}_over_{x_col}_line.png")
    plt.show()

# -------------------------
# 3. Histogram
# -------------------------
def plot_histogram(df: pd.DataFrame, col: str, bins: int = 10):
    """Create and save a histogram for numeric data."""
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df[col], bins=bins, kde=True, ax=ax)
    ax.set_title(f"{col} Distribution")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    save_plot(fig, f"{col}_histogram.png")
    plt.show()


