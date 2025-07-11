import random

class Question:
    def __init__(self, question, correct_answer, incorrect_answers=None, category=None, difficulty=None):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers or []
        self.category = category
        self.difficulty = difficulty
        
        # Create shuffled choices for multiple choice questions
        self.choices = self._create_shuffled_choices()
    
    def _create_shuffled_choices(self):
        """Create a shuffled list of all answer choices"""
        if not self.incorrect_answers:
            return []
        
        all_choices = [self.correct_answer] + self.incorrect_answers
        random.shuffle(all_choices)
        return all_choices
    
    def get_correct_choice_index(self):
        """Return the index (1-based) of the correct answer in the choices list"""
        if not self.choices:
            return None
        return self.choices.index(self.correct_answer) + 1
    
    def is_correct_answer(self, user_answer):
        """Check if user answer is correct (works for both text and index)"""
        if isinstance(user_answer, str):
            return user_answer.lower().strip() == self.correct_answer.lower().strip()
        elif isinstance(user_answer, int):
            return user_answer == self.get_correct_choice_index()
        return False