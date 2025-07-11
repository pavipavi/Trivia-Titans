# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]



import requests
import ssl
from urllib3.exceptions import InsecureRequestWarning
import html

# Disable SSL warnings if we need to bypass SSL verification
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def fetch_categories():
    """Fetch available categories from Open Trivia Database"""
    url = "https://opentdb.com/api_category.php"
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.SSLError:
        response = requests.get(url, verify=False, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        return data['trivia_categories']
    else:
        raise Exception(f"Failed to fetch categories: {response.status_code}")

def fetch_questions(amount=10, category=None, difficulty='easy', question_type='multiple'):
    """Fetch questions from Open Trivia Database with better error handling"""
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type={question_type}"
    
    if category:
        url += f"&category={category}"
    
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.SSLError:
        response = requests.get(url, verify=False, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0:
            # Decode HTML entities in questions and answers
            for question in data['results']:
                question['question'] = html.unescape(question['question'])
                question['correct_answer'] = html.unescape(question['correct_answer'])
                question['incorrect_answers'] = [html.unescape(ans) for ans in question['incorrect_answers']]
            return data['results']
        else:
            raise Exception(f"API Error: {data['response_code']} - No questions found for these parameters")
    else:
        raise Exception(f"Failed to fetch questions: {response.status_code}")
