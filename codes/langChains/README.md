# LangChains 예제 코드

이 디렉토리에는 LangChain을 활용한 두 가지 예제 코드가 포함되어 있습니다.

## 파일 설명

### 1. toyproject_gemini_rag.py

Gemini API를 사용한 RAG(Retrieval-Augmented Generation) 구현 예제입니다.

**주요 기능:**
- Google Gemini API 인증 및 모델 사용
- PDF 문서 로딩 및 청크 분할
- HuggingFace 임베딩을 사용한 벡터 저장소 생성
- RAG 체인을 통한 질의응답 시스템 구현

**실행 방법:**
```bash
# 필요 패키지 설치
pip install langchain-google-genai google-generativeai tiktoken pypdf sentence_transformers chromadb langchain-community

# 실행
python toyproject_gemini_rag.py
```

> 참고: Google API 키가 필요하며, PDF 파일 경로를 적절히 설정해야 합니다.

### 2. toyproject_agent_prompttomakeSQL.py

자연어로 작성된 쿼리를 SQL로 변환하는 에이전트 구현 예제입니다.

**주요 기능:**
- SQLite 데이터베이스 연결 및 조회
- OpenAI API를 활용한 SQL 에이전트 생성
- Few-shot 학습 예제를 통한 SQL 쿼리 생성 개선
- 콜백 핸들러를 통한 에이전트 실행 과정 모니터링

**실행 방법:**
```bash
# 필요 패키지 설치
pip install langchain langchain-openai langchain-community faiss-cpu sqlite3

# 환경 변수 설정
export OPENAI_API_KEY="your-api-key-here"

# 실행
python toyproject_agent_prompttomakeSQL.py
```

> 참고: OpenAI API 키가 필요하며, SQLite 데이터베이스 파일 경로를 적절히 설정해야 합니다. 