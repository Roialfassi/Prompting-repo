def profile_page_prompt(data_structure_name):
    prompt = f"""
     Task: Create a comprehensive "profile page" that thoroughly explains and illustrates one of the following data structures: {data_structure_name}.

The profile page should be well-structured and organized, covering all the essential components of the chosen data structure. It should be written in a clear and understandable manner, suitable for both beginners and those with some prior knowledge of data structures.

Content Requirements:

1. Introduction:
   - Provide a brief overview of the data structure, explaining what it is and its purpose.
   - Highlight the key characteristics or properties that define the data structure.

2. Definition:
   - Present a formal definition or mathematical representation of the data structure.
   - Clearly state any invariants or rules that must be followed by the data structure.

3. Visual Representation:
   - Include a well-labeled diagram or illustration that visually depicts the structure and organization of the data structure.
   - Use examples or sample data to demonstrate how the data structure would look in different scenarios.

4. Operations:
   - List and describe the fundamental operations supported by the data structure, such as insertion, deletion, search, traversal, etc.
   - For each operation, provide its time complexity analysis (best-case, average-case, and worst-case scenarios) using Big O notation.
   - Optionally, include code snippets or pseudocode to illustrate how these operations are implemented.

5. Use Cases and Applications:
   - Discuss real-world scenarios or problems where the chosen data structure is commonly used or well-suited.
   - Provide specific examples of applications or algorithms that utilize the data structure effectively.
   - Explain the advantages and reasons for choosing this data structure over others in the given use cases.

6. Advantages and Disadvantages:
   - Analyze the strengths and weaknesses of the data structure.
   - Compare it with other similar or related data structures, highlighting the trade-offs and differences.

7. Variations and Specializations (if applicable):
   - Mention any variations or specialized versions of the data structure, such as Self-Balancing Binary Search Trees (for AVL Trees), or Deques (for Queues).
   - Briefly explain how these variations differ from the main data structure and their specific use cases.

8. Questions and Answers:
   - Include a section with commonly asked questions related to the data structure and provide clear and concise answers.
   - These questions can cover topics like implementation details, time and space complexities, trade-offs, or specific edge cases.

9. Further Reading (optional):
   - Provide a list of additional resources, such as books, research papers, or online tutorials, for readers interested in exploring the data structure in more depth.

formatting and Presentation:
- Use appropriate headings, subheadings, and formatting (e.g., bold, italics) to enhance readability and organization.
- Consider using code blocks or syntax highlighting for any code snippets or pseudocode included.
- The profile page should be well-structured, with a logical flow and clear transitions between sections.

Length: The profile page should be comprehensive but concise, aiming for a length of approximately 1000-1500 words, excluding code snippets and visual representations.
     """
    return prompt


if __name__ == '__main__':
    topic = "Queue"
    lesson_plan_prompt = profile_page_prompt(topic)
    print(lesson_plan_prompt)
