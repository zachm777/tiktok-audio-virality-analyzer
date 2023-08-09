def login_and_scroll_page(self, driver, seconds):
    end_time = time.time() + seconds
    while time.time() < end_time:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)


def start_driver(self, url, scroll_duration=5):
    driver_path = "/Users/zachmeyer/Development/chromedriver"
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    service = ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    self.login_and_scroll_page(driver, scroll_duration)
    page_source = driver.page_source
    driver.quit()
    return page_source


def extract_videos_from_search(self, html):
    soup = BeautifulSoup(html, "html.parser")
    tiktok_divs = soup.find_all('div', class_=self.EXTRACT_VIDEOS_FROM_SEARCH_CLASS)
    tiktok_links = []
    for div in tiktok_divs:
        link = div.find('a')['href']
        if link:
            tiktok_links.append(link)
    return tiktok_links


def extract_audio_from_video(self, video_link):
    try:
        response = requests.get(video_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        href = soup.find('a', class_=self.EXTRACT_AUDIO_FROM_VIDEO_CLASS)['href']
        audio_link = "https://www.tiktok.com" + str(href)
        return audio_link
    except Exception as e:
        print(f"Error extracting audio from video: {video_link}. Error message: {e}")
        return None