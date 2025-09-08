# YouTube_Transcript_Download_and_Clean

A Python script to download and clean the transcript of a YouTube video.

## Features

- Downloads the transcript for a given YouTube video ID.
- Cleans the transcript by inserting a newline after each sentence.
- Saves the cleaned transcript as a markdown file.
- The output filename is timestamped to avoid overwriting previous transcripts.

## Prerequisites

- Python 3
- `youtube_transcript_api` library

You can install the required library using pip:
```bash
pip install youtube-transcript-api
```

## Usage

You can run the script from the command line and pass the YouTube video ID as an argument:

```bash
python get_transcript.py <video_id>
```

For example:
```bash
python get_transcript.py OlQIc-oV4uU
```

If you run the script without providing a video ID, it will prompt you to enter one:

```bash
python get_transcript.py
Please enter the YouTube video ID: OlQIc-oV4uU
```

The script will create a markdown file in the same directory with a name like `transcript_YYYYMMDD_HHMMSS.md`.