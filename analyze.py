import json
import os
from typing import Any, Dict
from litellm import completion

# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "groq/llama-3.3-70b-versatile"

def get_itinerary(destination):

    prompt = f"""
    Create a travel itinerary in JSON format for {destination}.

    The JSON must contain:
    destination
    price_range
    ideal_visit_times
    top_attractions
    """

    response = completion(
        model="groq/llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        api_key=os.getenv("GROQ_API_KEY")
    )

    content = response['choices'][0]['message']['content']
# limpiar bloques ```json
    content = content.replace("```json", "").replace("```", "").strip()
    return json.loads(content)
