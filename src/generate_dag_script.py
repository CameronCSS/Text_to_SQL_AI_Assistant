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

system_prompt = """
            You are a data engineer looking to generate an Airflow pipeline DAG skeleton 
            without the SQL details
            """

user_prompt = f"""
                Generate a cumulative Airflow DAG that transforms 
                {all_schemas['player_seasons.sql']}
                into {all_schemas['players.sql']}
                use markdown for output and Postgres for queries
                The DAG depends on last season data from players table 
                and the DAG depends on past is true
                Make sure each run scans only one season and does a 
                FULL OUTER JOIN with the previous seasons data
                Use the {{ ds }} airflow parameter to filter season 
                All create table statements should include IF NOT EXISTS
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
with open('../output/airflow_dag.py', 'w') as file:
    file.write(content)