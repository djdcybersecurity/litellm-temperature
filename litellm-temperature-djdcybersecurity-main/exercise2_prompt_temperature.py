import os
from openai import OpenAI

# Read environment variables
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL", "https://litellm.lib.ou.edu/v1")
model_name = os.getenv(
    "LITELLM_MODEL",
    "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
)

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Export it before running this script.")

# Create OpenAI client pointing at LiteLLM gateway
client = OpenAI(api_key=api_key, base_url=base_url)

# System + user messages
system_message = (
    "You are a concise automation engineer who always answers in exactly three "
    "short bullet points, using plain language."
)

user_question = (
    "Explain, for a new OU-Tulsa Polytechnic student, why learning to call LLM APIs "
    "is useful for process automation."
)

def ask_with_temperature(temp: float) -> str:
    """
    Send the same messages with a specific temperature and return the text.
    """
    response = client.chat.completions.create(
        model=model_name,
        temperature=temp,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_question},
        ],
    )
    return response.choices[0].message.content.strip()

def main() -> None:
    low_temp = 0.0
    high_temp = 1.0

    print(f"Using model: {model_name}")
    print(f"Base URL:    {base_url}")
    print()

    print(f"Requesting answer with LOW TEMP = {low_temp} ...")
    low_answer = ask_with_temperature(low_temp)
    print()

    print(f"Requesting answer with HIGH TEMP = {high_temp} ...")
    high_answer = ask_with_temperature(high_temp)
    print()

    print("=" * 80)
    print(f"LOW TEMP ({low_temp})")
    print("=" * 80)
    print(low_answer)
    print()

    print("=" * 80)
    print(f"HIGH TEMP ({high_temp})")
    print("=" * 80)
    print(high_answer)
    print()

if __name__ == "__main__":
    main()

