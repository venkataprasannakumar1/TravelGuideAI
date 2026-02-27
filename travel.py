import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API key not found. Check .env file")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

def generate_itinerary(destination, days, nights, interests):

    prompt = f"""
    Create a detailed travel itinerary.

    Destination: {destination}
    Duration: {days} days and {nights} nights
    Interests: {interests}

    Include:
    - Day wise plan
    - Attractions
    - Food suggestions
    - Travel tips
    - Summary
    """

    response = client.models.generate_content(
    model="gemini-1.5-flash-latest",
    contents=prompt
)


    return response.text


st.title("🌍 Travel Guide AI")

destination = st.text_input("Destination")

col1, col2 = st.columns(2)

with col1:
    days = st.number_input("Days", min_value=1, max_value=15, value=3)

with col2:
    nights = st.number_input("Nights", min_value=1, max_value=15, value=2)

interests = st.text_area("Interests")

if st.button("Generate Itinerary"):

    if destination.strip() == "":
        st.warning("Please enter destination")
    else:
        with st.spinner("Generating itinerary..."):
            itinerary = generate_itinerary(destination, days, nights, interests)
            st.write(itinerary)