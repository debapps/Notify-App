import markdown as md

# This module formats the Spreadsheet Data.

class DataFormatter:

    def __init__(self, text, emails):
        self.markdown_text = text
        self.emails = emails

    # Convert Markdown to HTML
    def convert_markdown_to_html(self):
        html_text = md.markdown(self.markdown_text)
        return html_text

    def get_email_list(self):
        return self.emails.split(',')

# md_text = '### Happy Anniversary Sweet Heart!\n\nCelebrate the day with your loved one. '  
# emails = 'anuradhadutta2112@gmail.com, debaditya.bhar@gmail.com'
# f = DataFormatter(md_text, emails)
# print(f.convert_markdown_to_html())
# print(f.get_email_list())