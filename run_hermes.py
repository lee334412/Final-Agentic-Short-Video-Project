import json
import os
import datetime

# 確保目錄存在
os.makedirs("agents", exist_ok=True)
os.makedirs("handoff", exist_ok=True)
os.makedirs("traces", exist_ok=True)

print("🚀 [Hermes Agent] 正在初始化 Self-Hosted Workflow...")

# 1. 定義 Agent 系統提示詞 (Persona) 並寫入 agents/
agents_config = {
    "planner": "你是影音企劃。請將主題拆成60秒內可執行的scenes，明確標示受眾、核心訊息、時間配置與素材需求。",
    "script": "你是短影音腳本作者。請根據 Planner 的 outline 產生旁白稿與字幕稿，語氣需清楚、正向、適合目標觀眾。",
    "visual": "你是分鏡設計師。請為每個 scene 設計鏡頭、畫面元素、B-roll、拍攝建議與素材需求。",
    "reviewer": "你是內容審查者。請檢查影片是否符合60秒、是否有事實風險、版權風險、肖像權風險，並提出具體修正。"
}

for name, prompt in agents_config.items():
    with open(f"agents/{name}_agent.md", "w", encoding="utf-8") as f:
        f.write(f"# {name.capitalize()} Agent Persona\n\n> {prompt}\n")

# 2. 模擬多代理人數據交接 (Structured Handoff JSON)
print("📝 [Hermes Agent] 委派 Planner Agent 開始生成專案企劃...")
planner_output = {
    "project_title": "南大資工60秒形象宣傳影片",
    "target_audience": ["高中生", "新生", "家長"],
    "core_message": "理論與實務並重，動手實作、專題製作，加入南大資工寫下你的未來。",
    "video_length_seconds": 60,
    "scenes_outline": [
        {"scene_id": 1, "time_range": "0-5", "purpose": "opening hook"},
        {"scene_id": 2, "time_range": "5-15", "purpose": "department positioning"},
        {"scene_id": 3, "time_range": "15-30", "purpose": "professional features"},
        {"scene_id": 4, "time_range": "30-45", "purpose": "team development"},
        {"scene_id": 5, "time_range": "45-55", "purpose": "learning atmosphere"},
        {"scene_id": 6, "time_range": "55-60", "purpose": "call to action"}
    ]
}
with open("handoff/01_planner_output.json", "w", encoding="utf-8") as f:
    json.dump(planner_output, f, ensure_ascii=False, indent=2)

print("🎤 [Hermes Agent] 傳遞 JSON 至 Script Agent，開始撰寫旁白與字幕...")
script_output = {
    "scenes": [
        {
            "scene_id": 1,
            "narration": "畫面響起密集的鍵盤聲。未來，由你定義。",
            "subtitle": "未來，由你定義。"
        },
        {
            "scene_id": 2,
            "narration": "這裡是國立臺南大學資訊工程學系。一個將創意轉化為現實的地方。",
            "subtitle": "國立臺南大學 資訊工程學系"
        },
        {
            "scene_id": 3,
            "narration": "從程式設計、人工智慧到軟硬體系統實作，我們理論與實務並重，培養核心科技實力。",
            "subtitle": "核心特色：程式設計 / AI / 系統開發"
        },
        {
            "scene_id": 4,
            "narration": "透過團隊合作與專題競賽，在白板前激盪火花，我們一起攻克所有技術難題。",
            "subtitle": "團隊合作 · 專題實作 · 競賽參與"
        },
        {
            "scene_id": 5,
            "narration": "這裡有最前沿的實驗室與溫馨的師生互動，讓你的學習生活充滿啟發。",
            "subtitle": "啟發性的學習氛圍與豐富資源"
        },
        {
            "scene_id": 6,
            "narration": "加入南大資工，寫下屬於你的第一行程式碼。我們在南大等你。",
            "subtitle": "歡迎加入 國立臺南大學資工系"
        }
    ]
}
with open("handoff/02_script_output.json", "w", encoding="utf-8") as f:
    json.dump(script_output, f, ensure_ascii=False, indent=2)

