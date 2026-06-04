<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>자기주도학습관리</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg: #0f172a;
      --panel: #111c33;
      --panel-2: #16243d;
      --text: #e5edf7;
      --muted: #94a3b8;
      --line: rgba(148, 163, 184, 0.22);
      --accent: #38bdf8;
      --accent-2: #22c55e;
      --danger: #fb7185;
      --warning: #facc15;
      --input: #0b1222;
      --shadow: 0 18px 50px rgba(2, 8, 23, 0.34);
      --radius: 8px;
    }

    body.light {
      --bg: #eef7fb;
      --panel: #ffffff;
      --panel-2: #f1f8fc;
      --text: #102033;
      --muted: #64748b;
      --line: rgba(15, 23, 42, 0.14);
      --input: #f8fafc;
      --shadow: 0 16px 40px rgba(15, 23, 42, 0.12);
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: var(--bg);
      color: var(--text);
      font-family: "Noto Sans KR", system-ui, sans-serif;
      transition: background 0.2s ease, color 0.2s ease;
    }

    button,
    input,
    select,
    textarea {
      font: inherit;
    }

    button {
      border: 0;
      cursor: pointer;
    }

    .app {
      display: grid;
      grid-template-columns: 248px minmax(0, 1fr);
      min-height: 100vh;
    }

    .sidebar {
      position: sticky;
      top: 0;
      height: 100vh;
      padding: 24px 18px;
      border-right: 1px solid var(--line);
      background: color-mix(in srgb, var(--panel) 84%, transparent);
      backdrop-filter: blur(18px);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 26px;
      font-family: "Outfit", sans-serif;
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 0;
    }

    .brand-mark {
      display: grid;
      place-items: center;
      width: 38px;
      height: 38px;
      border-radius: var(--radius);
      background: var(--accent);
      color: #082f49;
      font-weight: 900;
    }

    .nav {
      display: grid;
      gap: 8px;
    }

    .nav-btn {
      display: flex;
      align-items: center;
      gap: 10px;
      width: 100%;
      padding: 12px 13px;
      border-radius: var(--radius);
      background: transparent;
      color: var(--muted);
      text-align: left;
      transition: background 0.2s ease, color 0.2s ease, transform 0.2s ease;
    }

    .nav-btn:hover,
    .nav-btn:focus-visible,
    .nav-btn.active {
      background: rgba(56, 189, 248, 0.14);
      color: var(--text);
      outline: 2px solid transparent;
    }

    .nav-btn.active {
      box-shadow: inset 3px 0 0 var(--accent);
    }

    .main {
      min-width: 0;
      padding: 24px;
    }

    .topbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 22px;
    }

    h1,
    h2,
    h3 {
      margin: 0;
      font-family: "Outfit", "Noto Sans KR", sans-serif;
      letter-spacing: 0;
    }

    h1 {
      font-size: clamp(26px, 4vw, 40px);
    }

    .subtitle {
      margin: 6px 0 0;
      color: var(--muted);
      font-size: 14px;
    }

    .theme-toggle {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      min-height: 42px;
      padding: 0 14px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--panel);
      color: var(--text);
      box-shadow: var(--shadow);
      transition: border-color 0.2s ease, transform 0.2s ease, background 0.2s ease;
    }

    .theme-toggle:hover,
    .theme-toggle:focus-visible {
      border-color: var(--accent);
      transform: translateY(-1px);
      outline: 0;
    }

    .tab-panel {
      display: none;
    }

    .tab-panel.active {
      display: block;
      animation: fadeIn 0.2s ease both;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .toolbar,
    .summary-grid,
    .question-layout,
    .stats-grid {
      display: grid;
      gap: 14px;
    }

    .toolbar {
      grid-template-columns: minmax(260px, 1fr) auto;
      align-items: center;
      margin-bottom: 16px;
    }

    .date-picker {
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 0;
    }

    .icon-btn,
    .primary-btn,
    .ghost-btn,
    .danger-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-height: 42px;
      border-radius: var(--radius);
      transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease, color 0.2s ease;
    }

    .icon-btn {
      width: 42px;
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--text);
    }

    .icon-btn:hover,
    .icon-btn:focus-visible,
    .ghost-btn:hover,
    .ghost-btn:focus-visible {
      border-color: var(--accent);
      background: rgba(56, 189, 248, 0.12);
      outline: 0;
    }

    .primary-btn {
      padding: 0 16px;
      background: var(--accent);
      color: #082f49;
      font-weight: 800;
    }

    .primary-btn:hover,
    .primary-btn:focus-visible {
      background: #7dd3fc;
      transform: translateY(-1px);
      outline: 0;
    }

    .ghost-btn {
      padding: 0 14px;
      border: 1px solid var(--line);
      background: var(--panel);
      color: var(--text);
    }

    .danger-btn {
      width: 38px;
      min-height: 38px;
      border: 1px solid rgba(251, 113, 133, 0.35);
      background: rgba(251, 113, 133, 0.12);
      color: var(--danger);
    }

    .danger-btn:hover,
    .danger-btn:focus-visible {
      background: rgba(251, 113, 133, 0.22);
      outline: 0;
    }

    .date-label {
      min-width: 150px;
      color: var(--text);
      font-family: "Outfit", "Noto Sans KR", sans-serif;
      font-size: 24px;
      font-weight: 800;
      text-align: center;
    }

    .summary-grid {
      grid-template-columns: 170px repeat(2, minmax(160px, 1fr));
      margin-bottom: 18px;
    }

    .panel,
    .summary-card,
    .plan-card,
    .history-item {
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--panel);
      box-shadow: var(--shadow);
      transition: border-color 0.2s ease, background 0.2s ease, transform 0.2s ease;
    }

    .summary-card {
      padding: 16px;
    }

    .summary-label {
      color: var(--muted);
      font-size: 13px;
    }

    .summary-value {
      margin-top: 6px;
      font-family: "Outfit", sans-serif;
      font-size: 28px;
      font-weight: 800;
    }

    .donut-wrap {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 14px;
    }

    .donut {
      display: grid;
      place-items: center;
      width: 124px;
      height: 124px;
      border-radius: 50%;
      background: conic-gradient(var(--accent) calc(var(--rate) * 1%), rgba(148, 163, 184, 0.18) 0);
    }

    .donut-inner {
      display: grid;
      place-items: center;
      width: 82px;
      height: 82px;
      border-radius: 50%;
      background: var(--panel);
      font-family: "Outfit", sans-serif;
      font-size: 24px;
      font-weight: 800;
    }

    .form-panel {
      display: none;
      margin-bottom: 18px;
      padding: 16px;
    }

    .form-panel.open {
      display: block;
      animation: fadeIn 0.2s ease both;
    }

    .plan-form {
      display: grid;
      grid-template-columns: 160px minmax(220px, 1fr) 140px auto;
      gap: 10px;
      align-items: end;
    }

    label {
      display: grid;
      gap: 6px;
      color: var(--muted);
      font-size: 13px;
      font-weight: 700;
    }

    input,
    select,
    textarea {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--input);
      color: var(--text);
      transition: border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
    }

    input,
    select {
      height: 42px;
      padding: 0 12px;
    }

    textarea {
      min-height: 118px;
      padding: 12px;
      resize: vertical;
      line-height: 1.6;
    }

    input:hover,
    select:hover,
    textarea:hover {
      border-color: rgba(56, 189, 248, 0.55);
    }

    input:focus,
    select:focus,
    textarea:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.18);
      outline: 0;
    }

    .plans-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 14px;
    }

    .plan-card {
      position: relative;
      padding: 16px;
      overflow: hidden;
    }

    .plan-card.done {
      border-color: rgba(34, 197, 94, 0.55);
      background: color-mix(in srgb, var(--panel) 84%, rgba(34, 197, 94, 0.2));
    }

    .plan-head {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 12px;
    }

    .subject-pill {
      display: inline-flex;
      align-items: center;
      min-height: 30px;
      padding: 0 10px;
      border-radius: 999px;
      background: rgba(56, 189, 248, 0.14);
      color: var(--accent);
      font-size: 13px;
      font-weight: 800;
    }

    .plan-title {
      margin: 10px 0 14px;
      min-height: 44px;
      color: var(--text);
      line-height: 1.55;
      overflow-wrap: anywhere;
    }

    .spinner-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 13px;
    }

    .counter {
      display: grid;
      grid-template-columns: 38px 58px 38px;
      gap: 6px;
      align-items: center;
    }

    .counter-value {
      display: grid;
      place-items: center;
      height: 38px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--input);
      font-family: "Outfit", sans-serif;
      font-weight: 800;
    }

    .progress-meta {
      display: flex;
      justify-content: space-between;
      margin-bottom: 7px;
      color: var(--muted);
      font-size: 13px;
    }

    .progress {
      height: 10px;
      overflow: hidden;
      border-radius: 999px;
      background: rgba(148, 163, 184, 0.18);
    }

    .progress-fill {
      height: 100%;
      width: var(--progress);
      border-radius: inherit;
      background: linear-gradient(90deg, var(--accent), #22c55e);
      transition: width 0.2s ease;
    }

    .celebrate {
      position: absolute;
      inset: 0;
      display: none;
      place-items: center;
      background: rgba(15, 23, 42, 0.52);
      font-size: 44px;
      pointer-events: none;
    }

    .celebrate.show {
      display: grid;
      animation: pop 0.85s ease both;
    }

    @keyframes pop {
      0% { opacity: 0; transform: scale(0.7); }
      35% { opacity: 1; transform: scale(1.08); }
      100% { opacity: 0; transform: scale(1.2); }
    }

    .empty-state {
      padding: 34px 18px;
      border: 1px dashed var(--line);
      border-radius: var(--radius);
      color: var(--muted);
      text-align: center;
    }

    .question-layout {
      grid-template-columns: minmax(0, 1.1fr) minmax(280px, 0.9fr);
      align-items: start;
    }

    .panel {
      padding: 18px;
    }

    .subject-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 16px 0 12px;
    }

    .subject-tab {
      min-height: 36px;
      padding: 0 12px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--panel-2);
      color: var(--muted);
      font-weight: 800;
      transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease;
    }

    .subject-tab:hover,
    .subject-tab:focus-visible,
    .subject-tab.active {
      border-color: var(--accent);
      background: rgba(56, 189, 248, 0.14);
      color: var(--text);
      outline: 0;
    }

    .question-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: 10px;
    }

    .error {
      min-height: 22px;
      color: var(--danger);
      font-size: 13px;
    }

    .answer-box {
      min-height: 220px;
      margin-top: 16px;
      padding: 16px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      background: var(--input);
      white-space: pre-wrap;
      line-height: 1.72;
      overflow-wrap: anywhere;
    }

    .typing {
      display: inline-flex;
      gap: 5px;
      align-items: center;
    }

    .typing span {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--accent);
      animation: blink 1s infinite ease-in-out;
    }

    .typing span:nth-child(2) {
      animation-delay: 0.15s;
    }

    .typing span:nth-child(3) {
      animation-delay: 0.3s;
    }

    @keyframes blink {
      0%, 80%, 100% { opacity: 0.25; transform: translateY(0); }
      40% { opacity: 1; transform: translateY(-4px); }
    }

    .history-list {
      display: grid;
      gap: 10px;
      margin-top: 16px;
    }

    .history-item {
      overflow: hidden;
      box-shadow: none;
    }

    .history-toggle {
      width: 100%;
      padding: 13px;
      background: transparent;
      color: var(--text);
      text-align: left;
      transition: background 0.2s ease;
    }

    .history-toggle:hover,
    .history-toggle:focus-visible {
      background: rgba(56, 189, 248, 0.1);
      outline: 0;
    }

    .history-meta {
      display: block;
      margin-bottom: 5px;
      color: var(--accent);
      font-size: 12px;
      font-weight: 800;
    }

    .history-question {
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .history-body {
      display: none;
      padding: 0 13px 13px;
      color: var(--muted);
      line-height: 1.65;
      white-space: pre-wrap;
    }

    .history-item.open .history-body {
      display: block;
    }

    .stats-grid {
      grid-template-columns: minmax(0, 1.2fr) minmax(250px, 0.8fr);
      align-items: start;
    }

    .bar-list {
      display: grid;
      gap: 14px;
      margin-top: 18px;
    }

    .bar-row {
      display: grid;
      grid-template-columns: 72px minmax(0, 1fr) 52px;
      gap: 10px;
      align-items: center;
    }

    .bar-track {
      height: 12px;
      overflow: hidden;
      border-radius: 999px;
      background: rgba(148, 163, 184, 0.18);
    }

    .bar-fill {
      height: 100%;
      width: var(--bar);
      border-radius: inherit;
      background: var(--accent);
      transition: width 0.2s ease;
    }

    .stat-number {
      margin-top: 14px;
      font-family: "Outfit", sans-serif;
      font-size: 38px;
      font-weight: 800;
    }

    .mobile-tabs {
      display: none;
    }

    @media (max-width: 860px) {
      .app {
        grid-template-columns: 1fr;
        padding-bottom: 76px;
      }

      .sidebar {
        display: none;
      }

      .main {
        padding: 18px;
      }

      .topbar,
      .toolbar {
        grid-template-columns: 1fr;
        flex-direction: column;
        align-items: stretch;
      }

      .summary-grid,
      .question-layout,
      .stats-grid,
      .plan-form {
        grid-template-columns: 1fr;
      }

      .date-picker {
        justify-content: space-between;
      }

      .date-label {
        min-width: 132px;
      }

      .mobile-tabs {
        position: fixed;
        right: 12px;
        bottom: 12px;
        left: 12px;
        z-index: 20;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 6px;
        padding: 8px;
        border: 1px solid var(--line);
        border-radius: var(--radius);
        background: color-mix(in srgb, var(--panel) 92%, transparent);
        box-shadow: var(--shadow);
        backdrop-filter: blur(18px);
      }

      .mobile-tabs .nav-btn {
        justify-content: center;
        padding: 10px 8px;
        font-size: 12px;
      }

      .mobile-tabs .nav-btn.active {
        box-shadow: none;
      }
    }
  </style>
</head>
<body>
  <script>
    // 사용자가 직접 Anthropic API 키를 입력하세요. 브라우저에 노출되므로 개인 테스트 용도로만 사용하세요.
    const ANTHROPIC_API_KEY = "";
  </script>

  <div class="app">
    <aside class="sidebar">
      <div class="brand">
        <span class="brand-mark">S</span>
        Study Hub
      </div>
      <nav class="nav" aria-label="주요 메뉴">
        <button class="nav-btn active" data-tab="plans">📅 오늘의 계획</button>
        <button class="nav-btn" data-tab="question">🔍 개념 질문</button>
        <button class="nav-btn" data-tab="stats">📊 학습 통계</button>
      </nav>
    </aside>

    <main class="main">
      <header class="topbar">
        <div>
          <h1>올인원 학습 관리</h1>
          <p class="subtitle">일간 목표, 개념 질문, 학습 통계를 한 화면에서 관리하세요.</p>
        </div>
        <button class="theme-toggle" id="themeToggle" type="button" aria-label="라이트 다크 전환">🌙 다크</button>
      </header>

      <section class="tab-panel active" id="plansPanel">
        <div class="toolbar">
          <div class="date-picker" aria-label="날짜 선택">
            <button class="icon-btn" id="prevDay" type="button" aria-label="이전 날">‹</button>
            <div class="date-label" id="dateLabel"></div>
            <button class="icon-btn" id="nextDay" type="button" aria-label="다음 날">›</button>
          </div>
          <button class="primary-btn" id="toggleForm" type="button">+ 계획 추가</button>
        </div>

        <div class="summary-grid">
          <div class="summary-card donut-wrap">
            <div class="donut" id="summaryDonut" style="--rate:0">
              <div class="donut-inner" id="summaryRate">0%</div>
            </div>
          </div>
          <div class="summary-card">
            <div class="summary-label">완료 항목 수 / 전체 항목 수</div>
            <div class="summary-value" id="summaryItems">0 / 0</div>
          </div>
          <div class="summary-card">
            <div class="summary-label">오늘 달성 시간</div>
            <div class="summary-value" id="summaryHours">0h / 0h</div>
          </div>
        </div>

        <section class="panel form-panel" id="formPanel">
          <form class="plan-form" id="planForm">
            <label>
              과목
              <select id="planSubject" required>
                <option value="수학">수학</option>
                <option value="과학">과학</option>
                <option value="사회">사회</option>
                <option value="역사">역사</option>
                <option value="영어">영어</option>
                <option value="기타">기타</option>
              </select>
            </label>
            <label>
              목표 내용
              <input id="planGoal" type="text" placeholder="예: 이차방정식 문제집 2단원" required />
            </label>
            <label>
              목표 횟수
              <input id="planTarget" type="number" min="1" max="999" value="1" required />
            </label>
            <button class="primary-btn" type="submit">저장</button>
          </form>
        </section>

        <div class="plans-grid" id="plansGrid"></div>
      </section>

      <section class="tab-panel" id="questionPanel">
        <div class="question-layout">
          <section class="panel">
            <h2>개념 질문</h2>
            <div class="subject-tabs" id="subjectTabs" aria-label="질문 과목 선택">
              <button class="subject-tab active" type="button" data-subject="수학">수학</button>
              <button class="subject-tab" type="button" data-subject="과학">과학</button>
              <button class="subject-tab" type="button" data-subject="사회">사회</button>
              <button class="subject-tab" type="button" data-subject="역사">역사</button>
              <button class="subject-tab" type="button" data-subject="영어">영어</button>
            </div>
            <textarea id="questionInput" placeholder="궁금한 개념을 입력하세요."></textarea>
            <div class="question-actions">
              <div class="error" id="apiError" role="status"></div>
              <button class="primary-btn" id="askBtn" type="button">질문하기</button>
            </div>
            <div class="answer-box" id="answerBox">답변이 여기에 표시됩니다.</div>
          </section>

          <section class="panel">
            <h2>최근 질문</h2>
            <div class="history-list" id="historyList"></div>
          </section>
        </div>
      </section>

      <section class="tab-panel" id="statsPanel">
        <div class="stats-grid">
          <section class="panel">
            <h2>과목별 완료율</h2>
            <div class="bar-list" id="subjectStats"></div>
          </section>
          <section class="panel">
            <h2>총 공부 목표 대비 달성 시간</h2>
            <div class="stat-number" id="totalHours">0h / 0h</div>
            <p class="subtitle" id="totalRateText">달성률 0%</p>
          </section>
        </div>
      </section>
    </main>
  </div>

  <nav class="mobile-tabs" aria-label="모바일 메뉴">
    <button class="nav-btn active" data-tab="plans">📅 계획</button>
    <button class="nav-btn" data-tab="question">🔍 질문</button>
    <button class="nav-btn" data-tab="stats">📊 통계</button>
  </nav>

  <script>
    // ─── 기본 상태 ───
    const subjects = ["수학", "과학", "사회", "역사", "영어", "기타"];
    const questionSubjects = ["수학", "과학", "사회", "역사", "영어"];
    const state = {
      currentDate: new Date(),
      selectedSubject: "수학",
      plans: [],
      history: []
    };

    const $ = (selector) => document.querySelector(selector);
    const $$ = (selector) => [...document.querySelectorAll(selector)];

    const refs = {
      dateLabel: $("#dateLabel"),
      prevDay: $("#prevDay"),
      nextDay: $("#nextDay"),
      toggleForm: $("#toggleForm"),
      formPanel: $("#formPanel"),
      planForm: $("#planForm"),
      planSubject: $("#planSubject"),
      planGoal: $("#planGoal"),
      planTarget: $("#planTarget"),
      plansGrid: $("#plansGrid"),
      summaryDonut: $("#summaryDonut"),
      summaryRate: $("#summaryRate"),
      summaryItems: $("#summaryItems"),
      summaryHours: $("#summaryHours"),
      themeToggle: $("#themeToggle"),
      questionInput: $("#questionInput"),
      askBtn: $("#askBtn"),
      answerBox: $("#answerBox"),
      apiError: $("#apiError"),
      historyList: $("#historyList"),
      subjectStats: $("#subjectStats"),
      totalHours: $("#totalHours"),
      totalRateText: $("#totalRateText")
    };

    function dayKey(date = state.currentDate) {
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const day = String(date.getDate()).padStart(2, "0");
      return `${year}-${month}-${day}`;
    }

    function storageKey() {
      return `studyPlans_${dayKey()}`;
    }

    function clamp(number, min, max) {
      return Math.min(Math.max(number, min), max);
    }

    function escapeHtml(value) {
      return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }

    // ─── localStorage 관리 ───
    function loadPlans() {
      try {
        state.plans = JSON.parse(localStorage.getItem(storageKey())) || [];
      } catch {
        state.plans = [];
      }
    }

    function savePlans() {
      localStorage.setItem(storageKey(), JSON.stringify(state.plans));
    }

    function loadHistory() {
      try {
        state.history = JSON.parse(localStorage.getItem("conceptHistory")) || [];
      } catch {
        state.history = [];
      }
    }

    function saveHistory() {
      localStorage.setItem("conceptHistory", JSON.stringify(state.history.slice(0, 5)));
    }

    // ─── 탭 전환 ───
    function activateTab(tabName) {
      $$(".tab-panel").forEach((panel) => panel.classList.remove("active"));
      $(`#${tabName}Panel`).classList.add("active");

      $$("[data-tab]").forEach((button) => {
        button.classList.toggle("active", button.dataset.tab === tabName);
      });

      if (tabName === "stats") renderStats();
    }

    $$("[data-tab]").forEach((button) => {
      button.addEventListener("click", () => activateTab(button.dataset.tab));
    });

    // ─── 테마 관리 ───
    function applyTheme(theme) {
      document.body.classList.toggle("light", theme === "light");
      refs.themeToggle.textContent = theme === "light" ? "☀️ 라이트" : "🌙 다크";
      localStorage.setItem("studyTheme", theme);
    }

    refs.themeToggle.addEventListener("click", () => {
      const nextTheme = document.body.classList.contains("light") ? "dark" : "light";
      applyTheme(nextTheme);
    });

    // ─── 계획 관리 ───
    function updateDayView() {
      refs.dateLabel.textContent = state.currentDate.toLocaleDateString("ko-KR", {
        year: "numeric",
        month: "long",
        day: "numeric",
        weekday: "short"
      });
      loadPlans();
      renderPlans();
      renderSummary();
      renderStats();
    }

    refs.prevDay.addEventListener("click", () => {
      state.currentDate.setDate(state.currentDate.getDate() - 1);
      updateDayView();
    });

    refs.nextDay.addEventListener("click", () => {
      state.currentDate.setDate(state.currentDate.getDate() + 1);
      updateDayView();
    });

    refs.toggleForm.addEventListener("click", () => {
      refs.formPanel.classList.toggle("open");
      refs.planGoal.focus();
    });

    refs.planForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const target = Math.max(Number(refs.planTarget.value), 1);
      state.plans.unshift({
        id: crypto.randomUUID ? crypto.randomUUID() : String(Date.now()),
        subject: refs.planSubject.value,
        goal: refs.planGoal.value.trim(),
        target,
        completed: 0,
        celebrated: false,
        createdAt: new Date().toISOString()
      });
      savePlans();
      refs.planForm.reset();
      refs.planTarget.value = 1;
      refs.formPanel.classList.remove("open");
      renderPlans();
      renderSummary();
      renderStats();
    });

    function setCompleted(id, delta) {
      const plan = state.plans.find((item) => item.id === id);
      if (!plan) return;

      const beforeDone = plan.completed >= plan.target;
      plan.completed = clamp(plan.completed + delta, 0, plan.target);
      const afterDone = plan.completed >= plan.target;
      savePlans();
      renderPlans(afterDone && !beforeDone ? id : null);
      renderSummary();
      renderStats();
    }

    function deletePlan(id) {
      state.plans = state.plans.filter((item) => item.id !== id);
      savePlans();
      renderPlans();
      renderSummary();
      renderStats();
    }

    function renderPlans(celebrateId = null) {
      if (!state.plans.length) {
        refs.plansGrid.innerHTML = `<div class="empty-state">오늘 계획이 아직 없습니다.</div>`;
        return;
      }

      refs.plansGrid.innerHTML = state.plans.map((plan) => {
        const percent = Math.round((plan.completed / plan.target) * 100);
        const safeGoal = escapeHtml(plan.goal);
        return `
          <article class="plan-card ${percent >= 100 ? "done" : ""}">
            <div class="plan-head">
              <span class="subject-pill">${escapeHtml(plan.subject)}</span>
              <button class="danger-btn" type="button" aria-label="계획 삭제" data-delete="${plan.id}">🗑</button>
            </div>
            <div class="plan-title">${safeGoal}</div>
            <div class="spinner-row">
              <span class="summary-label">완료 횟수 입력</span>
              <div class="counter">
                <button class="icon-btn" type="button" aria-label="완료 횟수 감소" data-dec="${plan.id}">−</button>
                <span class="counter-value">${plan.completed}</span>
                <button class="icon-btn" type="button" aria-label="완료 횟수 증가" data-inc="${plan.id}">+</button>
              </div>
            </div>
            <div class="progress-meta">
              <span>${plan.completed} / ${plan.target}회</span>
              <strong>${percent}%</strong>
            </div>
            <div class="progress" aria-label="진행률 ${percent}%">
              <div class="progress-fill" style="--progress:${percent}%"></div>
            </div>
            <div class="celebrate ${celebrateId === plan.id ? "show" : ""}" aria-hidden="true">🎉</div>
          </article>
        `;
      }).join("");

      refs.plansGrid.querySelectorAll("[data-inc]").forEach((button) => {
        button.addEventListener("click", () => setCompleted(button.dataset.inc, 1));
      });
      refs.plansGrid.querySelectorAll("[data-dec]").forEach((button) => {
        button.addEventListener("click", () => setCompleted(button.dataset.dec, -1));
      });
      refs.plansGrid.querySelectorAll("[data-delete]").forEach((button) => {
        button.addEventListener("click", () => deletePlan(button.dataset.delete));
      });
    }

    function getSummary() {
      const totalItems = state.plans.length;
      const doneItems = state.plans.filter((plan) => plan.completed >= plan.target).length;
      const targetHours = state.plans.reduce((sum, plan) => sum + plan.target, 0);
      const doneHours = state.plans.reduce((sum, plan) => sum + plan.completed, 0);
      const itemRate = totalItems ? Math.round((doneItems / totalItems) * 100) : 0;
      const hourRate = targetHours ? Math.round((doneHours / targetHours) * 100) : 0;
      return { totalItems, doneItems, targetHours, doneHours, itemRate, hourRate };
    }

    function renderSummary() {
      const summary = getSummary();
      refs.summaryDonut.style.setProperty("--rate", summary.itemRate);
      refs.summaryRate.textContent = `${summary.itemRate}%`;
      refs.summaryItems.textContent = `${summary.doneItems} / ${summary.totalItems}`;
      refs.summaryHours.textContent = `${summary.doneHours}h / ${summary.targetHours}h`;
    }

    // ─── AI 질문 관리 ───
    $$(".subject-tab").forEach((button) => {
      button.addEventListener("click", () => {
        state.selectedSubject = button.dataset.subject;
        $$(".subject-tab").forEach((tab) => tab.classList.toggle("active", tab === button));
      });
    });

    refs.askBtn.addEventListener("click", askConceptQuestion);

    function buildSystemPrompt(subject) {
      return `당신은 대한민국 중학교·고등학교 교과 과정 전문 튜터입니다.
학생이 ${subject}에 대해 질문하면 해당 교과서 수준에 맞게
핵심 공식·개념·원리를 단계적으로 명확하게 설명해주세요.
수학의 경우 LaTeX 없이 유니코드 수식 기호(², ×, √, π 등)를 사용하고,
예시 문제와 풀이 과정도 함께 제시하세요.`;
    }

    async function askConceptQuestion() {
      const question = refs.questionInput.value.trim();
      refs.apiError.textContent = "";

      if (!question) {
        refs.apiError.textContent = "질문 내용을 입력해주세요.";
        refs.questionInput.focus();
        return;
      }

      if (!ANTHROPIC_API_KEY) {
        refs.apiError.textContent = "HTML 상단의 ANTHROPIC_API_KEY에 API 키를 입력해주세요.";
        return;
      }

      refs.askBtn.disabled = true;
      refs.answerBox.innerHTML = `<span class="typing" aria-label="답변 생성 중"><span></span><span></span><span></span></span>`;

      try {
        const answer = await streamAnthropicAnswer(question, state.selectedSubject);
        addHistory({
          subject: state.selectedSubject,
          question,
          answer,
          createdAt: new Date().toISOString()
        });
        refs.questionInput.value = "";
      } catch (error) {
        refs.answerBox.textContent = "답변 생성에 실패했습니다.";
        refs.apiError.textContent = error.message || "API 호출 중 문제가 발생했습니다. 키와 네트워크 상태를 확인해주세요.";
      } finally {
        refs.askBtn.disabled = false;
      }
    }

    async function streamAnthropicAnswer(question, subject) {
      const response = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "x-api-key": ANTHROPIC_API_KEY,
          "anthropic-version": "2023-06-01",
          "anthropic-dangerous-direct-browser-access": "true"
        },
        body: JSON.stringify({
          model: "claude-sonnet-4-20250514",
          max_tokens: 1200,
          stream: true,
          system: buildSystemPrompt(subject),
          messages: [
            {
              role: "user",
              content: question
            }
          ]
        })
      });

      if (!response.ok || !response.body) {
        const fallback = await response.text().catch(() => "");
        throw new Error(fallback || `API 오류가 발생했습니다. 상태 코드: ${response.status}`);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      let buffer = "";
      let answer = "";
      refs.answerBox.textContent = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const events = buffer.split("\n\n");
        buffer = events.pop() || "";

        for (const event of events) {
          const lines = event.split("\n");
          const dataLine = lines.find((line) => line.startsWith("data: "));
          if (!dataLine) continue;

          const data = dataLine.slice(6);
          if (data === "[DONE]") continue;

          try {
            const parsed = JSON.parse(data);
            if (parsed.type === "content_block_delta" && parsed.delta?.text) {
              answer += parsed.delta.text;
              refs.answerBox.textContent = answer;
            }
          } catch {
            // 스트림 중간의 불완전한 JSON 조각은 다음 청크에서 처리합니다.
          }
        }
      }

      return answer.trim();
    }

    function addHistory(item) {
      state.history = [item, ...state.history].slice(0, 5);
      saveHistory();
      renderHistory();
    }

    function renderHistory() {
      if (!state.history.length) {
        refs.historyList.innerHTML = `<div class="empty-state">최근 질문이 없습니다.</div>`;
        return;
      }

      refs.historyList.innerHTML = state.history.map((item, index) => {
        const date = new Date(item.createdAt).toLocaleString("ko-KR", {
          month: "short",
          day: "numeric",
          hour: "2-digit",
          minute: "2-digit"
        });
        return `
          <article class="history-item">
            <button class="history-toggle" type="button" data-history="${index}">
              <span class="history-meta">${escapeHtml(item.subject)} · ${date}</span>
              <span class="history-question">${escapeHtml(item.question)}</span>
            </button>
            <div class="history-body">${escapeHtml(item.answer)}</div>
          </article>
        `;
      }).join("");

      refs.historyList.querySelectorAll("[data-history]").forEach((button) => {
        button.addEventListener("click", () => {
          button.closest(".history-item").classList.toggle("open");
        });
      });
    }

    // ─── 통계 관리 ───
    function renderStats() {
      const rows = subjects.map((subject) => {
        const items = state.plans.filter((plan) => plan.subject === subject);
        const target = items.reduce((sum, plan) => sum + plan.target, 0);
        const completed = items.reduce((sum, plan) => sum + plan.completed, 0);
        const rate = target ? Math.round((completed / target) * 100) : 0;
        return { subject, rate };
      });

      refs.subjectStats.innerHTML = rows.map((row) => `
        <div class="bar-row">
          <strong>${row.subject}</strong>
          <div class="bar-track" aria-label="${row.subject} 완료율 ${row.rate}%">
            <div class="bar-fill" style="--bar:${row.rate}%"></div>
          </div>
          <span>${row.rate}%</span>
        </div>
      `).join("");

      const summary = getSummary();
      refs.totalHours.textContent = `${summary.doneHours}h / ${summary.targetHours}h`;
      refs.totalRateText.textContent = `달성률 ${summary.hourRate}%`;
    }

    // ─── 초기화 ───
    function init() {
      applyTheme(localStorage.getItem("studyTheme") || "dark");
      loadHistory();
      updateDayView();
      renderHistory();
    }

    init();
  </script>
</body>
</html>
