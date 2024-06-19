# import re
# import requests
# from bs4 import BeautifulSoup
# import json

# # URL of the HTML content
# url = 'https://vsa-digital.etutor.co/SR_SANKALP_QP_GT-513-01-2023ONLI/SR_SANKALP_QP_GT-513-01-2023ONLI.html'

# # Fetch the HTML content from the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     html_content = response.text

#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Initialize a dictionary to hold questions from 1 to 90
#     questions_dict = {}

#     # Compile the specific pattern to identify div elements with class like 'rvps\d+'
#     specific_pattern = re.compile(r'rvps\d+')

#     # Find all div elements containing questions
#     question_elements = soup.find_all('div', class_=specific_pattern)

#     # Variable to hold current question number
#     current_question_number = None

#     # Iterate through the question elements to extract questions from 1 to 90
#     for question_elem in question_elements:
#         # Find the table within each question element
#         question_table = question_elem.find('table')
#         if question_table:
#             question_trs = question_table.find_all('tr')

#             for question_tr in question_trs:
#                 question_tr_tds = question_tr.find_all('td')

#                 # Check if the current row is a question
#                 if len(question_tr_tds) >= 2:
#                     question_number_text = question_tr_tds[0].text.strip()
#                     question_number_match = re.match(r'^\d+\.$', question_number_text)
#                     if question_number_match:
#                         question_number = question_number_text[:-1]  # Remove the trailing dot
#                         if question_number.isdigit() and int(question_number) <= 90:
#                             question_text = question_tr_tds[1].text.strip()
#                             questions_dict[question_number] = {'question': question_text}
#                             current_question_number = question_number

#                 elif current_question_number and len(question_tr_tds) == 1:
#                     # This handles cases where there's only one cell (likely a continuation of the question text)
#                     question_text = question_tr_tds[0].text.strip()
#                     if current_question_number in questions_dict:
#                         questions_dict[current_question_number]['question'] += ' ' + question_text

#     # Convert the questions dictionary to JSON format
#     questions_json = json.dumps(questions_dict, indent=4)

#     # Print the JSON result
#     print(questions_json)

# else:
#     print(f"Failed to retrieve the URL. Status code: {response.status_code}")


# import re
# import requests
# from bs4 import BeautifulSoup
# import json

# # URL of the HTML content
# url = 'https://vsa-digital.etutor.co/SR_SANKALP_QP_GT-513-01-2023ONLI/SR_SANKALP_QP_GT-513-01-2023ONLI.html'

# # Fetch the HTML content from the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     html_content = response.text

#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Initialize a dictionary to hold questions from 1 to 90
#     questions_dict = {}

#     # Compile the specific pattern to identify div elements with class like 'rvps\d+'
#     specific_pattern = re.compile(r'rvps\d+')

#     # Find all div elements containing questions
#     question_elements = soup.find_all('div', class_=specific_pattern)

#     # Variable to hold current question number
#     current_question_number = None

#     # Iterate through the question elements to extract questions from 1 to 90
#     for question_elem in question_elements:
#         # Find the table within each question element
#         question_table = question_elem.find('table')
#         if question_table:
#             question_trs = question_table.find_all('tr')

#             for question_tr in question_trs:
#                 question_tr_tds = question_tr.find_all('td')

#                 # Check if the current row is a question
#                 if len(question_tr_tds) >= 2:
#                     question_number_text = question_tr_tds[0].text.strip()
#                     question_number_match = re.match(r'^\d+\.$', question_number_text)
#                     if question_number_match:
#                         question_number = question_number_text[:-1]  # Remove the trailing dot
#                         if question_number.isdigit() and int(question_number) <= 90:
#                             question_text = question_tr_tds[1].text.strip()
#                             question_img = question_tr_tds[1].find('img')
#                             question_img_src = question_img['src'] if question_img else None
#                             questions_dict[question_number] = {'question': {'text': question_text, 'img_src': question_img_src}}
#                             current_question_number = question_number

#                 elif current_question_number and len(question_tr_tds) == 1:
#                     # This handles cases where there's only one cell (likely a continuation of the question text)
#                     question_text = question_tr_tds[0].text.strip()
#                     if current_question_number in questions_dict:
#                         questions_dict[current_question_number]['question']['text'] += ' ' + question_text

#                 elif current_question_number and len(question_tr_tds) == 5:
#                     # This is an options row for MCQs
#                     options = {}
#                     for i in range(1, 5, 2):
#                         option_label = question_tr_tds[i].text.strip().replace(')', '')
#                         option_text = question_tr_tds[i+1].text.strip()
#                         option_img = question_tr_tds[i+1].find('img')
#                         option_img_src = option_img['src'] if option_img else None
#                         if option_img_src:
#                             options[option_label] = {'text': option_text, 'img_src': option_img_src}
#                         else:
#                             options[option_label] = {'text': option_text}

#                     questions_dict[current_question_number]['options'] = options

#     # Convert the questions dictionary to JSON format
#     questions_json = json.dumps(questions_dict, indent=4)

