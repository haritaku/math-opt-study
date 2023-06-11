import numpy as np
import plotly.express as px
from pydantic import PositiveInt
from pydantic.dataclasses import dataclass


@dataclass
class Problem:
    B: PositiveInt  # 箱のサイズ
    n: PositiveInt  # アイテムの数

    def __post_init__(self):
        self.s = np.random.randint(1, self.B - 1, self.n, int)  # アイテムのサイズ


@dataclass
class ProblemTest:
    B = 8  # 箱のサイズ
    n = 4  # アイテムの個数
    s = np.array([1, 3, 6, 7], dtype=int)  # アイテムのサイズ


def create_problems(B, n, n_problems=100, seed=0):
    np.random.seed(seed)
    return [Problem(B, n) for _ in range(n_problems)]


def draw_allocation(result):
    title = (
        f"<b>Bin allocation</b>"
        f"<br>Status: {result['status']}, "
        f"number of bins: {result['objective']}, "
        f"solve time: {result['solve_time_sec']:.3} s"
    )

    y = result["allocation"].columns.tolist()
    y.remove("bin")

    fig = px.bar(result["allocation"], x="bin", y=y, title=title)
    fig.show()
