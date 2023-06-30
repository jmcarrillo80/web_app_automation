from modules.Credentials import getSmartCompletionsCredentials, getSharepointCredentials
from playwright.sync_api import sync_playwright
from modules.SmartCompletions import run_download
from modules.Sharepoint import UploadFiles
from pathlib import Path
import os


DOWNLOAD_BASE_PATH = Path(r'C:\Users\s3d-batch.svc\Downloads')
SITE_URL = 'https://portal.kiewit.com/teams/bw20036202/constopr'
TARGET_URL = 'CompletionsTurnover/3 - Smart Completions Exports'

def main():
    download_path = DOWNLOAD_BASE_PATH/'SmartCompletions'
    username, password = getSmartCompletionsCredentials()
    if not download_path.is_dir():
        os.makedirs(download_path)
    for child in download_path.iterdir():
        if child.is_file():
            child.unlink(missing_ok=True)
    with sync_playwright() as playwright:
        files_downloaded = run_download(playwright=playwright, download_path=download_path, username=username, password=password)
    
    account, password = getSharepointCredentials()
    sharepointObj = UploadFiles(site_url=SITE_URL, account=account, password=password, target_url=TARGET_URL)
    ctx = sharepointObj.get_sharepoint_connection()
    web = ctx.web.get().execute_query()
    # will print web url if connection is successful
    print(web.url)
    for local_path in files_downloaded:
        sharepointObj.upload_large_file_to_sharepoint(ctx=ctx, local_path=local_path)



if __name__== "__main__":
    main()