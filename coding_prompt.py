def generate_code_quality_prompt(language, project_type, the_task):
    prompt = f"""
You are tasked with writing code in {language} for a {project_type} project. Your code should adhere to the following industry standards and best practices:

1. Code Organization:
   - Follow a consistent and logical structure for the project.
   - Separate concerns by organizing code into appropriate modules, classes, or files.
   - Use descriptive and meaningful names for variables, functions, classes, and files.

2. Commenting:
   - Provide clear and concise comments to explain the purpose and functionality of code segments.
   - Use docstrings or similar documentation conventions to document functions, classes, and modules.
   - Comment complex or non-obvious code to improve readability and maintainability.

3. Error Handling and Exceptions:
   - Implement proper error handling mechanisms using try-except blocks or similar constructs.
   - Raise appropriate exceptions when encountering exceptional situations.
   - Handle and gracefully recover from potential exceptions or error conditions.

4. Function Design:
   - Follow the principles of modularity and reusability when defining functions.
   - Use appropriate function signatures and parameter lists.
   - Adhere to naming conventions and coding styles specific to {language}.
   - Ensure functions have a single, well-defined responsibility.

5. Code Style and Formatting:
   - Follow the official style guide or coding conventions for {language}.
   - Maintain consistent indentation, spacing, and formatting throughout the codebase.
   - Use appropriate naming conventions for variables, functions, classes, and other identifiers.

6. Input Validation and Sanitization:
   - Implement input validation and sanitization to handle user input and prevent security vulnerabilities.
   - Validate input data types, ranges, and formats as necessary.
   - Sanitize or escape user input to prevent injection attacks or other security risks.

7. Performance Considerations:
   - Optimize critical sections of the code for performance, if applicable.
   - Consider appropriate data structures and algorithms to improve efficiency.
   - Avoid unnecessary computations or memory allocations.

8. Documentation and Readability:
   - Provide clear and concise documentation, including comments, docstrings, and external documentation (if applicable).
   - Write self-documenting code by using descriptive variable and function names.
   - Consider using code examples or usage scenarios to illustrate the intended behavior.

9. Testing and Debugging:
   - Implement unit tests or other appropriate testing strategies to ensure code correctness.
   - Include debugging statements or logging mechanisms to aid in troubleshooting and error diagnosis.

10. Language-Specific Considerations:
    - Adhere to any language-specific conventions, idioms, or best practices for {language}.
    - Utilize language features, libraries, or frameworks appropriately and effectively.

Please ensure that your code follows these industry standards and best practices for {language} and {project_type} projects.

The task of this mission is: {the_task}
"""
    return prompt


if __name__ == '__main__':
    language = "Vue3"
    project_type = "web application"
    the_task = "write me a landing page for a truck delivery company"
    code_quality_prompt = generate_code_quality_prompt(language, project_type, the_task)
    print(code_quality_prompt)
