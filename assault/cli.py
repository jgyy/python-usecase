# python -m assault -r 100 -c 10 -j results.json -u https://google.com
# python -m assault -s "34.231.255.101:80" -s "34.231.255.101:9000" -f example.json
import click
import sys
import json
from typing import IO, Any

from assault.http import assault, ping_servers
from assault.stats import Results


@click.command()
@click.option("--requests", "-r", default=None, help="Number of requests")
@click.option("--concurrency", "-c", default=None, help="Number of concurrent requests")
@click.option("--json-file", "-j", default=None, help="Path to output JSON file")
@click.option("--filename", "-f", default=None, help="Name of the json file")
@click.option("--server", "-s", default=None, multiple=True, help="Name of the server")
@click.option("--url", "-u", default=None, help="Link to the website")
def cli(requests, concurrency, json_file, url, filename, server):
    # Create a set to prevent duplicate server/port combinations
    servers = set()

    # If --filename or -f option is used then attempt to read
    # the file and add all values to the `servers` set.
    # If --server or -s option are used then add those values
    # to the set.
    if server and filename:
        try:
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except:
            print("Error: Unable to open or read JSON file")
            sys.exit(1)

        for s in server:
            servers.add(s)

        # Make requests and collect results
        results = ping_servers(servers)
        print("Successful Connections")
        print("---------------------")
        for server in results['success']:
            print(server)

        print("\n Failed Connections")
        print("------------------")
        for server in results['failure']:
            print(server)

    if json_file:
        try:
            output_file = open(json_file, "w")
        except:
            print(f"Unable to open file {json_file}")
            sys.exit(1)
        total_time, request_dicts = assault(url, requests, concurrency)
        results = Results(total_time, request_dicts)
        display(results, output_file)


def display(results: Results, json_file: IO[Any]):
    if json_file:
        # Write to a file
        json.dump(
            obj={
                "successful_requests": results.successful_requests(),
                "slowest": results.slowest(),
                "fastest": results.fastest(),
                "total_time": results.total_time,
                "requests_per_minute": results.requests_per_minute(),
                "requests_per_second": results.requests_per_second(),
            },
            fp=json_file,
            indent=2
        )
        json_file.close()
        print(".... Done!")
    else:
        # Print to screen
        print(".... Done!")
        print("--- Results ---")
        print(f"Successful Requests\t{results.successful_requests()}")
        print(f"Slowest            \t{results.slowest()}s")
        print(f"Fastest            \t{results.fastest()}s")
        print(f"Total time         \t{results.total_time}s")
        print(f"Requests Per Minute\t{results.requests_per_minute()}")
        print(f"Requests Per Second\t{results.requests_per_second()}")

if __name__ == "__main__":
    cli()
