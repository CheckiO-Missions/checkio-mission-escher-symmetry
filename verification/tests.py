"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 1, 2]],
            "answer": True,
        },
        {
            "input": [[1, 3, 2, 1, 3]],
            "answer": True,
        },
        {
            "input": [[1, 2, 2, 1]],
            "answer": False,
        },
        {
            "input": [[4, 4, 4, 4, 4, 4, 4, 4, 4]],
            "answer": True,
        },
    ],
    "Extra": [
        {
            "input": [[1, 2, 3, 2, 1]],
            "answer": False,
        },
        {
            "input": [[1, 0, 1, 0, 1, 0]],
            "answer": True,
        },
        {
            "input": [[1, 8, 5, 6, 6, 1, 9, 4, 4, 5, 2, 9]],
            "answer": True,
        },
        {
            "input": [[3, 6, 6, 4, 3, 2, 8, 7, 6, 4, 4, 7]],
            "answer": True,
        },
        {
            "input": [[1, 2, 1]],
            "answer": False,
        },
    ]
}
