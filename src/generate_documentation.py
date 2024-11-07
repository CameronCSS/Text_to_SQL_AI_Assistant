import anthropic
import os

# Read the API key directly from the file
with open('../apikey.env', 'r') as file:
    API_KEY = file.read().strip()

client = anthropic.Anthropic(api_key=API_KEY)

schema_files = os.listdir('../schemas')

all_schemas = {}

for file in schema_files:
    opened_file = open('../schemas/' + file, 'r')
    all_schemas[file] = opened_file.read()

system_prompt = """You are a data engineer looking to create documentation and example queries for your data sets"""

# You may need to alter this prompt to get what you want
user_prompt = f"""Using our main table scheme {all_schemas['employee_info.sql']}
                Generate a pipeline documentation in markdown format to show how these 
                two related tables {all_schemas['Retail_sales.sql']}
                and {all_schemas['Employee_satisfaction.sql']}
                are related to eachother and the original table
                make sure to include example queries
                make sure to document all columns with column comments
                make sure to document all created types as well
            """


message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    temperature=0,
    system= system_prompt,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt
                }
            ]
        }
    ]
)

# # USE to test Print the output before writing.
# print(message.content)


# Extract the text content from the message
content = message.content[0].text if isinstance(message.content, list) else message.content

if not os.path.exists('../output'):
    os.mkdir('../output')

# Write the content to file
with open('../output/documentation.md', 'w') as file:
    file.write(content)
