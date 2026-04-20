import streamlit as st
import streamlit.components.v1 as components
import random
import json

# --- 📝 데이터 세팅 (전체 데이터 동일) ---
RAW_DATA = """
데드크로스: 주식시장에서 단기 이동평균선이 장기 이동평균선을 아래로 뚫고 내려가는 현상
리세션: 경기 하강 과정에서 발생하는 일시적인 경기 후퇴
그린워싱: 실제로는 친환경적이지 않지만 마치 친환경적인 것처럼 홍보하는 위장 환경주의
스테그플레이션: 경기 불황 속에서 물가가 계속 오르는 현상
합성 소비자: 실제 사람의 행동 선호 의사결정 패턴과 심리적 동기를 모사하기 위해 인공지능(AI)이 생성해 낸 가상의 소비자 객체 혹은 집단을 의미
키네틱 리스크: 미사일 공격이나 드론 공습처럼 물리적인 타격에 의해 발생하는 경제적 위험을 뜻함 
빅맥 트레이드: 미국 중간선거를 앞두고 정책 변화 기대와 정치 이벤트 리스크를 반영해 투자 전력을 세우는 시장 접근법
프라이스 디코딩: 소비자들이 제품 가격을 액면 그대로 받아들이지 않고 원가, 유통 마진, 브랜드 가치 등으로 '분해'해 합리성을 분석하는 트렌드
HBM4E: 삼성전자가 실물 칩을 최초로 공개한 7세대 고대역폭 메모리 
팩맨 방어: 적대적 인수 위기에 처한 타깃 기업이 역으로 공격 기업의 주식을 사들여 경영권을 위협하는 공격적인 방어 전략
터보퀀트: '벡터 검색 엔진'에서 발생하는 메모리 병목 현상을 해결해 AI 효율성을 획기적으로 개선하는 데이터 압축 알고리즘 
타코(TACO): 시장 충격을 유발하는 강경 정책을 내놓았다가 금융시장 압박이 커지면 물러서는 트럼프 대통령의 반복된 정책 패턴 
나초(NACHO): 호르무즈 해협 개방에 대한 실질적 변화가 없다는 뜻의 줄임말
제로 클릭: 검색 없이 인공지능에 물어보면 바로 답을 얻는 환경
부동산 감독원: 집값 띄우기 및 탈세 등 부동산 시장 내 불법 행위를 전문적으로 감시하고 이를 수사하는 권한을 지닌 감독기구
오픈클로: 인공지능이 사용자의 컴퓨터 환경에 직접 접근해 실제 행동을 수행하도록 설계된 이른바 'AI 에이전트' 기술
EPIC FURY(장대한 분노): 2026년 2월 28일 미국이 이란을 상대로 개시한 군사작전의 공식 명칭
초크 포인트: 세계 경제의 급소라는 의미이며 글로벌 해상운송의 핵심 길목인 해협과 운하를 뜻함
아야톨라 알리 하메네이: 1989년부터 2026년 2월까지 이란을 통치한 최고지도자
이란 최고지도자: 대통령보다 상위 권련을 갖는 국가 최고 권력자로, 군 통수권과 사법부, 국영방송, 혁명수비대 등에 대한 최종 통제권을 행사함
호르무즈 해협: 페르시아만과 오만만을 연결하는 좁은 해상통로이며 세계 원유 해상 수송의 약 20~30%가 지나가는 에너지 요충지
포지 이니셔티브: 미국 트럼프 행정부가 주도해 핵심광물 공급망을 다변화하기 위해 결성한 무역블록
경자유전: 농사를 짓는 사람만이 농지를 소유할 수 있다는 원칙 (대한민국 헌법 제121조)
수니콘: 곧 유니콘이 될 가능성이 있는 비상장 스타트업
메모리플레이션: 메모리 반도체 가격 상승이 IT 완제품 가격으로 전이되는 현상
퍼플칼라: 근무시간과 장소를 유연하게 선택할 수 있는 직업군
팍스 실리카: 미국 워싱턴에서 출범한 미국 주도의 다자간 경제안보 협의체로, AI와 반도체 산업의 핵심 소재 공급망을 매개로 구축된 기술 동맹 체제를 뜻함
대미투자특별법 특별위원회: 대비 관세협상의 후속 조치를 다루는 '한미 전략적 투자 관리를 위한 특별법안' 처리를 논의하기 위해 여야가 합의해 만든 특위
그리드플레이션: 대기업들이 고물가 분위기를 틈타 상품·서비스 가격을 과도하게 올려 물가상승을 부채질하는 현상
브레인 포그: 머리에 안개가 낀 것처럼 멍한 느낌이 지속돼 생각과 표현을 분명하지 못하는 상태
먼로주의: 미국의 제5대 대통령 먼로가 밝힌 비동맹, 비식민, 불간섭을 내용으로 하는 고립주의 외교정책의 원칙
커뮤니티 커머스: 특정 관심사나 취향을 공유하는 사람들이 모인 커뮤니티를 기반으로 상품 정보와 경험을 공유하며 자연스럽게 구매로 연결되는 형태의 모델
몰트북: 2026년 1월 말 공개된 인공지능 에이전트 전용 사회관계망서비스 
컴퓨트 달러: 쇠락하는 페트로달러를 대체해 미국의 금융, 통화 패권을 유지하기 위해 제안된 기축통화 세스템
에이전틱 커머스: 사용자의 목적과 제약을 반영한 인공지능 에이전트가 상품 탐색부터 비교, 추천, 결제와 주문 실행까지 전 과정을 대행하는 방식
양말 인형: 스스로의 의지 없이 배후 인물의 지시대로 움직이는 대리인
VASP: 가상자산 사업자
투자소득수지: 한 나라의 거주자가 해외에 투자해 얻은 이자와 배당 등 투자 수익에서 외국인 투자자가 국내 자산에 투자해 취득한 소득을 차감한 값
바이브 코딩: 프로그래밍 언어를 완벽하게 구사하는 대신 자연어로 소프트웨어의 의도와 느낌을 전달해 코드를 생성하는 방식
튜나(TUNA): 도널드 트럼프 미국 태동령은 보통 발표를 뒤집는다는 뜻의 줄임말
납치광고: 이용자가 원래 보려던 콘텐츠와 무관하게 광고 페이지나 특정 플랫폼으로 강제 이동시키고, 쉽게 벗어나지 못하도록 설계된 온라인 광고 행태
아인슈텔룽 효과: 과거의 성공적인 해결 방식에 익숙해져서 더 나은 새로운 해결책을 찾지 못하는 현상
나프타: 플라스틱 등 석유화학의 원료가 되는 조제 휘발유로, 내연기관이나 도시가스의 연료로 사용됨
서킷 브레이커: 주식시장에서 주가지수가 일정 수준 이상 급락할 경우 공황 매매를 방지하고 투자자에게 냉정한 판단 시간을 제공하기 위해 일정 시간 동안 모든 매매 거래를 일시적으로 중단하는 시장 안정 장치
사이드카: 선물시장의 급등락이 현물시장에 과도하게 파급되는 것을 막기 위해 선물 가격이 기준가 대비 ±5% 이상인 상황이 1분간 지속하는 경우 발동되는 안전 장치
MASGA: 2025년 7월 한국 정부가 미국과의 통상 협상을 타결하는 데 결정적인 역할을 한 전략적 구상
AI 버블론: AI에 대한 기대가 과도해 인공지능 관련 주식이 과대평가될 수 있다는 우려를 뜻하는 표현
전동화: 자동차의 동력 기관을 전기로 바꾸는 것
노벨상: 매년 10월에 수상하며 생리의학, 물리학, 화학, 문학, 평화,경제학 분야에 걸쳐 수상함
ICE(United States Immigration and Customs Enforcement): 미국 이민세관집행국
NATO: 북대서양 조약 기구
조세이 탄광: 야마구치현에 있는 해저탄광, 일제 강점기 당시 수몰 사고로 조선인 136명이 사망
패트리어트 미사일: 지대공, 전술탄도미사일 요격 시스템
5극 3특: 수도권 일득 체제를 완화하고 국가균형성장을 추진하기 위해 대한민국을 5개 초광역권과 3개의 특별자치권으로 나눠 성장엔진을 육성하는 정책 
잔디깎기 전략: 작은 규모의 충돌이나 도발에는 지속적으로 대응하는 대신 큰 규모의 전쟁은 피하며 안보를 유지하는 전략
사데크의 약속 4: 2026년 미국과 이란의 전쟁 중 이란 혁명수비대의 반격 작전
SMR: 소형 모듈 원전으로 기존 대비 작은 용량과 모듈식 설계를 채택한 원자로
케빈 워시: 차기 미국 연방준비제도이사회 의장  
신현송: 차기 한국은행 총재 후보 
슈링크플레이션: 기업이 제품의 표시가격은 유지하면서 중량, 용량, 개수 등 실질 제공량을 줄여 결과적으로 단위당 가격을 올리는 전략 
검색증강생성: 대규모 언어모델에 정보검색기능을 결합한 기술
빅블러: 변화의 속도가 빨라지면서 기존에 존재하던 것들의 경계가 뒤섞이는 현상
HBM: 고대역폭 메모리
3차 상법개정안: 기업이 자사주를 원칙적으로 소각하도록 규정한 법안 (자사주 소각 의무화) 
온 디바이스 AI: 클라우드 서버에 의존하지 않고 기기에 탑재돼 직접 서비스를 제공하는 AI
토빈세: 국제 투기자본의 급격한 유출입으로 인한 금융 위기를 방지하기 위해 단기성 외환거래에 부과하는 세금
"""

