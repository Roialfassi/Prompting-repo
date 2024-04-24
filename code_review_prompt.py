def generate_code_review_prompt(language, function_code):
    prompt = f"""
    Perform a comprehensive code review of the following function written in {language}:
    
    On this function:
    {function_code}
        
    The code review should cover the following aspects:

    Functionality:
    Does the function correctly implement the intended behavior and meet its requirements?
    Are there any edge cases or corner cases that the function does not handle properly?
    Are there any potential bugs or logical errors in the function?
    
    Code Style and Readability:
    Does the code follow the appropriate style guide and coding conventions for {language}?
    Are variable and function names meaningful and descriptive?
    Is the code well-formatted and easy to read?
    
    Error Handling and Robustness:
    Does the function properly handle and propagate errors and exceptions?
    Are input parameters validated and sanitized appropriately?
    Are there any potential security vulnerabilities or risks?
    
    Performance and Efficiency:
    Can the function's performance be improved through better algorithms, data structures, or optimization techniques?
    Are there any unnecessary computations or memory allocations that can be avoided?
    
    Documentation and Comments:
    Is the function properly documented with comments, docstrings, or other appropriate documentation?
    Are complex or non-obvious sections of the code adequately explained?
    
    Modularity and Reusability:
    Can the function be broken down into smaller, more modular components for better reusability?
    Are there any opportunities for code refactoring or abstraction?
    
    Testing and Verification:
    Are there any existing unit tests or test cases for the function?
    Can you suggest additional test cases or scenarios to improve code coverage and verification?
    
    Language-Specific Considerations:
    Does the function adhere to language-specific conventions, idioms, or best practices for {language}?
    Are language features, libraries, or frameworks utilized effectively?
    
    Potential Improvements:
    Suggest any improvements or alternative approaches that could enhance the function's functionality, readability, or performance.
    
    Overall Assessment:
    Provide an overall assessment of the function's quality, strengths, and weaknesses.
    Summarize the most critical areas for improvement or refactoring.
    
    Please provide a detailed and structured code review, addressing each aspect listed above. Use appropriate code formatting and examples to illustrate your points and 
    
    Please provide a suggested implementation to a better way of writing this function
"""

if __name__ == '__main__':
    language = "Python"
    the_function = """
    def greet():
        print('Hello World!')
    """
    code_quality_prompt = generate_code_review_prompt(language, the_function)
    print(code_quality_prompt)
