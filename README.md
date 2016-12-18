```
|--------------------------------------------|-----------|-
| Script                                     |  Time     |
|--------------------------------------------|-----------|-
| get_title_with_urllib.py                   |  3.0017   |
| get_title_with_requests.py                 |  2.2646   |
|                                                        |
| get_title_with_aiohttp_in_diff_sessions.py |  0.8001   |
| get_title_with_aiohttp_in_one_session.py   |  0.8056   |
|--------------------------------------------|-----------|-
```

Notes:
======
Task was to fetch titles from random [4] urls (from the top of a head).

Time is best of 3, truncated first 4 digits after dot.

urllib here is used w/o session (it doesn't have one), requests - with.

Generally it is wrong to use aiohttp with separate sessions for each fetch.

Python 3.5



TODO?

Also would be nice to run blocking parts of aiohttp script with run_in_executor, try it out.
