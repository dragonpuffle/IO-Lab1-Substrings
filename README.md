# IO-Lab1-Substrings
Algorithms for searching a substring in a string

# **Отчет:**

Мы реализовали 3 разных алгоритма для поиска подстроки в тексте:

- Наивный алгоритм

- Алгоритм Кнута — Морриса — Пратта (КМП)

- Алгоритм Бойера — Мура — Хорспула (БМХ)

Алгоритм на каждом бенчмарке запускался 100 раз, чтобы оценить среднее время и количество операций для работы алгоритма. Видно, что все алгоритмы работают верно и возвращают одинаковый результат на одних и тех же бенчмарках. Ниже представлена таблица результатов, сгруппирована по бенчмаркам и алгоритмам.

# **Таблица:**
```
               Algorithm      Time  Operations  Result           Benchmark_text        Benchmark_pattern
8   Boyer-Moore-Horspool  0.000009        10.0       8   benchmarks/bad_t_1.txt   benchmarks/bad_w_1.txt
16    Knuth-Morris-Pratt  0.000006        20.0       8   benchmarks/bad_t_1.txt   benchmarks/bad_w_1.txt
0        Naive_algorithm  0.000003        18.0       8   benchmarks/bad_t_1.txt   benchmarks/bad_w_1.txt
9   Boyer-Moore-Horspool  0.000078       100.0      90   benchmarks/bad_t_2.txt   benchmarks/bad_w_2.txt
17    Knuth-Morris-Pratt  0.000057       216.0      90   benchmarks/bad_t_2.txt   benchmarks/bad_w_2.txt
1        Naive_algorithm  0.000021       910.0      90   benchmarks/bad_t_2.txt   benchmarks/bad_w_2.txt
10  Boyer-Moore-Horspool  0.000907      1000.0     900   benchmarks/bad_t_3.txt   benchmarks/bad_w_3.txt
18    Knuth-Morris-Pratt  0.000621      2196.0     900   benchmarks/bad_t_3.txt   benchmarks/bad_w_3.txt
2        Naive_algorithm  0.000250     90100.0     900   benchmarks/bad_t_3.txt   benchmarks/bad_w_3.txt
11  Boyer-Moore-Horspool  0.004341      5000.0    4000   benchmarks/bad_t_4.txt   benchmarks/bad_w_4.txt
19    Knuth-Morris-Pratt  0.003248     11996.0    4000   benchmarks/bad_t_4.txt   benchmarks/bad_w_4.txt
3        Naive_algorithm  0.001741   4001000.0    4000   benchmarks/bad_t_4.txt   benchmarks/bad_w_4.txt
12  Boyer-Moore-Horspool  0.000070        80.0     599  benchmarks/good_t_1.txt  benchmarks/good_w_1.txt
20    Knuth-Morris-Pratt  0.000326       666.0     599  benchmarks/good_t_1.txt  benchmarks/good_w_1.txt
4        Naive_algorithm  0.000172     10200.0     599  benchmarks/good_t_1.txt  benchmarks/good_w_1.txt
13  Boyer-Moore-Horspool  0.000069       107.0     610  benchmarks/good_t_2.txt  benchmarks/good_w_2.txt
21    Knuth-Morris-Pratt  0.000368       863.0     610  benchmarks/good_t_2.txt  benchmarks/good_w_2.txt
5        Naive_algorithm  0.000181     51935.0     610  benchmarks/good_t_2.txt  benchmarks/good_w_2.txt
14  Boyer-Moore-Horspool  0.000270       434.0    1629  benchmarks/good_t_3.txt  benchmarks/good_w_3.txt
22    Knuth-Morris-Pratt  0.001159      2847.0    1629  benchmarks/good_t_3.txt  benchmarks/good_w_3.txt
6        Naive_algorithm  0.000660    621030.0    1629  benchmarks/good_t_3.txt  benchmarks/good_w_3.txt
15  Boyer-Moore-Horspool  0.000520       510.0    9522  benchmarks/good_t_4.txt  benchmarks/good_w_4.txt
23    Knuth-Morris-Pratt  0.005066      9796.0    9522  benchmarks/good_t_4.txt  benchmarks/good_w_4.txt
7        Naive_algorithm  0.002912    876116.0    9522  benchmarks/good_t_4.txt  benchmarks/good_w_4.txt
```

# **Количество операций:**

Наивный алгоритм решает задачу простым перебором, алгоритм КМП сначала готовит префикс функцию шаблона (подстроки), а алгоритм БМХ предварительно обрабатывает шаблон для создания таблицы. Засчет предварительной подготовки алгоритмы требуют меньше операций, поэтому количество операций сравнения у наивного метода сильно больше (макс ~ 876000) в отличие от других. Остальные алгоритмы сохраняют малое количество операций, при этом алгоритм БМХ лучше справляется с этой задачей (макс 1000), чем алгоритм КМП (макс ~ 12000):

![operations_chart](https://github.com/user-attachments/assets/188478da-0902-4c4b-a9ad-4cf7e1fde58d)

# **Время работы:**

Другая ситуация с замером времени. На хороших данных алгоритм БМХ показывает себя лучше всех, однако сильно хуже работает на плохих данных. При этом на плохих данных наивный алгоритм работает быстрее остальных, так как не завязан на особых алгоритмах и занимается обычным перебором, в то время как другие алгоритмы подвержены качеству данных (благоприятные или нет), так как эти алгоритмы могут потратить много времени на предобработку данных, которая будет еще и плохо работать на конкретном примере. Алгоритм КМП менее подвержен замедлению скорости работы на плохих данных, при этом уступает в скорости работы алгоритму БМХ на хороших данных: 

![time_chart](https://github.com/user-attachments/assets/37f174f2-b9b6-40ed-9178-0fa6c1975f3c)

# **Вывод:**

Выбор алгоритма зависит от структуры данных и требований к производительности.

- Если шаблон может находиться в начале, или текст - сильно регулярный, то наивный метод может быть предпочтительным.
  
- Если мы работаем с реальным текстом, то БМХ будет самым быстрым.
  
- Если текст может быть как хорошим, так и плохим, то можно выбрать КМП.
  

# **Запуск:**

## 1. Клонировать репозиторий

```bash
git clone https://github.com/dragonpuffle/IO-Lab1-Substrings
cd IO-Lab1-Substrings
```

## 2. Установить зависимости 

```bash
pip install -r requirements.txt
```

## 3. Можно проверить программу на простых тестах

```python
python algorithms.py
```

## 4. Запустить с бенчмарками

Вывод таблицы в консоль, обновление таблицы `report.csv`, вывод графиков и сохранение их в файл.

```python
python main.py
```


