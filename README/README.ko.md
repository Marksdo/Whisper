# 🎶 Whisper Mate – 로컬 퍼스트 자막·음성 워크스페이스
[Deutsch](README.de.md) · [English](../README.md) · [Spanish](README.es.md) · [Finnish](README.fi.md) · [French](README.fr.md) · [Italian](README.it.md) · [Indonesian](README.id.md) · [언어](README.ko.md) · [日本語](README.ja.md) · [简体中文](README.zh_cn.md) · [繁体中文](README.zh_tw.md) · [Norwegian](README.nb.md) · [Dutch](README.nl.md) · [Polish](README.pl.md) · [Portuguese](README.pt_PT.md) · [Swedish](README.sv.md) · [ภาษาไทย](README.th.md) · [Turkish](README.tr.md) · [Ukrainian](README.uk.md) · [Vietnamese](README.vi.md)

| ![Whisper Mate icon](../images/appicon-128x128.png) | Whisper Mate는 오디오와 비디오를 세련된 자막, 번역, 내보내기로 변환하며 모든 처리를 Mac에서 로컬로 수행해 프로젝트의 프라이버시를 지킵니다. macOS App Store에서 다운로드: [Whisper Mate](https://apps.apple.com/us/app/id6450404233) |
| --- | --- |

## 🔑 핵심 장점
- **설계 단계부터 프라이버시**: 전사, 번역, 내보내기가 100% 로컬에서 진행되어 민감한 미디어가 Mac을 떠나지 않습니다.
- **최적의 엔진 선택**: FluidAudio, whisper.cpp, WhisperKit, Apple 온디바이스 AI(macOS 26+), Kokoro English Speech Synthesis를 사용 사례에 맞게 전환합니다.
- **라이브 제작 워크플로우**: 녹음, 자막, 번역, 플로팅 미리보기, 자동화 체인을 실시간으로 모니터링합니다.
- **보는 대로 결과**: 내장 플레이어에서 자막 서체, 크기, 행간을 즉시 확인합니다.
- **확장 가능한 도구**: 템플릿, JavaScript 프로세서, 사전, 정규식 변환을 조합해 복잡한 자막 정리를 자동화합니다.
- **자막 전용 데스크**: 편집, 검수, 일괄 내보내기/가져오기, Final Cut Pro·QuickLook·GIF·MKV 파이프라인을 한곳에서 관리합니다.

## 🔥 주요 기능
- **배치 및 라이브 전사**: 대용량 자산, 라이브 마이크 캡처, 앱 오디오 라우팅, 동시 번역을 처리합니다.
- **자막·번역 에디터**: 병합, 분할, 타이밍 조정, Quick-Cut, 대량 치환, 키보드 중심 제어를 제공합니다.
- **다국어 번역**: DeepL, Apple Translate, GPT, Gemini, DeepSeek, OpenRouter 또는 Ollama 호환 로컬 LLM을 활용합니다.
- **자동화 플레이북**: 작업 완료 시 스크립트, 내보내기, 요약, 알림을 자동으로 실행합니다.
- **입출력 에코시스템**: SRT, VTT, ASS, FCPXML, GIF, PDF, DOCX, MKV, 오디오 클립 등과 매끄럽게 연동합니다.
- **비주얼 도구**: 플로팅 창, 가변 폰트·행간, 텍스트 전용/분할 뷰 모드를 즉시 전환합니다.
- **LLM 협업**: Apple 온디바이스 모델, Ollama, 원격 LLM을 연결해 자막 다듬기, 요약, 스크립트 수정에 활용합니다.
- **프로젝트 제어 & 스냅샷**: 프로젝트를 그룹화하고 대기열 우선순위를 조정하며 되돌릴 수 있는 스냅샷을 저장, 안전하게 보관하고 원격 폴더를 모니터링합니다.
- **비디오 후반 작업**: Quick Cut 파형 편집, 챕터, 장면 키프레임, GIF/MP4 내보내기, 하드 서브 인코딩을 지원합니다.

## 🚀 활용 사례
- 영화, 팟캐스트, 인터뷰 자막 제작, 번역, 보이스오버.
- 회의, 수업, 라이브 스트림용 실시간 메모와 요약.
- 자동화로 다국어 배치를 처리하는 미디어 팀.
- 스냅샷으로 음성 코퍼스를 아카이브하고 주석을 다는 학술/연구팀.
- 긴 영상을 쇼츠, GIF, 내레이션 클립으로 재가공하는 마케팅·소셜 팀.
- 고품질 감사 로그가 필요한 고객 지원, 영업, 법률 녹음의 컴플라이언스 충족.

## 📋 고급 리소스 가이드
- [FAQ & 팁](../docs/faq-and-tips.md)
- [사용자 정의 내보내기 템플릿](../docs/custom-export-templates.md)
- [LLM 통합(요약, QA, 수정)](../docs/llm-integrations.md)
- [자막 삽입 영상 내보내기](../docs/exporting-subtitled-videos.md)
- [디렉터리 모니터링 & 자동 전사](../docs/directory-monitoring.md)
- [실시간 전사](../docs/real-time-transcription.md)
- [세그먼트 재전사](../docs/segment-retranscription.md)
- [프리셋 관리](../docs/preset-management.md)
- [사전 워크플로우](../docs/dictionary-workflows.md)
- [스냅샷 모범 사례](../docs/snapshot-best-practices.md)
- [멀티 프로젝트 관리 & 검색](../docs/multi-project-management.md)
- [완전 자동화 워크플로우 예시](../docs/fully-automated-workflows.md)

## 💬 지원 & 피드백
- 앱 내 **About** 메뉴에서 피드백을 보내거나 GitHub에 이슈를 등록해 함께 진행 상황을 추적해주세요.

## 🏞️ 앱 화면
![Projects](../images/v9-whispermate_main.webp)
![Subtitle Editor](../images/v9-sub-editor.webp)
![Live Transcription](../images/v9-live-video-transcription.webp)
![Embed Video Previewer](../images/v9-floating.webp)
![Re-transcription](../images/v9-retranscription.webp)
![Custom Export Template](../images/v9-custom-template.webp)

## 🔋 뛰어난 오픈소스 프로젝트에 감사드립니다

- [![GitHub stars](https://img.shields.io/github/stars/FluidInference/FluidAudio.svg?style=social&label=Star%20FluidAudio)](https://github.com/FluidInference/FluidAudio)
- [![GitHub stars](https://img.shields.io/github/stars/argmaxinc/WhisperKit.svg?style=social&label=Star%20WhisperKit)](https://github.com/argmaxinc/WhisperKit)
- [![GitHub stars](https://img.shields.io/github/stars/ggerganov/whisper.cpp.svg?style=social&label=Star%20whisper.cpp)](https://github.com/ggerganov/whisper.cpp)

<p align="center">
  <a href="https://fluidinference.com"><img src="https://assets.inference.plus/fi-badge.png" alt="Powered by Fluid Inference" height="80"></a>
  <a href="https://github.com/ggerganov/whisper.cpp" style="margin-left: 16px;"><img src="https://user-images.githubusercontent.com/1991296/235238348-05d0f6a4-da44-4900-a1de-d0707e75b763.jpeg" alt="Powered by whisper.cpp" height="80"></a>
  <a href="https://github.com/argmaxinc/WhisperKit" style="margin-left: 16px;"><img src="../images/vender/whisperkit.png" alt="Powered by WhisperKit" height="80"></a>
</p>
