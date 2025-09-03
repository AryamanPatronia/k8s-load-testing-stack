import os
import time
import subprocess
import requests
from threading import Thread

class LoadGenerator:
    def __init__(self, target, frequency):
        self.target = target
        self.frequency = frequency
        self.response_times = []
        self.failures = 0
        self.total_requests = 0
        self.stop_flag = False

        # Testing the connection using CURL...

    def test_connection(self):
        """Using curl to check if connected..."""
        try:
            result = subprocess.run(['curl', '-s', self.target], capture_output=True, text=True)
            if result.returncode == 0:
                print("Curl connection successful! Response:")
                print(result.stdout)
            else:
                print("Curl connection failed :( || ")
                print(result.stderr)
        except Exception as e:
            print(f"There was an error performing the curl test: {e}")

            # Sending requests [Generating Load]...

    def send_request(self):
        try:
            print(f"Generating load on {self.target}...")
            response = requests.get(self.target, timeout=10)  # Setting the timeout limit...
            print(f"Successful in receiving a response!")
            self.total_requests += 1

            if response.status_code == 200:
                response_text = response.text.strip()
                if response_text.startswith("Time:"):
                    time_ms = int(response_text.split(":")[1].strip().replace("ms", ""))
                    time_sec = time_ms / 1000  # Convert milliseconds to seconds
                    self.response_times.append(time_sec)
                    print(f"Response Time: {time_sec:.3f} seconds")
                else:
                    print(f"Unexpected response format: {response_text}")
            else:
                print(f"Request failed :( Status code: {response.status_code}")
                self.failures += 1
        except requests.exceptions.RequestException as e:
            print("\033[91mRequest Timeout :( [10 Seconds Exceeded] This will count as a failure...\033[0m")
            self.failures += 1
            self.total_requests += 1


    def start(self):
        # We are running a curl test before starting...
        self.test_connection()

        def worker():
            while not self.stop_flag:
                self.send_request()
                time.sleep(1 / self.frequency)

        threads = []
        for _ in range(self.frequency):
            thread = Thread(target=worker)
            thread.start()
            threads.append(thread)

        try:
            # Keep the Load Generator running until keyboard interrupt...
            while not self.stop_flag:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received. Stopping load generator now...")
            self.stop_flag = True
        finally:
            for thread in threads:
                thread.join()
            self.report()

            # This function generates a report...

    def report(self):
        if self.response_times:
            avg_response_time = sum(self.response_times) / len(self.response_times)
        else:
            avg_response_time = 0

        print("\n--- Test Results ---")
        print(f"Total Requests Sent: {self.total_requests}") # Keeping track of requests that are being sent...

        # Two metrics (Average Response Time & Number of Failures)

        print(f"Average Response Time: {avg_response_time:.2f} seconds")
        print(f"Number of Failures: {self.failures}")

if __name__ == "__main__":

    # Setting up the two environment variables (Target & Frequency)

    target = os.getenv("TARGET", "http://192.168.0.100:30000/primecheck")
    frequency = int(os.getenv("FREQUENCY", "5")) # We change this to higher value for more load, therefore, more failures...

    print(f"Starting load generator for {target} at {frequency} requests/second...")
    load_generator = LoadGenerator(target, frequency)
    load_generator.start()
