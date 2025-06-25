## TwitchSearcher Test Suite
This project automates the process of searching Twitch for a specific keyword (like StarCraft II), scrolling through the results, selecting a  live stream, and taking a screenshot after any ads finish playing.
##  Test Overview

You can watch the [brief demo](https://youtu.be/CChesURDqyE) first and then refer to the following parameter explanations

Func Name	|Parameter |Description
|---|---|---
gotoWeb | url|The browser will go to the input
search| string|Search for the input
scroll|int| Scoll the website for input times
gotoChannel|string| Opens the channel if found; otherwise logs a message
gotoRandomChannel|N/A| Opens random channel on the search page
screenshot|N/A| Take a screenshot for the page
quit|N/A| Close the browser

## How to Use
Clone the repository:

```
git clone https://github.com/teakia/webSearcher.git
cd webSearcher
```
Set up a virtual environment:

```
python3 -m venv venv
source venv/bin/activate 
```

Install dependencies:

```
pip install -r requirements.txt
```
Run the script:

```
python3 main.py -s a.txt
```
Or run the script with one or more outer files:

```
python3 main.py -s a.txt
python3 main.py -s a.txt b.txt
```

## Validation Approach
- The test suite uses **Selenium** to interact with Twitch's frontend. Validation is done primarily through:
    - Element presence: Using WebDriverWait with expected conditions to ensure elements are present before interacting.
    - Dynamic waits: For ads or loading delays, dynamic waits prevent brittle timeouts.


## Notes
- This script targets live search results only.
- No chromedriver needed, it's handled by scripts
- If Twitch layout changes (e.g., different class names), selectors may need to be updated.