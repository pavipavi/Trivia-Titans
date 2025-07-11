import time
from datetime import datetime
import config

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.start_time = None
        self.answers_log = []
        self.current_question = None
    
    def start_quiz(self):
        """Start the quiz and record start time"""
        self.start_time = datetime.now()
        print(f"{config.EMOJIS['target']} Quiz Started!")
        print("=" * 50)
    
    def has_more_questions(self):
        """Check if there are more questions to ask"""
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        """Display the next question and return it"""
        if not self.has_more_questions():
            return None
            
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        print(f"\n{config.EMOJIS['memo']} Question {self.question_number}/{len(self.question_list)}")
        print(f"Category: {self.current_question.category or 'General'}")
        print(f"Difficulty: {self.current_question.difficulty or 'Unknown'}")
        print("-" * 50)
        print(f"Q: {self.current_question.question}")
        
        if self.current_question.choices:
            print("\nChoices:")
            for index, choice in enumerate(self.current_question.choices, start=1):
                print(f"  {index}. {choice}")
        
        return self.current_question
    
    def check_answer(self, user_answer):
        """Check if the user's answer is correct and provide feedback"""
        if not self.current_question:
            return False
        
        # Convert string input to int if it's a number
        if isinstance(user_answer, str) and user_answer.isdigit():
            user_answer = int(user_answer)
        
        is_correct = self.current_question.is_correct_answer(user_answer)
        
        if is_correct:
            self.score += 1
            print(f"{config.EMOJIS['correct']} Correct!")
        else:
            print(f"{config.EMOJIS['wrong']} Wrong! The correct answer was: {self.current_question.correct_answer}")
        
        # Log the answer
        self.answers_log.append({
            'question': self.current_question.question,
            'user_answer': user_answer,
            'correct_answer': self.current_question.correct_answer,
            'is_correct': is_correct
        })
        
        print(f"Current Score: {self.score}/{self.question_number}")
        return is_correct
    
    def get_final_score(self):
        """Calculate and return final score statistics"""
        total_questions = len(self.question_list)
        percentage = (self.score / total_questions) * 100 if total_questions > 0 else 0
        
        end_time = datetime.now()
        duration = end_time - self.start_time if self.start_time else None
        
        return {
            'score': self.score,
            'total': total_questions,
            'percentage': percentage,
            'duration': duration,
            'answers_log': self.answers_log
        }
    
    def display_final_results(self):
        """Display comprehensive final results"""
        results = self.get_final_score()
        
        print("\n" + "=" * 50)
        print(f"{config.EMOJIS['trophy']} QUIZ COMPLETED!")
        print("=" * 50)
        print(f"Final Score: {results['score']}/{results['total']}")
        print(f"Percentage: {results['percentage']:.1f}%")
        
        if results['duration']:
            print(f"{config.EMOJIS['clock']} Time Taken: {results['duration']}")
        
        # Performance feedback using config
        if results['percentage'] >= config.SCORE_THRESHOLDS['excellent']:
            print(config.SCORE_MESSAGES['excellent'])
        elif results['percentage'] >= config.SCORE_THRESHOLDS['good']:
            print(config.SCORE_MESSAGES['good'])
        elif results['percentage'] >= config.SCORE_THRESHOLDS['average']:
            print(config.SCORE_MESSAGES['average'])
        else:
            print(config.SCORE_MESSAGES['poor'])
        
        return results
        
