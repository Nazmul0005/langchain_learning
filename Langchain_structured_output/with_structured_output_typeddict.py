from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Instantiate the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define the schema using a typed function signature
def review(summary: str, sentiment: str) -> dict:
    """Extracts a summary and sentiment from the input text. First print the summary, then the sentiment."""
    pass
# Use it with structured output
structured_output = model.with_structured_output(review)

# Invoke the model
result = structured_output.invoke(
    "The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix these issues."
)

# Output result
print(result)
