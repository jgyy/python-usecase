import asyncio
import os
import requests
import time
from requests.exceptions import ConnectionError

# Make the actual HTTP request and gather results
def fetch(url):
    started_at = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "request_time": request_time}

# Function to continue to process work from queue
async def worker(name, queue, results):
    loop = asyncio.get_event_loop()
    while True:
        url = await queue.get()
        if os.getenv("DEBUG"):
            print(f"{name} - Fetching {url}")
        future_result = loop.run_in_executor(None, fetch, url)
        result = await future_result
        results.append(result)
        queue.task_done()

# Divide up work into batches and collect final results
async def distribute_work(url, requests, concurrency, results):
    queue = asyncio.Queue()

    # Add an item to the queue for each request we want to make
    for _ in range(int(requests)):
        queue.put_nowait(url)

    # Create workers to match the concurrency
    tasks = []
    for i in range(int(concurrency)):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - started_at

    for task in tasks:
        task.cancel()

    return total_time


# Entrypoint to making requests
def assault(url, requests, concurrency):
    results = []
    total_time = asyncio.run(distribute_work(url, requests, concurrency, results))
    return (total_time, results)


def get(server):
    debug = os.getenv("DEBUG")
    try:
        if debug:
            print(f"Making request to {server}")
        response = requests.get(f"http://{server}")
        if debug:
            print(f"Received response from {server}")
        return {"status_code": response.status_code, "server": server}
    except(ConnectionError):
        if debug:
            print(f"Failed to connect to {server}")
        return {"status_code": -1, "server": server}

async def ping(server, results):
    loop = asyncio.get_event_loop()
    future_result = loop.run_in_executor(None, get, server)
    result = await future_result
    if result["status_code"] in range(200, 299):
        results["success"].append(server)
    else:
        results["failure"].append(server)

async def make_requests(servers, results):
    tasks = []

    for server in servers:
        task = asyncio.create_task(ping(server, results))
        tasks.append(task)

    await asyncio.gather(*tasks)

def ping_servers(servers):
    results = {"success": [], "failure": []}
    asyncio.run(make_requests(servers, results))
    return results


if __name__ == "__main__":
    os.environ["DEBUG"] = "true"
    os.environ["PYTHONPATH"] = "."
    servers = ('web-node1:80', 'web-node2:80', 'web-node1:3000', 'web-node2:3000', 'web-node1:8080')
    ping_servers(servers)