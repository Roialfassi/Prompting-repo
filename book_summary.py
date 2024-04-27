def summarize_book(book_name, author, added_information_on_book):
    prompt = f"""
Task: The book {book_name} by {author} , {added_information_on_book}
Your task is to create a comprehensive summary that captures the essence of the book, with a focus on understanding the author's intended lessons, teachings, and the development of the craft/skill/values portrayed.

The summary should include the following components:

1. Key Takeaways and Lessons:
   - Identify the main themes, messages, and lessons the author aims to convey through the book.
   - Present these takeaways and lessons in the form of bullet points or a concise list.
   - Explain how the author reinforces or illustrates these lessons throughout the narrative or through specific examples.

2. Understanding the Craft/Skill/Values:
   - Analyze the craft, skill, or set of values that are central to the book's narrative or subject matter.
   - Describe how the author introduces, develops, and reinforces this craft/skill/values throughout the book.
   - Highlight any specific techniques, principles, or methods the author presents for mastering or embracing this craft/skill/values.
   - Discuss the significance or importance of this craft/skill/values within the context of the book's themes or real-world applications.

3. Major Plot Summary (in chronological order):
   - Provide a concise summary of the book's major plotlines or narrative arcs, presented in chronological order.
   - Highlight the key events, turning points, or character developments that drive the story forward.
   - Avoid excessive details or spoilers, but ensure that the summaries capture the essence of each major plot or narrative thread.

4. Character Analysis (optional):
   - If the book has significant character development or memorable characters, you may choose to include a brief character analysis section.
   - Identify the main characters and their roles within the narrative.
   - Discuss any notable character arcs, growth, or transformations that occur throughout the book.

Guidelines:
- Keep the summary concise and focused, aiming for a length of approximately 500-800 words, excluding the bullet points or lists.
- Use clear and engaging language to convey the book's essence and the author's intent effectively.
- Avoid excessive plot details or spoilers that may diminish the reading experience for others.
- If you need clarification or have any specific questions about the book, feel free to ask.

Please provide a comprehensive summary of the book, following the outlined structure and guidelines, to help readers gain an understanding of the author's intended lessons, teachings, and the development of the craft/skill/values portrayed, while also covering the major plots chronologically.
"""
    return prompt


if __name__ == '__main__':
    name = "The 48 Laws of Power"
    author_name = "Robert Greene"
    added_information = "published at 1988"
    print(summarize_book(name, author_name, added_information))