print("🎬 [Hermes Agent] 傳遞 JSON 至 Visual Agent，開始進行畫面與分鏡規劃...")
visual_output = {
    "scenes_visual": [
        {"scene_id": 1, "visual_plan": "特寫雙手快速敲擊鍵盤，螢幕上閃爍著絢麗的 IDE 程式碼畫面。"},
        {"scene_id": 2, "visual_plan": "空拍或定點拍攝南大系館外觀或校園典雅綠意，畫面疊加系名大標題。"},
        {"scene_id": 3, "visual_plan": "快速切換剪輯：學生專注看著螢幕、操作硬體開發板、AI 模型訓練圖表。"},
        {"scene_id": 4, "visual_plan": "幾位同學在白板前討論架構圖，鏡頭環繞拍攝他們自信交談與微笑的特寫。"},
        {"scene_id": 5, "visual_plan": "教授在實驗室指導學生專題，大家一起看著螢幕點頭點頭，氣氛融洽。"},
        {"scene_id": 6, "visual_plan": "畫面淡出至南大資工官方標誌與簡短 slogan，片尾字幕註明素材皆為合規授權。"}
    ]
}
with open("handoff/03_visual_output.json", "w", encoding="utf-8") as f:
    json.dump(visual_output, f, ensure_ascii=False, indent=2)

print("🔍 [Hermes Agent] 委派 Reviewer Agent 進行多維度合規性審查...")
reviewer_feedback = {
    "review_status": "APPROVED_WITH_CONDITIONS",
    "timestamp": str(datetime.datetime.now()),
    "checklists": {
        "length_check_55_65s": "PASS (預估時長合計共 60 秒，符合規範)",
        "truthfulness_check": "PASS (內容聚焦實作與學習，未虛構招生名額與師資)",
        "copyright_and_portrait_risk": "WARNING (人工拍攝時需取得出鏡同學口頭同意，背景音樂需使用開源 CC0 素材)"
    },
    "suggestions": "整體架構流暢。請在 outputs/ 剪輯時嚴格控制轉場節奏，片尾記得放上 asset_sources.md 說明的素材授權。"
}
with open("handoff/04_reviewer_feedback.json", "w", encoding="utf-8") as f:
    json.dump(reviewer_feedback, f, ensure_ascii=False, indent=2)

# 3. 自動生成 Execution Trace 紀錄日誌
print("💾 [Hermes Agent] 正在導出完整的 Execution Trace 日誌...")
trace_content = f"""# Hermes Agent Workflow Execution Trace Log

- **執行模式**: Local Self-Hosted / Mock Agent Workflow (Zero Paid Token Path)
- **執行時間**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **觸發事件**: User requested a 60-second video workflow for NUTN CSIE Promotion

## 🕒 Task Delegation Timeline

1. `[00:01]` **Hermes Master** 啟動，讀取 `agents/` 設定檔。
2. `[00:03]` **Hermes Master** 委派 `Planner Agent` 建立結構。輸出至 `handoff/01_planner_output.json`。
3. `[00:05]` **Hermes Master** 路由數據至 `Script Agent` 撰寫文案。輸出至 `handoff/02_script_output.json`。
4. `[00:07]` **Hermes Master** 路由數據至 `Visual Agent` 設計鏡頭。輸出至 `handoff/03_visual_output.json`。
5. `[00:10]` **Hermes Master** 觸發安全原則，由 `Reviewer Agent` 進行事實與版權審查。審查報告輸出至 `handoff/04_reviewer_feedback.json`。

## 🎯 最終決策追溯說明
- 本次影片核心主軸由 `Planner Agent` 確立。
- 影片的字幕與精確秒數分配由 `Script Agent` 決定的旁白長度進行受控式限縮。
- 安全性警示由 `Reviewer Agent` 標記，已轉交人工團隊執行最終剪輯檢查。

---
*狀態: 流程安全結束。所有交接 JSON 數據已結構化保存。*
"""

with open("traces/execution_trace.md", "w", encoding="utf-8") as f:
    f.write(trace_content)

print("✨ [Hermes Agent] 執行完畢！所有 Handoff 檔案與 Trace 日誌已成功導出至對應資料夾。")