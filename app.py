# This is Notify main application.

from data_manager import DataManager
from data_formatter import DataFormatter
from email_notification import EmailNotify
from quote_news import generate_quote, generate_news_HTML
from daily_mail import DailyEmail

# Default To email list.
TO_EMAIL = ['debaditya.bhar@gmail.com', 'debadityabhar@icloud.com']

def main():
    
    # Sends Daily quotes email.
    daily = DailyEmail(generate_quote(), generate_news_HTML())
    today_email = daily.get_email()
    today_send_mail = EmailNotify(to_emails=TO_EMAIL, subject=today_email[0],
                                  content=today_email[1], is_html=True)
    today_send_mail.send_email()

    # Notify If there is any event for that day.
    data = DataManager()
    events = data.get_match_event()

    if events != None:
        for event in events:
            fmt = DataFormatter(text=event['content'], emails=event['emails'])
            notify_mail = EmailNotify(to_emails=fmt.get_email_list(), subject=event['subject'],
                                      content=fmt.convert_markdown_to_html(), is_html=True)
            notify_mail.send_email()
    else:
        print('No events found today!')
        

if __name__ == '__main__':
    main()