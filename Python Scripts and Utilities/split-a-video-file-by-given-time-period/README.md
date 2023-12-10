# Media File Splitter

This script splits a media file into two chunks based on the specified start and end times.

## Usage

1. Install FFmpeg: Make sure you have FFmpeg installed on your system.
2. Run the script using Python with the required command-line arguments:

```shell
python script.py inputfile starttime endtime outputfile1 outputfile2
```

- `inputfile`: The path to the input media file.
- `starttime`: The start time in seconds where the split should begin.
- `endtime`: The end time in seconds where the split should end.
- `outputfile1`: The path to the first output file.
- `outputfile2`: The path to the second output file.

## Prerequisites

- FFmpeg: Ensure that FFmpeg is installed and added to your system's PATH.

## Example

```shell
python script.py input.mp4 10 30 output1.mp4 output2.mp4
```

This example will split the `input.mp4` file from the 10th second to the 30th second and save the first chunk as `output1.mp4` and the second chunk as `output2.mp4`.

## License

This project is licensed under the [MIT License](LICENSE).