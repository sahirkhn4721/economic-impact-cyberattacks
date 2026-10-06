# Economic Impact of Cyberattacks on Businesses

## Question
How do reported data-breach costs change over time, and what do they imply for illustrative cybersecurity investment decisions?

## Data
Four published IBM/Ponemon annual global average data breach cost estimates (2021-2024), in USD millions. They are annual, cross-sectional estimates, not longitudinal firm level data or representative estimates of all cyberattacks . Data based on IBM Cost of a Data Breach reports and related IBM releases 2021-2024.

## Reproduction
Python 3 standard library only: `python analysis.py`. Reproduces table growth rates, 2021–2024 change, and illustrative expected-loss scenarios. The probability inputs are **hypothetical**, not empirical estimates.

## Limitations
Small sample, changes in report methodology/sampling, no causal inference, no estimated frequency of attack or efficacy of prevention. Results cannot validate return on security investments.

## Data Sources

The breach-cost data employed in this analysis are from IBM’s annual Cost of a Data Breach reports and other related IBM releases for 2021-2024.

- 2021: $4.24 million
- 2022: $4.35 million
- 2023: $4.45 million
- 2024: $4.88 million

The 5%, 10% and 20% breach probabilities used in the expected-loss analysis are hypothetical sensitivity scenarios, not empirical estimates of breach probability.

## Publication
This repository contains the data, reproducible analysis and final research paper for the BFIN515 project, The Economic Impact of Cyberattacks on Businesses: Data-Breach Costs and Cybersecurity Investment Decisions. The SSRN link will be added when the submission has been processed and is publicly available.
