import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.dates as mdates
import math


colors = ["#295fb2", "#d12542", "#9e3172"]
custom_cmap = LinearSegmentedColormap.from_list("custom_gradient", colors, N=90)
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.dpi"] = 150


def plot_time_series(
    df: pd.DataFrame,
    data_cols: list = ["y"],
    time_col: str = "ds",
    id_col: str = "unique_id",
    ids: list | str = "all",
    grid: tuple | None = None,
    figsize: tuple | None = None,
    n_max: int | None = None,
    title: str | None = None,
    outliers_cols: list | None = None,
    confidence_interval: list | None = None,
) -> Figure:
    """Plot das séries temporais e das previsões.

    Args:
        df (pd.DataFrame): Dados com valores históricos e previsões.
        data_cols (list): Nomes das colunas a serem adicionadas ao mesmo plot.
        time_col (str): Coluna com valores de tempo. Padrão é 'ds'.
        id_col (str): Coluna de identificação de cada série. Padrão é 'unique_id'.
        ids (list | None, optional): Ids a serem plotados. Implica na quantidade de plots. Padrão é None.
        grid (tuple | None, optional): Matriz de plots tipo nxm. Padrão é n/2.
        figsize (tuple, optional): Tamanho do plot. Padrão é (12, 8).
        n_max (int, optional): Tamanho n da amostra. Plotará os últimos n valores da série temporal. Padrão é None.
        title (str, optional): Título do gráfico. Padrão é None.
        outliers_cols (list, optional): Colunas de outliers. Padrão é None.
        confidence_interval (list, optional): Lista de tuplas com nomes das colunas dos intervalos de confiança. Ex: [("y_lower", "y_upper")]
    """
    if ids == "all":
        ids = df[id_col].unique().tolist()

    n_plots = len(ids)

    if grid is None:
        rows = math.ceil(n_plots / 2)
        cols = 2
        grid = (rows, cols)

    if figsize is None:
        figsize = (12, grid[0] * 2)

    fig, axes = plt.subplots(grid[0], grid[1], figsize=figsize)
    axes = axes.flatten()  # type: ignore

    if title:
        fig.suptitle(title, y=0.95, fontsize=14)

    for i, id in enumerate(ids):
        df_id = df[df[id_col] == id].reset_index(drop=True)

        if n_max is not None:
            df_id = df_id.iloc[-n_max:]

        ax = axes[i]

        for i_col, col in enumerate(data_cols):
            cor = colors[i_col % len(colors)]
            ax.plot(df_id[time_col], df_id[col], color=cor, label=col)

            if confidence_interval is not None and i_col < len(confidence_interval):
                lower_col, upper_col = confidence_interval[i_col]
                if lower_col in df_id and upper_col in df_id:
                    ax.fill_between(
                        df_id[time_col],
                        df_id[lower_col],
                        df_id[upper_col],
                        color=cor,
                        alpha=0.2,
                        label=f"{col} CI",
                    )

        if i == 0:
            ax.legend(loc="upper left")

        if outliers_cols is not None:
            for outlier_col in outliers_cols:
                outliers = df_id[df_id[outlier_col] != 0]
                if not outliers.empty:
                    ax.scatter(outliers[time_col], outliers[data_cols[0]], color="red")

        ax.set_title(f"unique_id={id}", fontsize=12)

        if n_max is not None:
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=42))

    for j in range(i + 1, len(axes)):  # type: ignore
        axes[j].axis("off")

    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.95))
    plt.show()

    return fig