EXTERNAL_DISTRACTORS = ["유니콘 기업", "데카콘 기업", "그레이 스완", "화이트 스완", "그린플레이션", "스테이케이션", "긱 워커", "플랫폼 노동", "ESG 경영", "RE100", "탄소국경세", "오픈 이노베이션", "데이터 3법", "마이데이터", "메타버스", "중대재해처벌법", "가상화폐", "스테이블 코인", "CBDC", "NFT", "브레드플레이션", "슈링크플레이션", "스킴플레이션", "밀크플레이션", "런치플레이션", "공매도", "서킷브레이커", "사이드카", "윈도우 드레싱", "어닝 쇼크", "기업공개(IPO)", "스팩(SPAC)", "엔젤 투자", "크라우드 펀딩", "벤처 캐피털", "기준금리", "빅스텝", "자이언트스텝", "베이비스텝", "양적긴축(QT)", "테이퍼 탠트럼", "역모기지론", "안전자산", "위험자산", "기축통화", "환율 조작국", "스와프 포인트", "통화 스와프", "외환보유고", "디폴트"]

def parse_data(raw_text):
    data = []
    for line in raw_text.strip().split('\n'):
        if ':' in line:
            word, definition = line.split(':', 1)
            data.append({"word": word.strip(), "definition": definition.strip()})
    return data

