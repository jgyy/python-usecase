"""
Writing Doctests and Type Hints

>>> import sys
>>> sys.version >= "3.5"
True
"""
from typing import List, Dict
from statistics import mean


class Results:
    """
    Results handles calculating statistics based on a list of requests that were made.
    Here's an example of what the information will look like:

    Successful requests     3000
    Slowest                 0.010s
    Fastest                 0.001s
    Average                 0.003s
    Total time              2.400s
    Requests Per Minute     90000
    Requests Per Second     125

    >>> results = Results(10.6, [{
    ...     'status_code': 200,
    ...     'request_time': 3.4
    ... }, {
    ...     'status_code': 500,
    ...     'request_time': 6.1
    ... }, {
    ...     'status_code': 200,
    ...     'request_time': 1.04
    ... }])
    >>> "__init__" in dir(results)
    True
    >>> "total_time" in dir(results)
    True
    >>> "requests" in dir(results)
    True
    >>> "slowest" in dir(results)
    True
    """

    def __init__(self, total_time: float, requests: List[Dict]):
        """
        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.total_time
        10.6
        >>> results.requests[1]
        {'status_code': 200, 'request_time': 3.4}
        >>> results.requests[2]
        {'status_code': 500, 'request_time': 6.1}
        >>> results.requests[0]
        {'status_code': 200, 'request_time': 1.04}
        """
        self.total_time = total_time
        self.requests = sorted(requests, key=lambda r: r["request_time"])

    def slowest(self) -> float:
        """
        Returns the slowest request's completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.slowest()
        6.1
        """
        return self.requests[-1]["request_time"]

    def fastest(self) -> float:
        """
        Returns the slowest request's completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.fastest()
        1.04
        """
        return self.requests[0]["request_time"]

    def average_time(self) -> float:
        """
        Returns the slowest request's completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.average_time()
        3.513333333333333
        """
        return mean([r["request_time"] for r in self.requests])

    def successful_requests(self) -> int:
        """
        Returns the slowest request's completion time

        >>> results = Results(10.6, [{
        ...     'status_code': 200,
        ...     'request_time': 3.4
        ... }, {
        ...     'status_code': 500,
        ...     'request_time': 6.1
        ... }, {
        ...     'status_code': 200,
        ...     'request_time': 1.04
        ... }])
        >>> results.successful_requests()
        2
        """
        return len([r for r in self.requests if r["status_code"] in range(200, 299)])
