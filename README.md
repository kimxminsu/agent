# 📈 투자 뉴스 분석 에이전트

Google Agent Development Kit(ADK)로 구축된 지능형 투자 뉴스 분석 시스템으로, 주식투자자가 산업 동향을 파악하고 데이터 기반의 투자 의사결정을 할 수 있도록 돕습니다.

## 🎯 주요 기능

- **📰 실시간 뉴스 검색**: 여러 산업의 최근 3일 뉴스를 실시간으로 수집
- **🔍 산업별 전문 분석**: 반도체, 바이오, 전기차, AI 등 주요 섹터 커버
- **📊 투자 영향도 분석**: 감정 분석을 통한 긍정적/부정적/중립적 영향도 평가
- **🏢 기업 및 테마 인사이트**: 관련 기업과 투자 테마 정보 제공
- **🤖 멀티 에이전트 아키텍처**: 요약 및 분석 전문 에이전트 활용
- **🚀 REST API**: 외부 애플리케이션과 쉬운 연동

## 🛠️ 기술 스택

- **프레임워크**: Google Agent Development Kit (ADK)
- **LLM**: Gemini 2.0 Flash
- **아키텍처**: Function Tools 기반 멀티 에이전트 시스템
- **API**: FastAPI 기반 REST 엔드포인트
- **언어**: Python 3.13+

## 📋 지원 산업

- 🔧 반도체 (Semiconductor)
- 🧬 바이오테크놀로지 (Biotechnology)  
- ⚡ 전기차 (Electric Vehicle)
- 🤖 인공지능 (Artificial Intelligence)

## 🚀 빠른 시작

- **의존성 설치**
`pip install google-adk`

- **에이전트 서버 실행**
`adk api_server`

- **curl로 테스트**
```
curl -X POST http://localhost:8000/run
-H "Content-Type: application/json"
-d '{"app_name": "investment_news_agent", "user_id": "user1", "session_id": "session1", "new_message": {"role": "user", "parts": [{"text": "반도체 산업 뉴스를 알려주세요"}]}}'
```

## 🎯 활용 사례

- **개인투자자**: 빠른 산업 동향 파악 및 투자 인사이트 획득
- **금융 분석가**: 자동화된 뉴스 모니터링 및 감정 분석
- **포트폴리오 매니저**: 섹터별 주요 개발사항 업데이트
- **핀테크 애플리케이션**: API를 통한 투자 뉴스 분석 기능 통합

⚠️ **면책조항**: 본 도구는 교육 목적의 정보를 제공합니다. 모든 투자 결정은 사용자의 책임입니다.