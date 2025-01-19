# Notify Application

The application notifies important occations, events to intended group of recipients on the very date through email messages. It works in following way:

-   Read a Google spreadsheet to get the list of specified event and event dates.
-   if current date matches with the any of the event dates, it triggers the email notification.
-   The group of email recipients and email subject and message body are fetched from the Google spreadsheet.
-   It sends the same email to multiple recipients.

## Environment variables

1. **APP_PASS_CODE** - The passcode for the sender email address.
2. **GOOGLE_SHEET_URL** - The Google Sheet URL for sheety API.

## External Python Packages used

-   **markdown**
-   **pandas**
-   **dotenv**

To install all dependencies use following command.

`pip install -r requirements.txt`
