# Mode statistics practice

Practice code for the article **The Mode, The Most Underrated And Most Misused Average**.
Every script is short, runs on its own, and prints the numbers used in the article.

The listening data is made up. `listening.py` rebuilds the same month of 900 plays every
time (a bus ride around 08:00, bedtime around 22:30, a few plays in between), so your output
matches the article line for line. Script 16 runs on your own Spotify history.

## Setup

```bash
pip install -r requirements.txt
```

Then run any script, for example `python 09_kde_hilltops.py`.

## The scripts

| Script | What it shows |
|---|---|
| `listening.py` | the made-up month of plays, plus an hours to hh:mm helper |
| `01_mean_lands_nowhere.py` | the mean play time lands in the silent afternoon |
| `02_more_legs_than_average.py` | 98 of 100 people have more legs than average |
| `03_count_the_plays.py` | the mode by counting, with `Counter` |
| `04_genres_column.py` | the mode of genres in pandas, and why the mean fails |
| `05_four_answers_to_a_tie.py` | four Python tools, four answers to one tie |
| `06_grouped_mode.py` | the grouped mode formula on hourly bars |
| `07_bin_edges_move_the_mode.py` | moving the bars 30 minutes changes the busiest bar |
| `08_exact_times.py` | exact times never repeat, so counting fails |
| `09_kde_hilltops.py` | kernel density estimation and hilltop finding |
| `10_hill_width.py` | how the hill width (bandwidth) changes the hill count |
| `11_two_sigma_rule.py` | two equal groups only make two hills past 2 sd apart |
| `12_heights.py` | women's and men's heights mixed still make one hill |
| `13_rule_of_three.py` | Pearson's mode guess, 3 x median - 2 x mean |
| `14_top_song_per_month.py` | the mode per group in pandas, keeping ties |
| `15_hidden_listener.py` | a Gaussian mixture finds a hidden listener, BIC picks how many groups |
| `16_your_spotify_data.py` | your own mode song, mean time and hilltops from a Spotify export |

## Use your own Spotify data

1. In your Spotify account's privacy settings, request a copy of your data.
2. When the email arrives, unzip it and find the streaming history files
   (for example `StreamingHistory0.json`, or `Streaming_History_Audio_*.json` in the extended history).
3. Run `python 16_your_spotify_data.py path/to/StreamingHistory0.json`.

Without a file it runs on `sample_streaming_history.json`, a small fake export. Spotify's times are
in UTC, so your hilltops may be shifted by your time zone.

## Exercises

**1.** Your last plays are `["A", "B", "B", "C", "A", "B", "A"]`. What does `statistics.mode` return, and what does `statistics.multimode` return?

<details><summary>Answer</summary>

`A` and `B` both appear three times. `statistics.mode` returns `A`, the first winner it met. `statistics.multimode` returns `['A', 'B']`.
</details>

**2.** Bars of width 10 start at 20 and hold `[10, 25, 40, 30, 5]`. Use `grouped_mode` from `06_grouped_mode.py` to estimate the mode.

<details><summary>Answer</summary>

The busiest bar is 40 to 50. f1 = 40, f0 = 25, f2 = 30, so the mode is 40 + 15 / (15 + 10) x 10 = **46**.
</details>

**3.** In `07_bin_edges_move_the_mode.py`, start the bars at 5.75 instead. Which bar is busiest now?

<details><summary>Answer</summary>

07:45 to 08:45, with 246 plays. A quarter of an hour of sliding is already enough to hand the win to the bus ride.
</details>

**4.** In `10_hill_width.py`, add widths of 12 and 90 minutes. How many hilltops does each give?

<details><summary>Answer</summary>

12 minutes gives 7 hilltops and 90 minutes gives 2. Somewhere between one and one and a half hours the small bump between the two habits melts away.
</details>

**5.** In `11_two_sigma_rule.py`, try gaps from 1.9 to 2.2 in steps of 0.05. Where does the second hill appear?

<details><summary>Answer</summary>

At 2.05. At exactly 2.0 the top is perfectly flat, still one hill. Anything past 2 standard deviations gives two.
</details>

**6.** In `13_rule_of_three.py`, change the gamma shape from 2.5 to 1.2. The true mode is now (1.2 - 1) x 6 = 1.2. How good is Pearson's guess?

<details><summary>Answer</summary>

It prints about 1.47. In the right area, but about 20% off, because the shape is far more lopsided. The rule is best on gently skewed data.
</details>

**7.** In `15_hidden_listener.py`, move the cousin's hill from 16.6 to 21.0, close to bedtime. Does the score still find three groups?

<details><summary>Answer</summary>

The scores come out as 7117, 5017, 4393 and 4367 for one to four groups. Three still beats two easily, but now four edges out three by a little, because the hidden hill overlaps your bedtime hill and the model starts splitting it oddly. The closer a hidden group sits to one of your own habits, the harder it is to pull apart, exactly like the height example in the article.
</details>

**8.** Run `16_your_spotify_data.py` on your own export. Do you see more than one hilltop, and can you name the habit behind each one?

<details><summary>Answer</summary>

No fixed answer. If a hill surprises you, filter the songs played in that window. That is usually where the story is.
</details>

## License

MIT
