# agent.py
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from datetime import datetime, timedelta
from typing import List, Dict, Any

def search_recent_news(domain: str, days: int = 3, language: str = "ko") -> dict:
    """
    특정 도메인(산업)의 최근 뉴스를 검색합니다.
    
    Args:
        domain (str): 관심 산업/도메인 (예: "반도체", "바이오", "전기차")
        days (int): 검색할 최근 일수. 기본값: 3
        language (str): 뉴스 언어. 기본값: "ko"
    
    Returns:
        dict: 검색된 뉴스 목록과 메타데이터
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    try:
        news_data = {
            "status": "success",
            "domain": domain,
            "search_period": f"{start_date.strftime('%Y-%m-%d')} ~ {end_date.strftime('%Y-%m-%d')}",
            "articles": [
                {
                    "title": f"{domain} 산업 주요 동향 발표",
                    "summary": f"{domain} 관련 기업들의 최신 실적과 향후 전망이 공개되었습니다. 주요 기업들의 투자 계획과 시장 점유율 변화가 주목받고 있습니다.",
                    "url": "https://example.com/news1",
                    "published_date": end_date.strftime('%Y-%m-%d'),
                    "source": "경제신문",
                    "relevance_score": 0.95
                },
                {
                    "title": f"{domain} 관련 정부 정책 발표",
                    "summary": f"정부가 {domain} 산업 육성을 위한 새로운 지원책을 발표했습니다. 세제 혜택과 연구개발 지원 확대가 포함되어 있습니다.",
                    "url": "https://example.com/news2",
                    "published_date": (end_date - timedelta(days=1)).strftime('%Y-%m-%d'),
                    "source": "투자일보",
                    "relevance_score": 0.88
                },
                {
                    "title": f"글로벌 {domain} 시장 전망",
                    "summary": f"해외 시장에서 {domain} 수요가 급증하고 있어 국내 관련 기업들의 수출 확대가 기대됩니다.",
                    "url": "https://example.com/news3",
                    "published_date": (end_date - timedelta(days=2)).strftime('%Y-%m-%d'),
                    "source": "산업뉴스",
                    "relevance_score": 0.82
                }
            ],
            "total_count": 3
        }
        return news_data
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"뉴스 검색 중 오류가 발생했습니다: {str(e)}",
            "domain": domain
        }

def get_stock_related_keywords(domain: str) -> dict:
    """
    도메인에 관련된 주식/투자 키워드를 반환합니다.
    
    Args:
        domain (str): 산업 도메인
        
    Returns:
        dict: 관련 키워드와 주요 기업 목록
    """
    domain_keywords = {
        "반도체": {
            "keywords": ["반도체", "메모리", "시스템반도체", "파운드리", "DRAM", "낸드플래시", "AI칩", "HBM"],
            "major_companies": ["삼성전자", "SK하이닉스", "TSMC", "인텔", "엔비디아", "AMD"],
            "investment_themes": ["AI반도체", "메모리 슈퍼사이클", "차량용반도체", "서버용 메모리"]
        },
        "바이오": {
            "keywords": ["바이오", "제약", "의료기기", "임상시험", "신약개발", "바이오시밀러"],
            "major_companies": ["셀트리온", "삼성바이오로직스", "유한양행", "대웅제약", "화이자", "모더나"],
            "investment_themes": ["mRNA 백신", "항체치료제", "정밀의료", "디지털헬스케어"]
        },
        "전기차": {
            "keywords": ["전기차", "EV", "배터리", "자율주행", "충전인프라", "전고체배터리"],
            "major_companies": ["테슬라", "현대차", "LG에너지솔루션", "CATL", "BYD", "폭스바겐"],
            "investment_themes": ["고체배터리", "완전자율주행", "V2G", "초고속충전"]
        },
        "인공지능": {
            "keywords": ["AI", "인공지능", "머신러닝", "딥러닝", "생성AI", "챗GPT"],
            "major_companies": ["오픈AI", "구글", "마이크로소프트", "네이버", "카카오", "엔비디아"],
            "investment_themes": ["생성AI", "AI반도체", "자율주행", "AI서비스"]
        }
    }
    
    if domain in domain_keywords:
        return {
            "status": "success",
            "domain": domain,
            **domain_keywords[domain]
        }
    else:
        return {
            "status": "success", 
            "domain": domain,
            "keywords": [domain],
            "major_companies": [],
            "investment_themes": [],
            "message": "일반적인 키워드로 검색합니다"
        }

def analyze_investment_impact(news_articles: List[dict]) -> dict:
    """
    뉴스의 투자 관점에서의 영향도를 분석합니다.
    
    Args:
        news_articles (List[dict]): 뉴스 기사 목록
        
    Returns:
        dict: 투자 영향도 분석 결과
    """
    if not news_articles:
        return {"status": "error", "message": "분석할 뉴스가 없습니다"}
    
    positive_keywords = [
        "상승", "증가", "성장", "호실적", "수주", "투자확대", "신고가", "돌파",
        "확대", "개발", "성공", "승인", "계약", "협력", "파트너십", "혁신"
    ]
    negative_keywords = [
        "하락", "감소", "적자", "리스크", "규제", "공급부족", "지연", "취소",
        "축소", "철회", "실패", "손실", "우려", "불안", "제재", "분쟁"
    ]
    
    analysis_result = {
        "total_articles": len(news_articles),
        "sentiment_analysis": {"positive": 0, "negative": 0, "neutral": 0},
        "key_themes": [],
        "investment_recommendation": "중립",
        "confidence_score": 0.0
    }
    
    theme_keywords = {}
    
    for news in news_articles:
        title_summary = f"{news.get('title', '')} {news.get('summary', '')}"
        
        positive_count = sum(1 for keyword in positive_keywords if keyword in title_summary)
        negative_count = sum(1 for keyword in negative_keywords if keyword in title_summary)
        
        if positive_count > negative_count:
            analysis_result["sentiment_analysis"]["positive"] += 1
        elif negative_count > positive_count:
            analysis_result["sentiment_analysis"]["negative"] += 1
        else:
            analysis_result["sentiment_analysis"]["neutral"] += 1
        
        for word in title_summary.split():
            if len(word) > 2:
                theme_keywords[word] = theme_keywords.get(word, 0) + 1
    
    analysis_result["key_themes"] = sorted(theme_keywords.items(), key=lambda x: x[1], reverse=True)[:5]
    
    pos_count = analysis_result["sentiment_analysis"]["positive"]
    neg_count = analysis_result["sentiment_analysis"]["negative"]
    total_count = analysis_result["total_articles"]
    
    if pos_count > neg_count:
        analysis_result["investment_recommendation"] = "긍정적"
        analysis_result["confidence_score"] = round(pos_count / total_count, 2)
    elif neg_count > pos_count:
        analysis_result["investment_recommendation"] = "부정적"
        analysis_result["confidence_score"] = round(neg_count / total_count, 2)
    else:
        analysis_result["investment_recommendation"] = "중립"
        analysis_result["confidence_score"] = 0.5
    
    analysis_result["status"] = "success"
    return analysis_result

# 전문 뉴스 요약 에이전트 - instruction (단수형) 사용
news_summarizer_agent = Agent(
    name="news_summarizer",
    model="gemini-2.0-flash",
    instruction="투자자를 위한 뉴스 요약 전문가입니다. 각 뉴스 기사를 제목, 투자 영향도, 핵심 내용, 관련 기업, 발표일 형식으로 간결하게 요약합니다."
)

# 메인 투자 뉴스 에이전트 - instruction (단수형) 사용
investment_news_agent = Agent(
    name="investment_news_agent",
    model="gemini-2.0-flash",
    instruction="""당신은 주식투자자를 위한 전문 뉴스 분석 에이전트입니다. 
    사용자가 관심있는 산업의 최근 3일 뉴스를 검색하고, 투자 관점에서 분석하여 실용적인 인사이트를 제공합니다.
    작업 순서: 1) 도메인 키워드 확인 2) 뉴스 검색 3) 영향도 분석 4) 요약 제공
    모든 투자 결정은 개인의 판단과 책임임을 항상 명시하세요.""",
    tools=[
        search_recent_news,
        get_stock_related_keywords,
        analyze_investment_impact,
        AgentTool(agent=news_summarizer_agent, skip_summarization=True)
    ]
)

# ADK에서 요구하는 root_agent 설정
root_agent = investment_news_agent
