PROMPT_PLANNER_TASK = '''
Design a clear and concise plan for the current development step: {step_name}. The development team will execute tasks based on your plan. I will provide you with COMPETITION INFORMATION, RESOURCE CONSTRAINTS, and previous reports and plans. Using this information, structure the plan thoughtfully.
In your response, briefly outline the task objectives, then specify the essential methods and constraints to consider. Focus strictly on tasks relevant to this step, avoiding those belonging to other phases.
<example>
- During the in-depth EDA step, only consider features that significantly impact the target variable when plotting data analysis charts to avoid long runtimes and redundant information.
- Analyze the distribution and statistical properties of features without deleting or reducing them, as feature reduction belongs to the feature engineering step.
</example>
Ensure the plan addresses key dependencies, resource availability, and time constraints without overcomplicating the process. The goal is to create an efficient and adaptable plan, emphasizing clarity and practicality over complexity.
Note: The plan should include a maximum of four tasks, with clear methods and constraints, guiding developers to effectively execute the critical steps of the current phase.
'''


PROMPT_PLANNER = '''
# CONTEXT #
{steps_in_context}
Currently, I am at step: {step_name}.
#############
# MESSAGE FROM LAST STEP #
{message}
#############
# COMPETITION INFORMATION #
{competition_info}
#############
# RESOURCE CONSTRAINTS #
- Always consider the runtime and efficiency of your code when writing code, especially for data visualization, handling large datasets, or complex algorithms.
<example>
Data visualization: When using libraries such as seaborn or matplotlib to create plots, consider turning off unnecessary details (e.g., annot=False in heatmaps), especially when the number of data points is large.
</example>
- Always consider resource constraints and limit the number of generated images to ensure that they do not exceed 10 when performing Exploratory Data Analysis (EDA), 
    - **Note that the generated images should be LIMITED to the most critical visualizations that provide valuable insights.**
#############
# TASK #
{task}
#############
# RESPONSE #
Let's work this out in a step by step way.
#############
# START PLANNING #
If you understand, please request the report and plan from the previous step. These documents contain important information that will guide your planning. In addition to the report and plan, I will also provide some sample data for your analysis. This will help you create a more accurate and tailored plan for the current step. Your plan should closely follow the previous step, maintain logical consistency, and avoid any duplication of tasks.
'''

# You can use the following template to guide your response:
# Thought: you should always think about what to do to complete the task
# Action: the action to take
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Final Thought: I now know the final answer
# Final Answer: the final answer to the original input question

PROMPT_PLNNAER_ROUND2 = '''
# TASK #
Please extract essential information from your answer and reorganize into a specified JSON format. You need to organize the information in a clear and concise manner, ensuring that the content is logically structured and easy to understand. You must ensure that the essential information is complete and accurate.
#############
# RESPONSE: JSON FORMAT #
Here is the JSON format you should follow:
```json
{{
    "final_answer": list=[
        {{
            "task": str="The specific task to be performed",
            "method": list=["Methods to be used"],
            "constraints": list=["Any constraints or considerations to keep in mind"]
        }}
    ]
}}
```
#############
# START REORGANIZING #
'''
# ```json
# {{
#     "thought_process": list=[
#         {{
#             "thought": str="Reflect on the current situation and consider how to proceed in fulfilling the user's requirements.",
#             "action": str="Describe the action you plan to take to meet the user's needs.",
#             "observation": str="Note the expected or actual results of the action."
#         }}
#     ],
#     "final_thought": str="Summarize your understanding and confirm that you now have the final answer.",
#     "final_answer": list=[
#         {{
#             "task": str="The specific task to be performed",
#             "method": list=["Methods to be used"],
#         }}
#     ]
# }}
# ```

# ## Thought Process ##
# (This Thought/Action/Observation sequence may repeat as needed.)
# - Thought: str="Reflect on the current situation and consider how to proceed in fulfilling the user's requirements."
# - Action: str="Describe the action you plan to take to meet the user's needs."
# - Observation: str="Note the expected or actual results of the action."
# ## Final Thought ##
# str="Summarize your understanding and confirm that you now have the final answer."
# ## Final Answer ##
# str="Provide the final answer to the original task."

# Here is an example of planning for the preliminary EDA step:
# [
#     {{
#         "task": "Understand the Structure of the Data",
#         "method": [
#             "Load the train.csv and test.csv datasets",
#             "Display the first few rows of the datasets using head()",
#             "Use info() to get a summary of the datasets, including the number of non-null entries and data types",
#             "Use describe() to get basic statistical summaries of the numerical features"
#         ]
#     }},
#     {{
#         "task": "Identify and Visualize Missing Values",
#         "method": [
#             "Use isnull().sum() to count the number of missing values in each column"
#         ]
#     }},
#     {{
#         "task": "Detect Outliers and Analyze Relationships",
#         "method": [
#             "Use box plots to visualize the distribution of numerical features and identify outliers",
#             "Use correlation matrices to identify the strength and direction of relationships between numerical features and SalePrice"
#         ]
#     }}
# ]