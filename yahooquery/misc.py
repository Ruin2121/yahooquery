# stdlib
import os

# third party
import pandas as pd

from .utils import get_crumb, initialize_session, setup_session
from .utils.countries import COUNTRIES

BASE_URL = "https://query2.finance.yahoo.com"


def _make_request(
    url,
    response_field=None,
    country=None,
    method="get",
    params=None,
    data=None,
    **kwargs,
):
    if params is None:
        params = {}
    if country:
        country = country.lower()
        try:
            params.update(COUNTRIES[country])
        except KeyError as e:
            raise KeyError(
                f'{country} is not a valid option.  Valid options include {", ".join(sorted(COUNTRIES.keys()))}'
            ) from e
    setup_url = kwargs.pop("setup_url", os.getenv("YF_SETUP_URL", None))
    session = initialize_session(**kwargs)
    session = setup_session(session, setup_url)
    crumb = get_crumb(session)
    if crumb is not None:
        params["crumb"] = crumb
    r = getattr(session, method)(url, params=params, json=data)
    json = r.json()
    if response_field:
        try:
            return json[response_field]["result"]
        except (TypeError, KeyError):
            return json[response_field]
    return json


def search(
    query,
    country="United States",
    quotes_count=10,
    news_count=10,
    first_quote=False,
):
    """Search Yahoo Finance for anything

    Parameters
    ----------
    query: str
        What to search for
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    quotes_count: int, default 10, optional
        Maximum amount of quotes to return
    news_count: int, default 0, optional
        Maximum amount of news items to return
    """
    url = "https://query2.finance.yahoo.com/v1/finance/search"
    params = {"q": query, "quotes_count": quotes_count, "news_count": news_count}
    data = _make_request(url, country=country, params=params)
    if first_quote:
        return data["quotes"][0] if len(data["quotes"]) > 0 else data
    return data


def get_currencies():
    """Get a list of currencies"""
    url = f"{BASE_URL}/v1/finance/currencies"
    return _make_request(url, response_field="currencies", country="United States")


def get_exchanges():
    """Get a list of available exchanges and their suffixes"""
    url = "https://help.yahoo.com/kb/finance-for-web/SLN2310.html?impressions=true"
    dataframes = pd.read_html(url)
    return dataframes[0]


def get_market_summary(country="United States"):
    """Get a market summary

    Parameters
    ----------
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.

    Returns
    -------

    """
    url = f"{BASE_URL}/v6/finance/quote/marketSummary"
    return _make_request(url, response_field="marketSummaryResponse", country=country)


def get_trending(country="United States"):
    """Get trending stocks for a specific region

    Parameters
    ----------
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    """
    try:
        region = COUNTRIES[country.lower()]["region"]
    except KeyError as e:
        raise KeyError(
            f'{country} is not a valid option.  Valid options include {", ".join(COUNTRIES.keys())}'
        ) from e
    url = f"{BASE_URL}/v1/finance/trending/{region}"
    return _make_request(url, response_field="finance", country=country)[0]
