# Notify Application

The application notifies important occasions, events to intended group of recipients on the very date through email messages. It works in following way:

-   Sends Good Morning email with a funny quote and image everyday.
-   Sends your daily dose of Technology related News.
-   Read a Google spreadsheet to get the list of specified event and event dates.
-   if current date matches with the any of the event dates, it triggers the email notification.
-   The group of email recipients and email subject and message body are fetched from the Google spreadsheet.
-   It sends the same email to multiple recipients.

## Environment variables

1. **APP_PASS_CODE** - The passcode for the sender email address.
2. **GOOGLE_SHEET_URL** - The Google Sheet URL for sheety API.
3. **QUOTE_API_URL** - The URL for the Quote API (https://api.kanye.rest/)
4. **IMG_URL** - The URL for the Image API (picsum photos)
5. **NEWS_API_URL** - The URL for the News API (https://newsapi.org/v2/everything)
6. **NEWS_API_KEY** - The API key for the News API.
7. **NEWS_TOPIC** - The news topic or category.
8. **ABS_PATH** - The Absulute path of the email template folder.

## External Python Packages used

-   **markdown**
-   **pandas**
-   **python-dotenv**

To install all dependencies use following command.

`pip install -r requirements.txt`
