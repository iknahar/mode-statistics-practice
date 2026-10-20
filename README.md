# Mode statistics practice

Practice code for the article **The Mode, The Most Underrated And Most Misused Average**.
Every script is short, runs on its own, and prints the exact numbers used in the article.

The gym data is made up. `gym.py` builds the same fake week of 1,000 check-ins every
time (a before-work crowd, an after-work crowd and a few drop-ins), so your output
matches the article line for line.

## Setup

```bash
pip install -r requirements.txt
```

Then run any script, for example `python 09_kde_hilltops.py`.

## The scripts

| Script | What it shows |
|---|---|
| `gym.py` | the made-up check-in week, plus an hours to hh:mm helper |
| `01_mean_lands_nowhere.py` | the mean check-in time lands in the quiet hours |
| `02_count_the_piles.py` | the mode by counting, with `Counter` |
| `03_words_column.py` | the mode of class names in pandas, and why the mean fails |
| `04_four_answers_to_a_tie.py` | four Python functions, four answers to one tie |
| `05_old_scipy_code.py` | the `IndexError` old SciPy code hits, and the fix |
| `06_grouped_mode.py` | the grouped mode formula on hourly bars |
| `07_bin_edges_move_the_mode.py` | moving the bars 30 minutes changes the busiest bar |
| `08_exact_times.py` | exact times never repeat, so counting fails |
| `09_kde_hilltops.py` | kernel density estimation and hilltop finding |
| `10_hill_width.py` | how the hill width (bandwidth) changes the hill count |
| `11_two_sigma_rule.py` | two equal groups only make two hills past 2 sd apart |
| `12_heights.py` | women's and men's heights mixed still make one hill |
| `13_rule_of_three.py` | Pearson's mode guess, 3 x median - 2 x mean |
| `14_mode_per_group.py` | the mode per group in pandas, keeping ties |
| `15_hidden_crowd.py` | a Gaussian mixture finds the hidden crowds, BIC picks how many |

## Exercises

**1.** Shoe sizes sold this morning are `[38, 39, 39, 40, 41, 39, 40, 40]`. What is the mode? What does `scipy.stats.mode` say?

<details><summary>Answer</summary>

There are two modes, 39 and 40, three sales each. `statistics.multimode` returns `[39, 40]`. `scipy.stats.mode` returns a single value, `39`.
</details>

**2.** Bars of width 10 start at 20 and hold `[10, 25, 40, 30, 5]`. Use `grouped_mode` from `06_grouped_mode.py` to estimate the mode.

<details><summary>Answer</summary>

The busiest bar is 40 to 50. f1 = 40, f0 = 25, f2 = 30, so the mode is 40 + 15 / (15 + 10) x 10 = **46**.
</details>

**3.** In `07_bin_edges_move_the_mode.py`, start the bars at 4.75 instead. Which bar is busiest now?

<details><summary>Answer</summary>

06:45 to 07:45, with 220 check-ins. Quarter of an hour of sliding is already enough to hand the win to the morning crowd.
</details>

**4.** In `10_hill_width.py`, add widths of 12 and 36 minutes. How many hilltops does each give?

<details><summary>Answer</summary>

12 minutes gives 6 hilltops and 36 minutes gives 3. Only from about 48 minutes do you settle on the two real rush hours.
</details>

**5.** In `11_two_sigma_rule.py`, try gaps from 1.9 to 2.2 in steps of 0.05. Where does the second hill appear?

<details><summary>Answer</summary>

At 2.05. At exactly 2.0 the top is perfectly flat, still one hill. Anything past 2 standard deviations gives two.
</details>

**6.** In `13_rule_of_three.py`, change the gamma shape from 2.5 to 1.2. The true mode is now (1.2 - 1) x 3 = 0.6. How good is Pearson's guess?

<details><summary>Answer</summary>

It prints about 0.73. Still in the right area, but off by about 20%, because the shape is far more lopsided. The rule is best on gently skewed data.
</details>

**7.** In `15_hidden_crowd.py`, move the class crowd's centre from 33 to 55 minutes. Does BIC still pick two crowds?

<details><summary>Answer</summary>

Yes, BIC is 4966, 4920 and 4936 for one, two and three crowds, so two still wins. But the margin over one crowd shrinks from 358 to 46. Closer crowds are harder to tell apart, just like the height example.
</details>

**8.** Take any column from your own life (sleep times, screen time, bus waits). Plot it at three hill widths. Do you see more than one hill, and can you name the column that splits them?

<details><summary>Answer</summary>

No fixed answer. If you find two hills, try colouring by weekday versus weekend. That splits a surprising number of everyday columns.
</details>

## License

MIT
