import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="HandyFinder", page_icon="🛠️")

# 2. Add your Yelp API Key here (or use Streamlit Secrets)
YELP_API_KEY = "YOUR_YELP_API_KEY_HERE"

def get_handymen(location):
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {
        "term": "handyman",
        "location": location,
        "sort_by": "rating",  # Ensures top rated come first
        "limit": 5
    }
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# 3. Simple UI
st.title("🛠️ Top Rated Handymen")
st.write("Find the best-reviewed help in your area.")

location_input = st.text_input("Enter City or Zip Code (e.g., Weston, FL):", "")

if location_input:
    with st.spinner('Searching the neighborhood...'):
        data = get_handymen(location_input)
        
        if "businesses" in data and len(data["businesses"]) > 0:
            for biz in data["businesses"]:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(biz["image_url"], width=100)
                with col2:
                    st.subheader(f"[{biz['name']}]({biz['url']})")
                    st.write(f"⭐ {biz['rating']} ({biz['review_count']} reviews)")
                    st.write(f"📞 {biz['display_phone']}")
        else:
            st.error("No handymen found. Try a different zip code!")