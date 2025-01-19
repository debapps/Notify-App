# This is Notify main application.

from data_manager import DataManager
from data_formatter import DataFormatter
from email_notification import EmailNotify

def main():
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