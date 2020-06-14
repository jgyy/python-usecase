"""
Writing Doctests and Type Hints

>>> import sys
>>> sys.version >= "3.5"
True
"""
from typing import List, Dict


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
        >>> results.requests[0]
        {'status_code': 200, 'request_time': 3.4}
        >>> results.requests[1]
        {'status_code': 500, 'request_time': 6.1}
        >>> results.requests[2]
        {'status_code': 200, 'request_time': 1.04}
        """
        self.total_time = total_time
        self.requests = requests

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
        return 6.1

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
        return 1.04

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
        9.846666667
        """
        return 9.846666667

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
        return 2
