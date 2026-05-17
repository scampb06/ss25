import os
import pathlib
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
CHANNEL_NAME = "3-1-alerts"
DOWNLOAD_DIR = pathlib.Path("downloads_IA_pdfs")

if not SLACK_BOT_TOKEN:
    raise SystemExit("Set SLACK_BOT_TOKEN env var first")

client = WebClient(token=SLACK_BOT_TOKEN)
DOWNLOAD_DIR.mkdir(exist_ok=True)

def get_channel_id_by_name(name: str):
    cursor = None
    while True:
        try:
            resp = client.conversations_list(
                cursor=cursor,
                limit=1000,
                types="public_channel,private_channel",
            )
        except SlackApiError as e:
            raise SystemExit(f"Error calling conversations.list: {e}")

        for ch in resp["channels"]:
            if ch["name"] == name:
                return ch["id"]

        cursor = resp.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    return None

def list_channel_files(channel_id: str, types: str = "pdf"):
    all_files = []
    cursor = None

    while True:
        try:
            resp = client.files_list(
                channel=channel_id,
                types=types,
                cursor=cursor,
                count=200,
            )
        except SlackApiError as e:
            raise SystemExit(f"Error calling files.list: {e}")

        all_files.extend(resp.get("files", []))

        # files.list pagination can use either paging or response_metadata
        cursor = resp.get("paging", {}).get("next_cursor") or resp.get(
            "response_metadata", {}
        ).get("next_cursor")

        if not cursor:
            break

    return all_files

def is_ia_pdf(f):
    name = f.get("name", "")
    return name.startswith("IA") and name.endswith(".pdf")

def download_file(file_obj):
    url = file_obj.get("url_private") or file_obj.get("url_private_download")
    if not url:
        print(f"Skipping {file_obj.get('name')} (no url_private)")
        return

    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}

    filename = DOWNLOAD_DIR / file_obj["name"]
    print(f"Downloading: {file_obj['name']} -> {filename}")

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    with open(filename, "wb") as out:
        out.write(r.content)

def main():
    channel_id = get_channel_id_by_name(CHANNEL_NAME)
    if not channel_id:
        raise SystemExit(f"Channel '{CHANNEL_NAME}' not found")

    print(f"Channel '{CHANNEL_NAME}' has id: {channel_id}")

    all_pdfs = list_channel_files(channel_id, types="pdf")
    print(f"Total PDFs found in channel: {len(all_pdfs)}")

    ia_pdfs = [f for f in all_pdfs if is_ia_pdf(f)]
    print(f"IA*.pdf files to download: {len(ia_pdfs)}")

    for f in ia_pdfs:
        download_file(f)

    print("Done")

if __name__ == "__main__":
    main()