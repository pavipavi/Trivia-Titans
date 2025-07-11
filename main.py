from question_model import Question
from data import fetch_questions, fetch_categories
from quiz_brain import QuizBrain
import sys
import config

def get_valid_input(prompt, valid_options=None, input_type=int):
    """Get valid input from user with error handling"""
    while True:
        try:
            user_input = input(prompt).strip()
            
            if input_type == int:
                value = int(user_input)
                if valid_options and value not in valid_options:
                    print(f"Please enter a number between {min(valid_options)} and {max(valid_options)}")
                    continue
                return value
            elif input_type == str:
                if valid_options and user_input.lower() not in valid_options:
                    print(f"Please enter one of: {', '.join(valid_options)}")
                    continue
                return user_input.lower()
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please try again.")
        except KeyboardInterrupt:
            print("\nQuiz cancelled by user.")
            sys.exit()

def display_categories(categories):
    """Display available categories in a formatted way"""
    print(f"\n{config.EMOJIS['book']} Available Categories:")
    print("-" * 30)
    for i, category in enumerate(categories, 1):
        print(f"{i:2d}. {category['name']}")
    print("-" * 30)

def main():
    """Main quiz application"""
    print(config.WELCOME_MESSAGE)
    print("=" * 50)
    
    try:
        # Get number of questions
        num_questions = get_valid_input(
            f"Enter the number of questions ({config.MIN_QUESTION_COUNT}-{config.MAX_QUESTION_COUNT}): ",
            valid_options=range(config.MIN_QUESTION_COUNT, config.MAX_QUESTION_COUNT + 1)
        )
        
        # Get categories
        print(f"\n{config.EMOJIS['target']} Fetching categories...")
        categories = fetch_categories()
        display_categories(categories)
        
        category_choice = get_valid_input(
            f"Choose a category (1-{len(categories)}) or 0 for any: ",
            valid_options=range(0, len(categories) + 1)
        )
        
        selected_category = categories[category_choice - 1]['id'] if category_choice > 0 else None
        category_name = categories[category_choice - 1]['name'] if category_choice > 0 else "Mixed"
        
        # Get difficulty
        difficulty = get_valid_input(
            f"{config.EMOJIS['fire']} Choose difficulty ({'/'.join(config.DIFFICULTY_LEVELS)}): ",
            valid_options=config.DIFFICULTY_LEVELS,
            input_type=str
        )
        
        
        print(f"\n{config.EMOJIS['target']} Fetching {num_questions} {difficulty} questions from {category_name}...")
        
        # Fetch questions
        question_data = fetch_questions(
            amount=num_questions,
            category=selected_category,
            difficulty=difficulty
           
        )
        
        # Create question objects
        question_bank = []
        for item in question_data:
            question = Question(
                question=item["question"],
                correct_answer=item["correct_answer"],
                incorrect_answers=item.get("incorrect_answers", []),
                category=item.get("category"),
                difficulty=item.get("difficulty")
            )
            question_bank.append(question)
        
        # Start quiz
        quiz = QuizBrain(question_bank)
        quiz.start_quiz()
        
        # Main quiz loop
        while quiz.has_more_questions():
            current_question = quiz.next_question()
            user_answer = get_valid_input(
                    f"\n{config.EMOJIS['target']} Your answer (enter number): ",
                    valid_options=range(1, len(current_question.choices) + 1)
                )
           
            
            quiz.check_answer(user_answer)
            
            # Small delay for better UX
            if quiz.has_more_questions():
                input(f"\n{config.EMOJIS['target']} Press Enter to continue...")
        
        # Display final results
        results = quiz.display_final_results()
        
        # Ask if user wants to play again
        play_again = get_valid_input(
            f"\n{config.EMOJIS['party']} Would you like to play again? (yes/no): ",
            valid_options=['yes', 'no', 'y', 'n'],
            input_type=str
        )
        
        if play_again in ['yes', 'y']:
            main()
        else:
            print(f"Thanks for playing! {config.EMOJIS['party']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again or check your internet connection.")

if __name__ == "__main__":
    main()