# Configuration file for the Quiz Game

# API Configuration
API_BASE_URL = "https://opentdb.com/api.php"
CATEGORIES_URL = "https://opentdb.com/api_category.php"
REQUEST_TIMEOUT = 10
MAX_RETRIES = 3

# Game Configuration
DEFAULT_QUESTION_COUNT = 10
MIN_QUESTION_COUNT = 1
MAX_QUESTION_COUNT = 50

# Difficulty levels
DIFFICULTY_LEVELS = ['easy', 'medium', 'hard']

# Question types
QUESTION_TYPES = ['multiple', 'boolean']

# Display Configuration
EMOJIS = {
    'correct': '✅',
    'wrong': '❌',
    'star': '🌟',
    'trophy': '🏆',
    'book': '📚',
    'target': '🎯',
    'fire': '🔥',
    'thumbs_up': '👍',
    'muscle': '💪',
    'party': '🎉',
    'graduation': '🎓',
    'gear': '⚙️',
    'brain': '🧠',
    'lightning': '⚡',
    'hourglass': '⏳',
    'rocket': '🚀',
    'question': '❓',
    'memo': '📝',
    'clock': '🕐'
}

# Scoring thresholds
SCORE_THRESHOLDS = {
    'excellent': 80,
    'good': 60,
    'average': 40
}

# Messages
WELCOME_MESSAGE = f"{EMOJIS['graduation']} Welcome to Trivia Titans!"
SCORE_MESSAGES = {
    'excellent': f"{EMOJIS['star']} Excellent work! You're a true Titan!",
    'good': f"{EMOJIS['thumbs_up']} Good job! Titan in training!",
    'average': f"{EMOJIS['book']} Keep studying to become a Titan!",
    'poor': f"{EMOJIS['muscle']} Train harder to join the Titans!"
}
