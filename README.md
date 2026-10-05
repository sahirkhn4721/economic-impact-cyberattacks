# Economic Impact of Cyberattacks on Businesses

## Question
How do reported data-breach costs change over time, and what do they imply for illustrative cybersecurity investment decisions?

## Data
Four published IBM/Ponemon annual global average data breach cost estimates (2021–2024), USD million They are published annual cross-sectional estimates, not longitudinal panels at the firm level or representative estimates of all cyberattacks. IBM Cost of a Data Breach Studies (2021-2024) Annual global average breach-cost estimates are based on data released by IBM and related releases.

## Reproduction
Python 3 standard library only: `python analysis.py`. Reproduces table growth rates, 2021–2024 change, and illustrative expected-loss scenarios. The probability inputs are **hypothetical**, not empirical estimates.

## Limitations
Small sample, report methodology/sampling changes, no causal inference, no estimated attack frequency or prevention efficacy. Results cannot establish return on security investments.

## Data Sources

The breach-cost data employed in this analysis are from IBM’s annual Cost of a Data Breach reports and other related IBM releases for 2021-2024.

- 2021: $4.24 million
- 2022: $4.35 million
- 2023: $4.45 million
- 2024: $4.88 million

The 5%, 10% and 20% breach probabilities used in the expected-loss analysis are hypothetical sensitivity scenarios, not empirical estimates of breach probability.

## Publication
This repository contains the data and reproducible analysis supporting the BFIN515 research paper, The Economic Impact of Cyberattacks on Businesses. The SSRN paper link will be added following publication.