QUIZ_DATA = parse_data(RAW_DATA)

st.set_page_config(page_title="시사상식", layout="centered")

# --- 🎨 컴팩트 스타일 (여백 및 크기 최적화) ---
st.markdown("""
    <style>
    /* 전체 여백 줄이기 */
    .main .block-container { padding-top: 1rem; padding-bottom: 1rem; max-width: 95%; }
    .title-separator { border-top: 1px solid #eee; margin-top: 5px; margin-bottom: 15px; }
    h1 { font-size: 1.5rem !important; margin-bottom: 10px; }
    
    /* 탭 메뉴 슬림화 */
    .stTabs [data-baseweb="tab-list"] { gap: 5px; }
    .stTabs [data-baseweb="tab"] {
        height: 35px; font-size: 14px !important;
        border-radius: 20px !important; padding: 0px 15px !important;
    }
    
    /* 단답형/객관식 폰트 조절 */
    .stMarkdown p, .stRadio label { font-size: 14.5px !important; }
    div[data-testid="stForm"] { padding: 10px; border-radius: 10px; }
    
    .next-btn-container { display: flex; justify-content: center; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("시사상식 대비")
st.markdown('<div class="title-separator"></div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["암기", "단답", "객관"])

# --- 탭 1: 암기 모드 (컴팩트 검색창) ---
with tab1:
    json_data = json.dumps(QUIZ_DATA, ensure_ascii=False)
    search_html = f"""
    <div id="search-container" style="font-family: sans-serif; width: 100%; box-sizing: border-box;">
        <input type="text" id="search-input" placeholder="단어 검색" 
            style="width: 100%; padding: 10px 15px; border-radius: 20px; border: 1px solid #eee; 
            outline: none; font-size: 14px; background-color: #f9f9f9; margin-bottom: 15px; box-sizing: border-box;">
        <div id="results-container"></div>
    </div>
    <script>
        const data = {json_data};
        const input = document.getElementById('search-input');
        const container = document.getElementById('results-container');
        function displayResults(filter = "") {{
            container.innerHTML = "";
            const filtered = data.filter(item => item.word.toLowerCase().includes(filter.toLowerCase()));
            filtered.forEach(item => {{
                const details = document.createElement('details');
                details.style.marginBottom = "8px";
                details.style.border = "1px solid #f9f9f9";
                details.style.borderRadius = "8px";
                details.style.padding = "10px";
                const summary = document.createElement('summary');
                summary.innerHTML = "<span style='font-size: 8px; margin-right: 8px;'>●</span>" + item.word;
                summary.style.fontSize = "14px";
                summary.style.cursor = "pointer";
                summary.style.listStyle = "none";
                const p = document.createElement('p');
                p.innerText = item.definition;
                p.style.marginTop = "10px"; p.style.color = "#666"; p.style.fontSize = "13px"; p.style.lineHeight = "1.5";
                details.appendChild(summary); details.appendChild(p); container.appendChild(details);
            }});
        }}
        displayResults();
        input.addEventListener('input', (e) => displayResults(e.target.value));
    </script>
    """
    components.html(search_html, height=550, scrolling=True)

# --- 탭 2: 단답형 ---
with tab2:
    if 'current_q' not in st.session_state: st.session_state.current_q = random.choice(QUIZ_DATA)
    if 'input_key' not in st.session_state: st.session_state.input_key = 0
    q = st.session_state.current_q
    st.markdown(f"**Q.** {q['definition']}")
    with st.form(key=f"short_form_{st.session_state.input_key}"):
        col_input, col_check = st.columns([2, 1])
        with col_input: ans = st.text_input("정답", placeholder="입력", label_visibility="collapsed")
        with col_check: submit = st.form_submit_button("확인")
        if submit:
            if ans.replace(" ", "").lower() == q['word'].replace(" ", "").lower(): st.success("정답")
            elif ans != "": st.error(f"정답: {q['word']}")
    st.markdown('<div class="next-btn-container">', unsafe_allow_html=True)
    if st.button("다음 문제"):
        st.session_state.current_q = random.choice(QUIZ_DATA)
        st.session_state.input_key += 1
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- 탭 3: 객관식 ---
with tab3:
    if 'quiz_set' not in st.session_state:
        selected = random.sample(QUIZ_DATA, min(15, len(QUIZ_DATA)))
        st.session_state.quiz_set = []
        for q_item in selected:
            internal_words = [d['word'] for d in QUIZ_DATA if d['word'] != q_item['word']]
            full_distractor_pool = list(set(internal_words + EXTERNAL_DISTRACTORS))
            distractors = random.sample(full_distractor_pool, 3)
            opts = distractors + [q_item['word']]
            random.shuffle(opts)
            st.session_state.quiz_set.append({"q": q_item, "opts": opts})
        st.session_state.user_ans = [None] * len(selected)
        st.session_state.done = False

    for i, item in enumerate(st.session_state.quiz_set):
        st.markdown(f"**{i+1}. {item['q']['definition']}**")
        st.session_state.user_ans[i] = st.radio(f"c_{i}", item['opts'], index=None if st.session_state.user_ans[i] is None else item['opts'].index(st.session_state.user_ans[i]), key=f"r_{i}", label_visibility="collapsed", disabled=st.session_state.done)
        if st.session_state.done:
            if st.session_state.user_ans[i] == item['q']['word']: st.success(f"정답: {item['q']['word']}")
            else: st.error(f"오답. (정답: {item['q']['word']})")
        st.write("---")

    if not st.session_state.done:
        if st.button("최종 제출 및 채점"):
            st.session_state.done = True
            st.rerun()
    else:
        if st.button("새로운 문제 풀기"):
            del st.session_state.quiz_set
            st.rerun()
