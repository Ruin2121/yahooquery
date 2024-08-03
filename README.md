<!-- markdownlint-disable -->
<p align="center">
    <a href="#"><img src="docs/docs/img/full.png"></a>
</p>
<p align="center">
    <em>Python wrapper for an unofficial Yahoo Finance API</em>
    <br>
    <em>Forked by Ruin2121</em>
</p>
<p align="center">
    <a href="https://codecov.io/gh/Ruin2121/yahooquery">
        <img src="https://codecov.io/gh/Ruin2121/yahooquery/graph/badge.svg?token=BWHE5GCW8T"/>
    </a>
    <a href="https://sourcery.ai">
        <img src="https://img.shields.io/badge/Sourcery-enabled-brightgreen">
    </a>
    <a href="https://github.com/astral-sh/ruff">
        <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;">
    </a>
</p>
<!-- markdownlint-restore -->

## Overview

Yahooquery is a python interface to unofficial Yahoo Finance API endpoints. The package allows a user to retrieve nearly all the data visible via the Yahoo Finance front-end.

Some features of yahooquery:

- **Fast**: Data is retrieved through API endpoints instead of web scraping. Additionally, asynchronous requests can be utilized with simple configuration
- **Simple**: Data for multiple symbols can be retrieved with simple one-liners
- **User-friendly**: Pandas Dataframes are utilized where appropriate
- **Premium**: Yahoo Finance premium subscribers are able to retrieve data available through their subscription

## Requirements

Python 3.9+

- [Pandas](https://pandas.pydata.org) - Fast, powerful, flexible and easy to use open source data analysis and manipulation tool
- [Requests](https://requests.readthedocs.io/en/master/) - The elegant and simple HTTP library for Python, built for human beings.
- [Requests-Futures](https://github.com/ross/requests-futures) - Asynchronous Python HTTP Requests for Humans

### Yahoo Finance Premium Subscribers

- [Selenium](https://www.selenium.dev/selenium/docs/api/py/) - Web browser automation

  Selenium is only utilized to login to Yahoo, which is done when the user passes certain keyword arguments. Logging into Yahoo enables users who are subscribers to Yahoo Finance Premium to retrieve data only accessible to premium subscribers.

## Installation

For standard installation:

```bash
pip install "yahooquery @ git+https://github.com/Ruin2121/yahooquery.git@2.3.7r9"
```

If you're a Yahoo Finance premium subscriber and would like to retrieve data available through your subscription, do the following:

```bash
pip install "yahooquery[premium] @ git+https://github.com/Ruin2121/yahooquery.git@2.3.7r9"
```

## Example

The majority of the data available through the unofficial Yahoo Finance API is related to a company, which is represented in yahooquery as a `Ticker`. You can instantiate the `Ticker` class by passing the company's ticker symbol. For instance, to get data for Apple, Inc., pass `aapl` as the first argument to the `Ticker` class:

```python
from yahooquery import Ticker

aapl = Ticker('aapl')

aapl.summary_detail
```

## Multiple Symbol Example

The `Ticker` class also makes it easy to retrieve data for a list of symbols with the same API. Simply pass a list of symbols as the argument to the `Ticker` class.

```python
from yahooquery import Ticker

symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']

faang = Ticker(symbols)

faang.summary_detail
```

## License

This project is licensed under the terms of the MIT license.
