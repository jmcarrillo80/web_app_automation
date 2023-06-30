from playwright.sync_api import Playwright
from pathlib import Path
import time


export_names = ["Assets (Kiewit Power Bi Export)", "Planned Tasks (Kiewit Power Bi Export)", "Punchlist & C.O.W. (Kiewit Power Bi Export)", \
                "Systemization Custody Log (Kiewit Power Bi Export)", "Systemization Tree (Kiewit Power Bi Export)"]

def run_download(playwright: Playwright, download_path: Path, username: str, password: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://xom.ceccms.com/login.aspx")
    page.wait_for_load_state('networkidle')
    page.get_by_placeholder("User Name").click()    
    page.get_by_placeholder("User Name").fill(username)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state('networkidle')
    time.sleep(2)
    page.get_by_role("button", name="Done").click()
    page.wait_for_load_state('networkidle')
    page.get_by_role("link", name="Configuration").click()
    page.wait_for_load_state('networkidle')
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Exports").click()
    page1 = page1_info.value
    page1.locator("#colfiltvExports_PrimaryList_grideditExportName_filter").click()
    files_downloaded = []
    for name in export_names:
        page1.locator("#colfiltvExports_PrimaryList_grideditExportName_filter").fill(name)
        page1.keyboard.press("Enter")
        page1.wait_for_load_state('networkidle')
        time.sleep(2)
        with page1.expect_download() as download_info:
            page1.locator("div:nth-child(1) > div.slick-cell.l4.r4.cell-title > div > a").click()
        download = download_info.value
        print('\nurl: ', download.url)
        print('filename: ', download.suggested_filename)
        download_filepath = Path(download.path())
        new_download_filepath = download_path/download.suggested_filename
        new_download_filepath.unlink(missing_ok=True)
        download_filepath.rename(new_download_filepath)
        files_downloaded.append(new_download_filepath)        
    time.sleep(2)
    print('\nfiles downloaded ({0}): {1}'.format(len(files_downloaded), files_downloaded))
    context.close()
    browser.close()
    return files_downloaded


