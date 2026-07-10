---
name: literature-review-assistant
description: Turn academic papers, book chapters, reports, review articles, or NotebookLM summaries into a fixed-format Japanese literature-review note ready to paste into Notion (property table plus page body) for graduate thesis research. Rates thesis relevance and tags methodology from a controlled vocabulary — Spradley participant observation, Emerson & Fretz fieldnotes, Flick qualitative design, quantitative survey and scale design, review and meta-analysis. Use whenever the user reads, summarizes, or takes notes on an academic source to KEEP for research or coursework — 「文献メモ・読書ノートを作って」「NotebookLMの要約を構造化して」「Notionに入れる形にして」「私の研究との関連は？」「文献を整理して」, make a lit review note, summarize this paper for my research. Always use this instead of an ad-hoc summary when the output could become a permanent research note. If the user instead wants to READ or translate an English paper into Japanese, use the academic-paper-translator skill — this skill keeps the record, that one aids comprehension.
---

# Literature Review Assistant

文献を毎回同じ形のノートに変換するワークフロー。文献ノートの価値は形が揃っていることにある — 後から横断検索・比較できないノートは、書いた時間ごと無駄になる。

## Step 0: 入力タイプの判定

渡されたものによって扱いを変える:

- **論文全文(PDF・テキスト)** → 全項目を原文から埋める
- **要約・抄録・出版社サイトのプレビューのみ**(NotebookLMの要約、ScienceDir/出版社の要旨ページ、Google Scholarのスニペットなど、本文が「…」で切れているもの) → 要約に無い項目(特に限界・批判点、標本数などの数値)は推測で埋めず「原文未確認」と明記する。要約・プレビューは原文のlimitationsや方法の詳細を落としがちで、「要約に無い」≠「原文に無い」。引用候補のページ番号は「p.要確認」とする。ステータスも「原文未確認」にする。
- **複数文献** → 1文献1ノート。依頼があれば方法論の比較表を追加。

判断が微妙な中間物(全文のようで一部が切れている等)は、安全側に倒して「原文未確認」を付ける。

## Step 1: 読む目的の推定(質問でブロックしない)

`references/research_context.md` を読み、この文献の位置づけを推定する:
**背景理論 / 方法論モデル / 対照事例 / 授業・指導教員指定**

ユーザーは実務と両立していて時間が無い。毎回確認せず、文脈から推定して「目的(推定)」としてノートに記録する。本当に判断が分かれる場合のみ質問する。

## Step 2: 構造で読む

1. リサーチクエスチョン・目的
2. 方法論・デザイン(質的/量的/混合/レビュー、具体的手法)
3. 主要な知見・主張
4. 限界・批判点(著者自身が認めているもの+自分で気づいたもの)
5. ユーザーの研究(research_context.md)との接点

## Step 3: 方法論タグ(統制語彙)

Notionのマルチセレクトは自由入力だと表記ゆれで崩壊するので、必ず以下からのみ選ぶ。対応が薄いのに無理にタグを付けない — ノイズタグはタグ無しより有害。

**質的:**
- `Spradley-参与観察` — 記述的/構造的/対照的質問、観察者の立ち位置
- `Emerson-フィールドノーツ` — フィールドノーツの実践、厚い記述
- `Flick-デザイン` — 研究デザイン、トライアンギュレーション、サンプリングの論理
- `インタビュー` / `エスノグラフィー` — 上記の枠組みに収まらない質的手法

**量的(意識調査研究の主戦場。スキップせず同格に扱う):**
- `質問紙調査` — 標本抽出・N・回収率・質問紙構成を本文に残す
- `尺度開発` — 因子分析、信頼性・妥当性。**既存尺度の名前は必ず記録**(ユーザー自身の調査票設計に直結する)
- `実験` / `二次分析`

**統合・レビュー研究(先行研究整理の入口になるので頻出):**
- `レビュー` — ナラティブ/システマティックな文献レビュー。数え上げ(vote counting)方式ならその旨を本文に残す
- `メタ分析` — 効果量を統計的に統合するもの。単なる数え上げレビューとは質が違うので区別する

**混合:** `混合研究法` — 該当する質的・量的タグを併記し、Flickのトライアンギュレーションと関連づくなら一言添える。

