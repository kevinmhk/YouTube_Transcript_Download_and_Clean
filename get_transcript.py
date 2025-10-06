from youtube_transcript_api import YouTubeTranscriptApi
import datetime
import os
import sys

language = None
language_provided = False

if len(sys.argv) > 1:
    video_id = sys.argv[1]
    if len(sys.argv) > 2:
        language = sys.argv[2]
        language_provided = True
else:
    video_id = input("Please enter the YouTube video ID: ")
    language_input = input("Please enter the transcript language (default: en): ").strip()
    if language_input:
        language = language_input
        language_provided = True
    else:
        language = "en"

try:
    if language_provided:
        transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=[language])
    else:
        transcript_list = YouTubeTranscriptApi().fetch(video_id)

    joiner = "\n\n" if language_provided and language.lower() != "en" else " "
    full_transcript = joiner.join(item.text for item in transcript_list)

    if language_provided and language.lower() != "en":
        processed_transcript = full_transcript
    else:
        processed_transcript = full_transcript.replace('. ', '.\n\n')

    # Generate filename
    now = datetime.datetime.now()
    datetime_str = now.strftime("%Y%m%d_%H%M%S")
    file_name = f"transcript_{datetime_str}.md"
    
    # Get full path
    file_path = os.path.abspath(file_name)

    # Write to markdown file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"# Transcript for video ID: {video_id}\n\n")
        f.write(f"URL: https://www.youtube.com/watch?v={video_id}\n\n")
        f.write(processed_transcript)

    # Output full path to console
    print(f"Transcript saved to: {file_path}")

except Exception as e:
    print(f"Could not retrieve transcript for video ID {video_id}.")
    print(f"Error: {e}")
