WebSearcher Automation

WebSearcher is a Python automation tool that uses Selenium to interact with streaming platform, especially with Twitch.tv. It allows you to programmatically:


Please execute the command below before testing.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Features

Automated browser control with Selenium

Command-driven interface through plain text instruction files

Dynamic scrolling to load Twitch search results

Filtering channels by URL blacklist patterns

Random or specific selection of live channels to visit

Detection and waiting for ads to finish before screenshot

Robust error handling and logging

Support for multiple instruction files sequentially

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/twitchsearcher.git
cd twitchsearcher
Create a Python virtual environment and activate it:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Download ChromeDriver that matches your Chrome browser version, and place it under ./chromedriver-linux64/chromedriver or adjust the path in the code.

Usage
Prepare a command script file, for example a.txt:

bash
Copy
Edit
gotoWeb https://www.twitch.tv
search Just Chatting
scroll
gotoRandomChannel /directory/ /videos/ /collections/ /clip/ /schedule
screenshot
quit
Run the automation by specifying the script file(s):

bash
Copy
Edit
python main.py -s a.txt
You can specify multiple script files to run sequentially:

bash
Copy
Edit
python main.py -s a.txt b.txt
Command Reference
gotoWeb <url>: Opens the given URL in browser. Protocol http:// or https:// is required or automatically added.

search <keyword>: Searches Twitch for the specified keyword.

scroll: Scrolls the page down multiple times to load more results.

gotoRandomChannel <blacklist_patterns>: Randomly selects a live channel whose URL does not contain any of the blacklist patterns.

screenshot: Takes a screenshot of the current browser window.

quit: Closes the browser and ends the session.

Troubleshooting
Ensure ChromeDriver version matches your installed Chrome browser.

Make sure URLs include protocol (http or https).

Check that your instruction file formatting is correct and commands are supported.

If errors about missing elements occur, Twitch's page structure might have changed; update the selectors accordingly.

License
MIT License

Author
Your Name - your.email@example.com

If you want, I can also help you draft a more detailed developer guide or examples for extending TwitchSearcher.py. Just ask!