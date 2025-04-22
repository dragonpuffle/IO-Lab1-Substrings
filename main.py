from time import time
from typing import Dict

import matplotlib.pyplot as plt
import pandas as pd

from algorithms import (read_file, naive_algorithm, Boyer_Moore_Horspool_algorithm, Knuth_Morris_Pratt_algorithm,
                        get_counter, make_none, make_bias_table, make_prefix)


def run_one_benchmark(alg_func: tuple, alg_name: str, bench_pattern: str, bench_text: str, results: list,
                      alternative: bool = False) -> None:

    print(f'Searching {bench_pattern} in {bench_text}...')
    substring = read_file(bench_pattern)
    text = read_file(bench_text)

    total_operations = 0
    pre_operations = 0
    total_duration = 0
    pre_duration = 0
    result = 0

    preprocess = None
    if alternative:
        start = time()
        preprocess = alg_func[1](substring)
        end = time()
        pre_duration = end - start
        pre_operations = get_counter()


    for _ in range(100):
        start = time()
        result = alg_func[0](substring, text, preprocess)
        end = time()
        duration = end - start
        operations = get_counter()
        total_operations += operations
        total_duration += duration

    results.append({'Algorithm': alg_name, 'Time': round(total_duration/100 + pre_duration, 6), 'Operations': total_operations/100 + pre_operations, 'Result': result,
                    'Benchmark_text': bench_text, 'Benchmark_pattern': bench_pattern})


def run_all_benchmarks(algs: Dict, bad_benchs: Dict, good_benchs: Dict, alternative: bool = False) -> None:
    start_total = time()
    results = []
    for alg_name, alg_func in algs.items():
        print(f'Using {alg_name}...')
        for bench_text, bench_pattern in bad_benchs.items():
            run_one_benchmark(alg_func, alg_name, bench_pattern, bench_text, results, alternative)
        for bench_text, bench_pattern in good_benchs.items():
            run_one_benchmark(alg_func, alg_name, bench_pattern, bench_text, results, alternative)
    end_total = time()
    print(f'Total time: {round(end_total - start_total, 6)} seconds')

    data = pd.DataFrame(results).sort_values(by=['Benchmark_text','Algorithm', 'Time'], axis=0)
    print(data)
    report_name = 'report_alt.csv' if alternative else 'report.csv'
    data.to_csv(report_name, index=False, encoding='utf-8')

    visualize(data, alternative)


def visualize(data: pd.DataFrame, alternative: bool = False) -> None:
    pivot_time = data.pivot(index='Benchmark_text', columns='Algorithm', values='Time')
    pivot_ops = data.pivot(index='Benchmark_text', columns='Algorithm', values='Operations')

    pivot_time.plot(kind='bar', figsize=(12, 6))
    plt.title('Mean time for each algorithm by benchmark')
    plt.xlabel('Benchmark')
    plt.ylabel('Time, sec')
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Algorithm')
    chart_name1 = 'time_chart_alt.png' if alternative else 'time_chart.png'
    plt.savefig(chart_name1)
    plt.show()

    pivot_ops.plot(kind='bar', figsize=(12, 6))
    plt.title('Mean operations for each algorithm by benchmark')
    plt.xlabel('Benchmark')
    plt.ylabel('Operations')
    plt.tight_layout()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Algorithm')
    chart_name2 = 'operations_chart_alt.png' if alternative else 'operations_chart.png'
    plt.savefig(chart_name2)
    plt.show()


if __name__ == '__main__':
    algs = {
        'Naive_algorithm': (naive_algorithm, make_none),
        'Boyer-Moore-Horspool': (Boyer_Moore_Horspool_algorithm, make_bias_table),
        'Knuth-Morris-Pratt': (Knuth_Morris_Pratt_algorithm, make_prefix)
    }

    bad_benchs = {f'benchmarks/bad_t_{i}.txt': f'benchmarks/bad_w_{i}.txt' for i in range(1, 5)}
    good_benchs = {f'benchmarks/good_t_{i}.txt': f'benchmarks/good_w_{i}.txt' for i in range(1, 5)}

    # Dev note: results showed no difference
    alternative = False

    run_all_benchmarks(algs, bad_benchs, good_benchs, alternative)
