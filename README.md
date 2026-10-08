# Alisa의 LLM 노트 (한국어 번역)

Alisa Liu의 Notion 학습 노트 「[Alisa’s book of LLMs](https://alisawuffles.notion.site/alisa-s-book-of-llms)」를 한국어로 옮긴 **비공식 번역**입니다.
모든 내용의 저작권은 원저자에게 있으며, 원저자의 요청이 있으면 즉시 내립니다.

**🔗 읽기: https://dev-jonghoonpark.github.io/book-of-llms-ko/**

> [how-ai-works](https://github.com/dev-jonghoonpark/how-ai-works) 시리즈의 일부입니다.

## 다루는 내용

| 장 | 주제 |
|---|---|
| 신경망 기초 | 다층 퍼셉트론, 활성화 함수, 기울기, 역전파, 옵티마이저, 학습률 |
| 수학적인 것들 | 정보 이론, 수치 안정성, 기초 통계, 샘플링을 통한 기울기 흐름, 이론 전산학 |
| 현대 transformer LM | 아키텍처, 구현 메모, 파라미터·활성값·FLOPs·메모리 계산, Attention, RMSNorm, SwiGLU, RoPE |
| 추론 | Batching·packing, 추측 디코딩, KV cache와 그 크기 줄이기, 샘플링 전략, Flash Attention |
| 스케일링 법칙 · GPU | |
| 기타 아키텍처 | RNN, LSTM, 상태 공간 모델 |
| 사후 학습 | 정책 기울기, PPO, RLHF, GRPO, DPO |
| 정밀도 · 병렬화 | 집합 통신 연산, 데이터·파이프라인·텐서 병렬화 |
| 멀티모달 | |

## 번역 원칙

- 수식(LaTeX)·코드·그림은 원문 그대로 두고 설명만 옮겼습니다. 원문에서 오류로 보이는 부분도 고치지 않았습니다.
- 업계에서 영어로 통용되는 용어(transformer, attention, token, KV cache 등)는 영어로 두고, 번역어가 정착된 용어는 처음 등장할 때 영어를 함께 적었습니다.
- 번역 기준 시점은 2026-10-09입니다. 원문은 계속 갱신되므로 최신 내용은 원문을 확인하세요.

## 구조

- `content.md` — 번역 본문(마크다운 + LaTeX)
- `template.html` + `build.py` → `index.html` (`python3 build.py`). [marked](https://github.com/markedjs/marked)와 [KaTeX](https://katex.org/)로 브라우저에서 렌더링합니다.
- `img/` — 원문 그림