#     # Print the JSON result
#     print(questions_json)

# else:
#     print(f"Failed to retrieve the URL. Status code: {response.status_code}")


# import re
# import requests
# from bs4 import BeautifulSoup
# import json

# # URL of the HTML content
# url = 'https://vsa-digital.etutor.co/SR_SANKALP_QP_GT-513-01-2023ONLI/SR_SANKALP_QP_GT-513-01-2023ONLI.html'

# # Fetch the HTML content from the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     html_content = response.text

#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Initialize a dictionary to hold questions from 1 to 90
#     questions_dict = {}

#     # Compile the specific pattern to identify div elements with class like 'rvps\d+'
#     specific_pattern = re.compile(r'rvps\d+')

#     # Find all div elements containing questions
#     question_elements = soup.find_all('div', class_=specific_pattern)

#     # Variable to hold current question number
#     current_question_number = None

#     # Iterate through the question elements to extract questions from 1 to 90
#     for question_elem in question_elements:
#         # Find the table within each question element
#         question_table = question_elem.find('table')
#         if question_table:
#             question_trs = question_table.find_all('tr')

#             for question_tr in question_trs:
#                 question_tr_tds = question_tr.find_all('td')

#                 # Check if the current row is a question
#                 if len(question_tr_tds) >= 2:
#                     question_number_text = question_tr_tds[0].text.strip()
#                     question_number_match = re.match(r'^\d+\.$', question_number_text)
#                     if question_number_match:
#                         question_number = question_number_text[:-1]  # Remove the trailing dot
#                         if question_number.isdigit() and int(question_number) <= 90:
#                             question_text = question_tr_tds[1].text.strip()
#                             question_img = question_tr_tds[1].find('img')
#                             question_img_src = question_img['src'] if question_img else None
#                             questions_dict[question_number] = {'question': {'text': question_text, 'img_src': question_img_src}}
#                             current_question_number = question_number

#                 elif current_question_number and len(question_tr_tds) == 5:
#                     # This is an options row for MCQs
#                     options = {}
#                     for i in range(1, 5, 2):
#                         option_label = chr(64 + i)  # A, B, C, D
#                         option_text = question_tr_tds[i+1].text.strip()
#                         option_img = question_tr_tds[i+1].find('img')
#                         option_img_src = option_img['src'] if option_img else None
#                         options[option_label] = {'text': option_text, 'img_src': option_img_src}

#                     questions_dict[current_question_number]['options'] = options

#     # Convert the questions dictionary to JSON format
#     questions_json = json.dumps(questions_dict, indent=4)

#     # Print the JSON result
#     print(questions_json)

# else:
#     print(f"Failed to retrieve the URL. Status code: {response.status_code}")


import re
import requests
from bs4 import BeautifulSoup
import json

# URL of the HTML content
url = 'https://vsa-digital.etutor.co/SR_SANKALP_QP_GT-513-01-2023ONLI/SR_SANKALP_QP_GT-513-01-2023ONLI.html'

# Fetch the HTML content from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize a dictionary to hold questions from 1 to 90
    questions_dict = {}

    # Compile the specific pattern to identify div elements with class like 'rvps\d+'
    specific_pattern = re.compile(r'rvps\d+')

    # Find all div elements containing questions
    question_elements = soup.find_all('div', class_=specific_pattern)

    # Variable to hold current question number
    current_question_number = None

    # Iterate through the question elements to extract questions from 1 to 90
    for question_elem in question_elements:
        # Find the table within each question element
        question_table = question_elem.find('table')
        if question_table:
            question_trs = question_table.find_all('tr')

            for question_tr in question_trs:
                question_tr_tds = question_tr.find_all('td')

                # Check if the current row is a question
                if len(question_tr_tds) >= 2:
                    question_number_text = question_tr_tds[0].text.strip()
                    question_number_match = re.match(r'^\d+\.$', question_number_text)
                    if question_number_match:
                        question_number = question_number_text[:-1]  # Remove the trailing dot
                        if question_number.isdigit() and int(question_number) <= 90:
                            question_text = question_tr_tds[1].text.strip()
                            question_img = question_tr_tds[1].find('img')
                            question_img_src = question_img['src'] if question_img else None
                            questions_dict[question_number] = {'question': {'text': question_text, 'img_src': question_img_src}}
                            current_question_number = question_number

                elif current_question_number and len(question_tr_tds) == 5:
                    # This is an options row for MCQs
                    options = {}
                    for i in range(1, 5, 2):
                        option_label = chr(64 + i)  # A, B, C, D
                        option_text = question_tr_tds[i+1].text.strip()
                        option_img = question_tr_tds[i+1].find('img')
                        option_img_src = option_img['src'] if option_img else None
                        options[option_label] = {'text': option_text, 'img_src': option_img_src}

                    questions_dict[current_question_number]['options'] = options

    # Convert the questions dictionary to JSON format
    questions_json = json.dumps(questions_dict, indent=4)

    # Print the JSON result
    print(questions_json)

else:
    print(f"Failed to retrieve the URL. Status code: {response.status_code}")



