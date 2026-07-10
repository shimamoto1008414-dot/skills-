---
name: academic-paper-translator
description: Fully translate an English academic paper into Japanese for graduate research, preserving the paper's structure so the flow of the argument stays intact. Leads with a short summary, then gives a complete (not condensed) translation, a term glossary that keeps the original English in parentheses, and notes on how the paper connects to the user's animal-privacy thesis. Use whenever the user wants to READ, translate, or understand an English paper, chapter, abstract, or NotebookLM extract — 「この英語論文を翻訳して」「全文翻訳して」「訳して」「和訳して」「この論文何て書いてある？」「英語の論文読みたいけど時間ない」「通勤中に読める形にして」, translate this paper, what does this paper say, summarize this English article so I can understand it. Trigger even when the user just pastes an English paper with little instruction — full Japanese comprehension is the default need. If the user instead wants a permanent fixed-format note for Notion (「文献メモ」「Notionに入れる」), use the literature-review-assistant skill — this skill aids comprehension, that one keeps the record. Output is delivered as a Word (.docx) file, not Markdown.
---

# Academic Paper Translator

英語論文を「日本語で読み通す」ための伴走スキル。修論は日本語で書くが、検索・引用・原文参照は英語で行うため、**意味の理解**と**原語への戻りやすさ**を両立させることが目的。既定は**全文翻訳** — 要約で内容を圧縮してしまうと論の運び(前後の文脈)が消えるので、段落構造を保ったまま省略せずに訳し、上に短い要約を添えて全体像を先に掴めるようにする。

## Step 0: 入力と範囲の判定

**入力タイプ:**
- 論文全文(PDF・テキスト) → 全文を訳す
- 特定の段落・セクションだけを指定 → その範囲だけを全文で訳す
- 抄録・出版社プレビュー・NotebookLM抽出のみ → 手元にある範囲を全文で訳す。本文が「…」で切れている箇所は「(プレビュー未収録)」と明示し、内容を推測で補わない

指示が「訳して」だけでも、既定は**手元の本文すべての全文翻訳**。範囲が段落単位に限定されているときだけその範囲に絞る。確認で止めない。

## Step 1: 言語ルール(共通)

- 日本語で書く。**専門用語・重要キーワードは初出時に「日本語訳 (原語)」形式**にする
  例: 撹乱 (disturbance)、繁殖成功 (reproductive success)、参与観察 (participant observation)
- 2回目以降は日本語だけでよい
- 定訳が無い・訳が揺れる語は原語を主にして仮訳を添える 例: foraging guild(仮訳: 採食ギルド)
- **論文タイトル・著者・掲載誌・尺度名・種の学名・固有名詞は原語のまま**(検索・引用に使うため)。必要なら訳を添える
- 学術文章の**ヘッジ表現(may, suggests, is likely, limited evidence 等)を消さない** — 「〜の可能性がある」「〜を示唆する」と訳し分ける。断定に変えると論文の主張の強さを誤って伝えることになる

## Step 2: 出力(既定 = 全文翻訳、Word .docx ファイルで保存)

**成果物は Word 文書 (.docx) ファイルとして保存する。チャット本文に Markdown を貼らない**(長い翻訳をチャットに流さず、ファイルとして渡す)。文書の中身は以下の構成を上から順に並べ、最上部の要約だけ読めば概要が掴め、その下で全文を読み通せる形にする。下の `## 見出し` は Word の見出しスタイル、`重要用語 対訳集` は Word の表として作る(見た目上の Markdown 記号は残さない)。

```
## ひとことサマリー
(2〜3文。通勤中や一覧で内容を思い出せる粒度。何を問い、何が分かったか。ここだけ要約。以降は圧縮しない)

## 全文翻訳
(論文自身の見出し・段落順に、省略せず全文を日本語に訳す。要約・間引きをしない。
 - 原文の見出し(Abstract / Introduction / Methods ...)を日本語見出し＋(原語)で立て、その下に本文を訳す
 - 段落の区切り・箇条書き・図表キャプションの区切りを原文どおり保つ。前後の文脈がつながって読めることが最優先
 - 文献引用の (Author, year) はそのまま残す(原文の典拠が追えるように)
 - プレビュー等で切れている箇所は「(以降プレビュー未収録)」と明示し、その先を創作しない)

## 重要用語 対訳集
| 日本語 | 原語 | 一言メモ |
|---|---|---|
(この論文を読むうえで鍵になる用語。修論でそのまま使えるように)

## 自分の研究とのつながり
(references/research_context.md を読み、動物のプライバシー意識調査と
 ①どこが直接つながるか ②概念的に橋渡しできるか ③つながらないか を率直に。
 無理に関連づけない。つながりが薄ければ「薄い」と書く)

## 引っかかった点・要確認
(訳に自信のない箇所、原文が曖昧な箇所、プレビューで欠けている箇所)
```

**ファイル名**: `著者姓年_原題_邦題.docx`(原題=英語タイトルを邦題の前に入れる。例: `Rubel2025_Digital Platforms, Privacy, and the Ethics of Wildlife Information Sharing_デジタルプラットフォームと動物のプライバシー.docx`)。ファイル名に使えない記号(`: ? / \ * " < > |`)は「-」等に置換する。連番を付ける場合は先頭に付ける。
**保存先**: ユーザー指定があればそこ。指定が無ければ入力元のPDF/テキストと同じフォルダに保存する。
**.docx の生成手段**: `docx` スキルなど、その環境で使える手段で Word 文書を作る。日本語(CJK)フォントで文字化けしないようにする。生成後は保存パスをユーザーに伝える。

出力後に一度だけ、「このまま literature-review-assistant で文献ノート(Notion用)にしますか？ 対訳表の用語を research-glossary(用語の貯蔵庫)に登録しますか？」と橋渡しを提案する(押し付けない)。

## Step 3: 対訳(バイリンガル)表示 — 依頼時のみ

「原文と並べて」「対訳で」「バイリンガルで」等の依頼時は、(同じく .docx 内に)段落ごとに **原文 → 訳** を交互に並べる。原文を残す分だけ長くなるので、既定にはしない。方法・結果など後で正確に引用したい箇所を突き合わせたいときに使う。

```
> [原文の段落]

[その訳]
```

## 正確さについて

- 分からない語・多義的な箇所を推測で埋めない。「原文では X。文脈により A/B の両義」と示す
- 数値・単位・統計値は改変しない。原文が示していない数値を補完しない
- 原文に無い解釈や評価を、翻訳本体に混ぜない(「自分の研究とのつながり」欄でのみ自分の解釈を書く)

## NotebookLMとの役割分担

NotebookLM = 原文忠実な一次抽出・通勤用オーディオ概要。このスキル = それを日本語で読み解き、研究文脈に接続する。NotebookLMの抽出を入力にしてもよい。

## 著作権・利用範囲

この翻訳は本人の研究・学習のための読解補助であり、再配布・公開用の翻訳ではない。生成物を第三者に配布・公開しないこと。引用時は原文(原語)を出典として用いる。
