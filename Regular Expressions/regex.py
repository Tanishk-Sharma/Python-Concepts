import re

my_str = """
Hi There!
Here are our contact details:

If you would like to contact me, please send a mail to someusername@somedomain.com
If you want to get in touch with Sales, please mail to salesusername@somedomain.com
Our vendors would be happy to respond on vendormail@vendordomain.net
Thanks for your interest!
Great Guy,
Some Company,
companyaddress@companydomain.xyz
"""

mail_pattern = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{3}'

all_mails_from_text = re.findall(mail_pattern, my_str)

for mail_id in all_mails_from_text:
  print(mail_id)
