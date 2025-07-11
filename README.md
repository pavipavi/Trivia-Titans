# Trivia Titans �

A feature-rich console-based quiz game that fetches questions from the Open Trivia Database API.

## Features ✨

- **Multiple Categories**: Choose from 20+ question categories
- **Difficulty Levels**: Easy, Medium, Hard
- **Question Types**: Multiple choice or True/False
- **Smart Input Validation**: Robust error handling for user inputs
- **Performance Tracking**: Score tracking with time measurement
- **Beautiful Console Interface**: Emojis and formatted output
- **Detailed Results**: Comprehensive final results with performance feedback
- **Replay Option**: Play multiple rounds without restarting

## Installation 🚀

1. Clone or download the project
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🎮

Run the game:
```bash
python main.py
```

Follow the on-screen prompts to:
1. Choose number of questions (1-50)
2. Select a category
3. Choose difficulty level
4. Answer questions and get immediate feedback
5. View final results and performance statistics

## Project Structure 📁

```
trivia-titans/
├── main.py              # Main application entry point
├── question_model.py    # Question class definition
├── quiz_brain.py        # Quiz logic and scoring
├── data.py             # API integration and data fetching
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## API Integration 🌐

This game uses the [Open Trivia Database API](https://opentdb.com/):
- Categories: https://opentdb.com/api_category.php
- Questions: https://opentdb.com/api.php

## Error Handling 🛡️

The application includes comprehensive error handling for:
- Network connectivity issues
- SSL certificate problems
- Invalid API responses
- User input validation
- Keyboard interrupts

## Performance Features 📊

- **Time Tracking**: Measures quiz completion time
- **Score Analytics**: Percentage calculation and performance feedback
- **Answer Logging**: Keeps track of all questions and answers
- **Smart Validation**: Accepts both text and numeric inputs for answers

## Customization 🎨

Modify `config.py` to customize:
- API endpoints
- Score thresholds
- Display messages
- Emoji preferences
- Game limits

## Contributing 🤝

Feel free to submit issues, feature requests, or pull requests to improve the game!

## License 📄

This project is open source and available under the MIT License.
