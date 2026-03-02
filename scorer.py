import os
import json
from openai import OpenAI

# Make sure you set your API key as an environment variable:
# Mac/Linux:
# export OPENAI_API_KEY="your_key_here"
# Windows:
# setx OPENAI_API_KEY "your_key_here"

client = OpenAI()

def find_viral_moments(segments):
    full_text = ""
    for seg in segments:
        full_text += seg["text"] + "\n"

    prompt = f"""
You are a viral short-form content strategist.

From this transcript, select 5 highly engaging 30-60 second clips.

Rules:
- Strong hook at the start
- Emotional or controversial moments preferred
- High curiosity factor
- Return ONLY valid JSON

Format:
[
  {{"start": 10, "end": 55}},
  {{"start": 120, "end": 165}}
]

Transcript:
{full_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    try:
        moments = json.loads(content)
    except json.JSONDecodeError:
        print("AI response was not valid JSON. Printing raw output:")
        print(content)
        raise

    return moments
