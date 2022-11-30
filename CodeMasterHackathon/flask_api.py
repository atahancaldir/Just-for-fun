#!/usr/bin/env python
# encoding: utf-8

from re import sub
from flask import Flask, jsonify, request
from fetch_website import FetchWebsite
import time

fetcher = FetchWebsite()

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def create_url_analysis(url):
    url_analysis = dict()
    sub_fetcher = FetchWebsite()
    sub_fetcher.get_url_data(url)

    url_analysis["parsedUrl"] = url
    if sub_fetcher.response_code != 400 and sub_fetcher.response_code != 503:
        url_analysis["finalUrl"] = sub_fetcher.final_url
    url_analysis["secured"] = sub_fetcher.is_secured
    url_analysis["reachable"] = sub_fetcher.is_reachable
    if sub_fetcher.response_code != 404 and sub_fetcher.response_code != 408 and sub_fetcher.response_code != 503 and sub_fetcher.response_code != 400 and sub_fetcher.response_code != 310:
        url_analysis["redirectedURLs"] = sub_fetcher.redirected_urls
    if sub_fetcher.response_code != 400:
        url_analysis["totalAccessDuration"] = sub_fetcher.total_access_time
    if sub_fetcher.response_code != 404 and sub_fetcher.response_code != 408 and sub_fetcher.response_code != 310 and sub_fetcher.response_code != 503 and sub_fetcher.response_code != 400:
        url_analysis["contentLength"] = sub_fetcher.content_size
    url_analysis["responseCode"] = sub_fetcher.response_code
    url_analysis["responseMessage"] = sub_fetcher.response_message

    return url_analysis

@app.route('/')
def index():
    try:
        url = request.args.get('url')
        fetcher.get_hyperlinks(url)

        start_time = time.time()

        result = dict()
        result["url"] = url
        result["analysisDuration"] = None
        result["redirectedURLs"] = fetcher.redirected_urls
        result["responseCode"] = fetcher.response_code
        result["responseMessage"] = fetcher.response_message
        result["internalLinks"] = []
        result["externalLinks"] = []

        for internal_link in fetcher.internal_urls:
            result["internalLinks"].append(create_url_analysis(internal_link))

        for external_link in fetcher.external_urls:
            result["externalLinks"].append(create_url_analysis(external_link))

        result["analysisDuration"] = time.time() - start_time

        return jsonify(result)
    except:
        return "999"

app.run()