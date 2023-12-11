# Internet Speed Test

This Python script uses the `speedtest-cli` library to test your internet speed. It tests and logs the download speed, upload speed, and ping.

## Installation

Before running this script, you need to install the `speedtest-cli` library. You can install it using pip:

```bash
pip install speedtest-cli
```

## Usage

To run the script, use the following command:

```bash
python speedtest.py
```

The script will print the results of the speed test to the console:

```
Starting speed test at 2023-06-22 12:00:00
Download Speed: 100.00 Mbps
Upload Speed: 50.00 Mbps
Ping: 10 ms
Speed test completed
```

The results are also logged to a file named `internet_speed.log`. If an error occurs during the speed test, the error message and stack trace will also be logged.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
