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

    # Initialize a dictionary to hold all questions and their options
    questions_dict = {}

    # Compile the specific pattern to identify div elements with class like 'rvps\d+'
    specific_pattern = re.compile(r'rvps\d+')

    # Find all div elements containing questions
    question_elements = soup.find_all('div', class_=specific_pattern)

    # Variable to hold current question number
    current_question_number = None

    # Iterate through the question elements to extract questions and options
    for question_elem in question_elements:
        # Find the table within each question element
        question_table = question_elem.find('table')
        if question_table:
            question_trs = question_table.find_all('tr')

            for question_tr in question_trs:
                question_tr_tds = question_tr.find_all('td')

                # Check if the current row is a question or an option
                if len(question_tr_tds) == 2 and 'colspan' in question_tr_tds[1].attrs:
                    # This is a question row
                    question_number = question_tr_tds[0].text.strip().replace('.', '')
                    current_question_number = question_number
                    question_img = question_tr_tds[1].find('img')
                    question_img_src = question_img['src'] if question_img else None
                    questions_dict[question_number] = {'question': question_img_src, 'options': {}}

                elif current_question_number and len(question_tr_tds) == 5:
                    # This is an options row
                    for i in range(1, 5, 2):
                        option_label = question_tr_tds[i].text.strip().replace(')', '')
                        option_text = question_tr_tds[i+1].text.strip()
                        option_img = question_tr_tds[i+1].find('img')
                        option_img_src = option_img['src'] if option_img else None
                        if option_img_src:
                            questions_dict[current_question_number]['options'][option_label] = option_img_src
                        else:
                            questions_dict[current_question_number]['options'][option_label] = option_text

    # Convert the questions dictionary to JSON format
    questions_json = json.dumps(questions_dict, indent=4)

    # Print the JSON result
    print(questions_json)

else:
    print(f"Failed to retrieve the URL. Status code: {response.status_code}")


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

#     # Initialize dictionaries to hold all questions and their options
#     questions_dict = {
#         'mcq': {},
#         'numerical': {}
#     }

#     # Compile the specific pattern to identify div elements with class like 'rvps\d+'
#     specific_pattern = re.compile(r'rvps\d+')

#     # Find all div elements containing questions
#     question_elements = soup.find_all('div', class_=specific_pattern)

#     # Variable to hold current question number
#     current_question_number = None
#     current_question_type = None

#     # Iterate through the question elements to extract questions and options
#     for question_elem in question_elements:
#         # Find the table within each question element
#         question_table = question_elem.find('table')
#         if question_table:
#             question_trs = question_table.find_all('tr')

#             for question_tr in question_trs:
#                 question_tr_tds = question_tr.find_all('td')

#                 # Check if the current row is a question or an option
#                 if len(question_tr_tds) == 2 and 'colspan' in question_tr_tds[1].attrs:
#                     # This is a question row
#                     question_number = question_tr_tds[0].text.strip().replace('.', '')
#                     current_question_number = question_number
#                     question_img = question_tr_tds[1].find('img')
#                     question_img_src = question_img['src'] if question_img else None
#                     current_question_type = 'numerical' if len(question_tr_tds[1].find_all('td')) == 2 else 'mcq'

#                     # Initialize the dictionary for MCQ questions if not already initialized
#                     if current_question_type == 'mcq' and current_question_number not in questions_dict['mcq']:
#                         questions_dict['mcq'][current_question_number] = {'options': {}}

#                     # Check if it's a numerical question (no options)
#                     if current_question_type == 'numerical':
#                         questions_dict[current_question_type][question_number] = {'question': question_img_src}

#                 elif current_question_number and len(question_tr_tds) == 5:
#                     # This is an options row for MCQ
#                     for i in range(1, 5, 2):
#                         option_label = question_tr_tds[i].text.strip().replace(')', '')
#                         option_text = question_tr_tds[i+1].text.strip()
#                         option_img = question_tr_tds[i+1].find('img')
#                         option_img_src = option_img['src'] if option_img else None

#                         # Ensure options dictionary for the current MCQ question is initialized
#                         if current_question_number in questions_dict['mcq']:
#                             questions_dict['mcq'][current_question_number]['options'][option_label] = option_img_src
#                         else:
#                             questions_dict['mcq'][current_question_number] = {'options': {option_label: option_img_src}}

#     # Convert the questions dictionary to JSON format
#     questions_json = json.dumps(questions_dict, indent=4)

#     # Print the JSON result
#     print(questions_json)

# else:
#     print(f"Failed to retrieve the URL. Status code: {response.status_code}")
