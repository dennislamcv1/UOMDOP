# Module 4

## Dependencies

This module's Python package dependencies include:

* Altair
* Pandas
* NumPy

## Data files

The base CSV file is `./mega_millions-20240518.csv`

The base CSV file is read by `./data/mega_millions_data_separator.ipynb` which produces the following four CSV files:

1. `./data/mega_millions-2002_08.csv`
2. `./data/mega_millions-2009_15.csv`
3. `./data/mega_millions-2016_22.csv`
4. `./data/mega_millions-2023_24.csv`

## Notebook data input/output

| File | Reads | Writes |
| :--- | :---- | :----- |
| `01-pandas-concat.ipynb` | `./data/mega_millions-2002_08.csv`, `./data/mega_millions-2009_15.csv`, `./data/mega_millions-2016_22.csv`, `./data/mega_millions-2023_24.csv` | `./data/mega_millions_combined-2002-24.csv` |
| `02-pandas-merge_join.ipynb` | `./data/mega_millions_combined-2002-24.csv` | `./data/mega_millions_pick5_cols-2002_24.csv` |
| `03-pandas-reshape_drop.ipynb` | `./data/mega_millions_pick5_cols-2002-24.csv` | `./data/mega_millions_pick5_cols-2017_24.csv` |
| `04-pandas-aggregate.ipynb` | `./data/mega_millions_pick5_cols-2017-24.csv` | `./data/mega_millions-aggregate-2017_24.csv` |
| `05-pandas-filter.ipynb` | `./data/mega_millions-aggregate-2017-24.csv` | `./data/mega_millions-filter-sigma_one-2017_24.csv` |
| `06-pandas-transform.ipynb` | `./data/mega_millions-aggregate-2017-24.csv` | `./data/mega_millions-transform-2017_24.csv` |
| `07-pandas-apply.ipynb` | `./data/mega_millions-transform-2017-24.csv` | `./data/mega_millions-apply-2017_24.csv` |
