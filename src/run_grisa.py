"""
Running grisa from a function

Author: Tomas Fratrik
"""

from grisa import Grisa

def run_grisa(absolute_path):
    grisa = Grisa()
    grisa.options_add_argument('--headless')
    grisa.options_add_argument('--no-sandbox')
    grisa.options_add_argument('--disable-dev-shm-usage')
    grisa.options_add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

    grisa.set_driver_path("CHROMEDRIVER_PATH")
    grisa.set_binary_path("GOOGLE_CHROME_BIN")

    grisa.init_driver()
    grisa.run(absolute_path, accept_cookies=True, local_dev=False)

    page_source = grisa.get_page_source()
    similiar_img_json = grisa.scrape_similiar(page_source)
    try:
        grisa.go_to_source()
        page_source = grisa.get_page_source()
        source_img_json = grisa.scrape_source(page_source)
    except Exception as e:
        source_img_json = []
    grisa.driver_quit()

    return (similiar_img_json, source_img_json)