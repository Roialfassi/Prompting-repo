def generate_lesson_plan(topic, duration_minutes, additional_context=""):
    prompt = f"""
Generate a comprehensive lesson plan on the topic of '{topic}' for a {duration_minutes}-minute lesson. The lesson plan should include the following components:

1. Introduction (5-10% of the total duration):
   - Explain the importance and relevance of the topic, providing context and real-world examples.
   - Outline the learning objectives and what students will be able to understand or accomplish by the end of the lesson.

2. Background and Key Concepts (20-30% of the total duration):
   - Provide background information and foundational knowledge necessary to understand the topic.
   - Explain key concepts, theories, or principles related to the topic, using analogies and examples to aid comprehension.
   - Address any prerequisites or assumed knowledge required for the lesson.

3. Practical Examples and Activities (30-40% of the total duration):
   - Incorporate interactive activities, demonstrations, or hands-on exercises to reinforce the concepts.
   - Provide real-world examples and applications of the topic to promote practical understanding.
   - Include sample questions and answers to assess student comprehension and facilitate discussion.

4. Potential Projects or Assignments (10-20% of the total duration):
   - Suggest potential projects, assignments, or extended learning opportunities related to the topic.
   - Outline the objectives, requirements, and evaluation criteria for these projects or assignments.

5. Conclusion and Recap (5-10% of the total duration):
   - Summarize the key points covered in the lesson.
   - Encourage students to reflect on their learning and ask any remaining questions.
   - Provide resources or recommendations for further exploration of the topic.

{additional_context}
"""
    return prompt


# Example usage
if __name__ == '__main__':
    topic = "Retraction Formulas Data structures"
    duration_minutes = 60
    additional_context = "Make sure to include specific examples and mark the importance of the subject to the data structures course"

    lesson_plan_prompt = generate_lesson_plan(topic, duration_minutes, additional_context)
    print(lesson_plan_prompt)
