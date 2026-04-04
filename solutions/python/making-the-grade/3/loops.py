"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    credited_scores = [round(score) for score in student_scores]

    return credited_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    failing_score = 40
    passing_brackets = 4 # Four passing brackets in order: A, B, C, and D
    step = round((highest - failing_score) / passing_brackets)
    
    lower_thresholds = list(range(failing_score+1, highest, step))
    return lower_thresholds


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    if len(student_scores) != len(student_names):
        raise ValueError("Missing/extra value detected.")
        
    ranking_string = []
    for index in range(len(student_scores)):
        rank = f'{index+1}. '
        name = f'{student_names[index]}: '
        score = f'{student_scores[index]}'
        ranking_string.append(rank + name + score)
        
    return ranking_string
        
        

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    creme_de_crop = []
    for [name, score] in student_info:
        if score == 100:
            creme_de_crop = [name, score]
            return creme_de_crop

    return creme_de_crop
    
