import csv
from pathlib import Path
from statistics import mean, stdev

ROOT = Path(__file__).resolve().parent
METRICS = {
    "completion_time_s": ("Tempo de conclusão", "s"),
    "pos_error_cm": ("Erro de posição (distância)", "cm"),
    "yaw_error_deg": ("Erro angular", "graus"),
    "touch_count": ("Quantidade de toques", "toques"),
    "wrong_selections": ("Seleções incorretas", "seleções"),
    "tracking_lost": ("Perdas de rastreamento", "ocorrências"),
}
LEARNING = {1, 12, 13}


def main():
    with (ROOT / "data/trials.csv").open(newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    valid = [row for i, row in enumerate(rows, 1) if i not in LEARNING]

    with (ROOT / "data/trials_analisados.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(valid)

    summary = []

    for technique in ("touch", "reticle"):
        group = [r for r in valid if r["technique"] == technique]
        for metric in METRICS:
            values = [float(r[metric]) for r in group]
            summary.append(
                dict(
                    technique=technique,
                    metric=metric,
                    n=len(values),
                    mean=mean(values),
                    std=stdev(values),
                )
            )

    with (ROOT / "data/resumo.csv").open("w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["technique", "metric", "n", "mean", "std"]
        )
        writer.writeheader()
        writer.writerows(summary)

    for row in summary:
        print(
            f"{row['technique']:7} {row['metric']:20} {row['mean']:.3f} ± {row['std']:.3f} (n={row['n']})"
        )

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    output = ROOT / "graficos"
    output.mkdir(exist_ok=True)
    for metric, (title, unit) in METRICS.items():
        stats = [r for r in summary if r["metric"] == metric]
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(
            ["Touch", "Reticle"],
            [r["mean"] for r in stats],
            yerr=[r["std"] for r in stats],
            capsize=6,
            color=["#387bb5", "#dc8740"],
        )
        ax.set(title=title, ylabel=f"Média ± desvio padrão amostral ({unit})")
        ax.set_ylim(bottom=0)
        fig.tight_layout()
        fig.savefig(output / f"{metric}.png", dpi=200)
        plt.close(fig)


if __name__ == "__main__":
    main()
