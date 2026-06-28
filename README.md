# Final 自主學習作業：OpenClaw/ Hermes Agent 多代理人短影片工作流程

## 🎯 專案基本資訊
- **專案名稱**：國立臺南大學資訊工程學系 60秒形象宣傳影片
- **加分項目**：已選定「NUTN CSIE 60-second promotional video」
- **學號**：S11259044
- **使用平台**：Hermes Agent (Self-Hosted / Local Model Mock Run Workflow)

---

## 📢 零付費 Token 可完成性聲明
> **本專案完全基於零付費 path 完成。**
> 系統架構使用 Hermes Agent 框架，採用結構化 Mock/Stub 模式模擬 Planner、Script、Visual 與 Reviewer 四個代理人的數據路由與狀態交接。過程中無使用任何個人付費 API key，亦無訂閱任何付費 AI 影音工具，100% 符合平台公平性與受控式工作流 (Controlled Workflow) 的評分要求。

---

## 📁 儲存庫目錄結構說明
本專案嚴格遵循多媒體系統實驗室之規範，根目錄結構如下：

- 📂 `report/` : 存放期末專案報告 PDF 檔 (`Final_Report_S11259044.pdf`)。
- 📂 `agents/` : 存放 4 個 Specialized Agents 的 Persona 系統提示詞設定。
- 📂 `handoff/` : 存放 Agent 之間遞迴交接的標準結構化 JSON 檔案（01~04）。
- 📂 `traces/` : 存放主控台自動導出的 `execution_trace.md` 時間軸日誌紀錄。
- 📂 `outputs/` : 
  - 🎥 `final_video.mp4` : 最終交付之 9:16 直式短影片成果（片長 60 秒，符合 55-65s 誤差範圍）。
  - 📝 `asset_sources.md` : 影片中所有 AI 繪圖生成與開源背景配樂的授權說明。

---

## 🤖 多代理人系統架構 (Agent Design & Handoff)
本系統將短影片任務解構為四個專門代理人，並透過主控台完成數據流交接：

1. **Planner Agent (企劃)** -> 產出影片核心受眾(高中生/新生)與 6 大場景結構。
2. **Script Agent (腳本)** -> 基於企劃結構，受限秒數內精準撰寫旁白與直式字幕。
3. **Visual Agent (分鏡)** -> 依據腳本文案，規劃 9:16 垂直構圖 (Vertical composition) 生圖畫面與運鏡提示。
4. **Reviewer Agent (審查)** -> 針對長度、內容真實性（不虛構系所資訊）、版權與肖像權進行合規性攔截審查。

> 💡 每個 Agent 的中間輸出皆完整保存於 `handoff/` 中，可透過標準 JSON 追溯最終短影片中的主要決策來源。

---

## 📊 Baseline 比較摘要
本專案於報告中建立了 **Single-Agent Baseline** 對照組（使用單一 Prompt 直接要求 LLM 生成 60 秒腳本）。
經實驗評估，Multi-Agent Workflow 在**時間長度精準控制**、**安全性與事實審查 (Fact-checking)**，以及**分鏡結構完整度**上，皆顯著優於單一 Prompt 產出，充分展現受控式協作流之學習價值。
