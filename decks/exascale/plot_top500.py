#!/usr/bin/env python3

from argparse import ArgumentParser
from datetime import date
import re

import matplotlib.pyplot as plt
import pandas as pd


def get_args():
    parser = ArgumentParser()
    parser.add_argument("input_filenames", metavar="FILENAME", nargs="+", help="TOP500 result XML files, with their original filenames")
    parser.add_argument("--output_filename", default=None, help="Where to put the plot. Default outputs to the screen.")
    parser.add_argument("--plot_styles", default=None, help="Matplotlib style file to use")
    return parser.parse_args()


def get_stats(filename):
    year, month = re.match(".*([21][9012][0-9][0-9])([01][16]).xls", filename).groups()
    df = pd.read_excel(filename)
    if "Unnamed: 0" in df.columns:
        df = pd.read_excel(filename, skiprows=1)
    if "Rpeak [TFlop/s]" in df:
        flops = df["Rpeak [TFlop/s]"] * 1e12
    elif "RPeak" in df:
        flops = df["RPeak"] * 1e9
    elif "Rpeak" in df:
        flops = df["Rpeak"] * 1e9
    else:
        print(df.columns)
        raise ValueError
    return {
        "date": date(int(year), int(month), 1),
        "sum": flops.sum(),
        "max": flops.max(),
        "min": flops.min()
    }


def get_data(input_filenames):
    return pd.DataFrame(get_stats(filename) for filename in input_filenames)


def plot_data(data, output_filename):
    fig, ax = plt.subplots(layout="constrained")
    for metric, marker in ("sum", "o"), ("max", "^"), ("min", "v"):
        ax.scatter(data["date"], data[metric], marker=marker, label=metric.title())

    ax.legend(loc="best")
    ax.set_xlabel("Date")
    ax.set_ylabel("FLOP/s")

    ax.set_yscale("log")
    ax.axhline(1e18, color="grey", dashes=(3, 3))

    if output_filename is None:
        plt.show()
    else:
        fig.savefig(output_filename)
        plt.close(fig)


def main():
    args = get_args()
    data = get_data(args.input_filenames)
    if args.plot_styles:
        plt.style.use(args.plot_styles)
    plot_data(data, args.output_filename)


if __name__ == "__main__":
    main()
