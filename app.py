import streamlit as st
import requests

# 🔍 작품 검색 함수
def search_artworks(query):
    url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    params = {"q": query}
    response = requests.get(url, params=params)
    return response.json().get("objectIDs", [])[:10]

# 📄 작품 상세 조회 함수
def get_artwork_details(object_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    return requests.get(url).json()

# 🎨 Streamlit 앱 UI
st.title("🎨 Explore Artworks with MET Museum API")

# 사용자 검색어 입력
query = st.text_input("Search for Artworks:")

# 검색어가 입력된 경우
if query:
    ids = search_artworks(query)
    if not ids:
        st.warning("No results found.")
    else:
        for object_id in ids:
            data = get_artwork_details(object_id)
            
            # 제목 출력
            st.subheader(data.get("title", "Untitled"))
            
            # 이미지가 있는 경우 출력
            img_url = data.get("primaryImageSmall")
            if img_url:
                st.image(img_url, width=300)
            else:
                st.info("No image available.")
            
            # 작가명, 제작년도 출력
            st.write(f"**Artist:** {data.get('artistDisplayName', 'Unknown')}")
            st.write(f"**Year:** {data.get('objectDate', 'Unknown')}")
            
            st.markdown("---")  # 구분선 추가