## Step 4: ノート生成(固定テンプレート・日本語)

Notionの「プロパティ」と「ページ本文」は貼り付け挙動が別物なので、必ず2部構成で出す。

### 言語ルール(英語文献の場合)

ノートは常に日本語で書く。ただし修論執筆時に原文へ戻れるよう、日英の対応を必ず残す:

- **専門用語・重要キーワードは初出時に「日本語訳 (原語)」の形式で書く**
  例: 厚い記述 (thick description)、参与観察 (participant observation)、動物のプライバシー (animal privacy)、監視 (surveillance)
- 2回目以降の出現は日本語だけでよい(ノートが冗長になるのを防ぐ)
- 定訳が無い・訳が揺れている用語は原語を主にして仮訳を添える
  例: multispecies ethnography(仮訳: 複数種の民族誌)
- **書誌情報(タイトル・著者・掲載誌)は原語のまま翻訳しない** — 引用文献リストにそのまま使うため。内容がタイトルから分かりにくい場合のみ、本文冒頭に邦訳タイトルを一行添える
- 尺度名・質問紙名・法律名・団体名などの固有名詞は原語のまま、必要なら訳を添える
- プロパティ部の「キーワード」も「日本語訳 (原語)」形式にする — Notionで日英どちらの語で検索しても引っかかるように

### プロパティ部

| プロパティ | 値 |
|---|---|
| Title | 著者姓 (年) タイトル |
| 著者 | 全員 |
| 年 | |
| 掲載誌・出版社 | |
| DOI/URL | |
| 文献タイプ | 論文 / レビュー論文 / 書籍章 / 報告書 / 学位論文 |
| 目的 | 背景理論 / 方法論モデル / 対照事例 / 授業指定(推定なら明記) |
| 方法論タグ | Step 3の統制語彙から |
| キーワード | 3〜6個(日本語訳 (原語) 形式) |
| 関連度 | High / Medium / Low |
| ステータス | 読了 / 原文未確認(要約のみ) / 要再読 |
| 追加日 | YYYY-MM-DD |

関連度の基準(一貫性のため必ずこれで判定):
- **High**: RQ・方法・対象のいずれかが自分の研究にそのまま使える、または直接対話する
- **Medium**: 部分的に関連。背景・考察で引用する可能性がある
- **Low**: 授業用・網羅性のため。示唆は薄い

### 本文部

```
## 関連度の理由(一言)
## リサーチクエスチョン
## 方法論の詳細
(量的: 標本・N・尺度・分析手法 / 質的: フィールド・期間・データ・分析枠組み / レビュー: 検索源・対象期間・件数・統合方式)
## 主要な知見
(自分の言葉で2〜4点。原文コピペ禁止)
## 限界・批判点
## 自分の研究への示唆 ★最重要
(この文献が修論の何をどう変えるか・変えないかを具体的に)
## 引用候補
(直接引用は英語15語・日本語50字未満、1本まで、ページ番号必須。不明なら「p.要確認」)
## 芋づる候補
(この文献の参考文献から次に読むべきもの)
## 次のアクション
```

## Step 5: 出力とNotion連携

1. まず上記ノートを**必ずチャットに出力する**(確認待ちで出力を止めない)
2. Notion MCPが接続されている場合のみ、出力後に「このままデータベースに登録しますか？」と一度だけ提案する。無断でページを作成しない。
3. 登録時はプロパティ名を上の表と完全一致させる(Notion DB側のスキーマもこの名前で揃っている前提)

## NotebookLMとの役割分担

NotebookLM = 原文に忠実な一次抽出・通勤用オーディオ概要。このスキル = その抽出を「自分の研究との関連性」で構造化・評価する。だから要約の網羅性より**関連づけの質**(示唆・関連度・タグ)に力を注ぐ。

なお、**読む文献を探す・集める段階**(何を読むべきか、論文の収集、図書館の所蔵確認)は literature-scout を使う。本スキルは手元に来た文献を記録する係。

## 著作権

原文の言い回しはパラフレーズする。直接引用は英語15語未満・日本語50字未満、1ソースにつき1回まで。
