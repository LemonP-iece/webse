import streamlit as st
import requests
from bs4 import BeautifulSoup

# 모바일 화면 기본 설정 (유튜브 앱 느낌의 어두운 테마 설정 가능)
st.set_page_config(page_title="통합 검색 포털", page_icon="🔍", layout="centered")

# 사용자 지정 10개 사이트 리스트 (예시)
TARGET_SITES = [
    {"name": "네이버", "url": "https://www.naver.com"},
    {"name": "유튜브", "url": "https://www.youtube.com"},
    {"name": "다음", "url": "https://www.daum.net"},
    # ... 자주 가시는 사이트 10개 등록
]

# 커스텀 CSS: 모바일 유튜브 카드 스타일링
st.markdown("""
    <style>
    .search-card {
        background-color: #1e1e1e;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 16px;
        color: white;
    }
    .site-badge {
        background-color: #FF0000;
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 통합 모바일 검색")

# 상단 검색창
keyword = st.text_input("", placeholder="검색어를 입력하세요...", key="search_input")

# 크롤링/검색 로직 (실제 웹 스크래핑 연동 파트)
def fetch_search_results(query):
    results = []
    # 예시 데이터 (실제 서비스 구현 시 BeautifulSoup/API로 데이터 수집)
    # 각 사이트별 og:image(썸네일), og:title, og:description 파싱
    for i in range(1, 6):
        results.append({
            "site": "유튜브" if i % 2 == 0 else "네이버 뉴스",
            "title": f"'{query}' 관련 검색 결과 영상/기사 {i}",
            "summary": f"이 콘텐츠는 {query}에 대한 핵심 요약 내용과 세부 정보를 담고 있습니다.",
            "thumbnail": f"https://picsum.photos/400/225?random={i}", # 예시 썸네일 (16:9 비율)
            "link": "https://youtube.com"
        })
    return results

if keyword:
    st.write(f"**'{keyword}'** 검색 결과")
    data = fetch_search_results(keyword)
    
    # 모바일 환경에 최적화된 1열 카드 피드 (유튜브 모바일 UI)
    for item in data:
        with st.container():
            # 1. 썸네일 이미지 (16:9 비율)
            st.image(item["thumbnail"], use_column_width=True)
            
            # 2. 사이트 태그 및 제목
            st.markdown(f"<span class='site-badge'>{item['site']}</span> **{item['title']}**", unsafe_allow_html=True)
            
            # 3. 본문 요약 내용
            st.caption(item["summary"])
            
            # 4. 바로가기 버튼
            st.link_button("보러 가기", item["link"])
            st.divider()
