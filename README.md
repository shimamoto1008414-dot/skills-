# skills-

自分専用スキル集の置き場（source of truth）。各スキルは `SKILL.md`＋`references/` で
構成され、claude.ai にアップロードして使う。修正・追加は Claude Code の
`skill-creator` 経由で行う。

- **claude.ai で発動** … claude.ai のスキル設定にアップロード＆有効化したものが、
  会話の内容に応じて自動発動する。
- **Claude Code で発動** … `.claude/skills/` に置いたスキルのみ自動ロードされる
  （`Academic/` `work/` `personal/` は保管用で、Claude Code の自動対象ではない）。

> 下の一覧は `scripts/gen_readme.py` が自動生成する。スキルを増やしたら
> 再生成される（コミット時に `.githooks/pre-commit` が実行）。手で書き換えないこと。

<!-- SKILLS:START -->

## スキル一覧（現在 **13** スキル）

### 📚 Academic（大学院・研究）

| スキル | 場所 | 何をする |
|---|---|---|
| `academic-document-formatter` | `Academic/academic-document-formatter` | 大学院の研究・ゼミ活動における「自分が作る文書」のフォーマッター。 |
| `academic-paper-translator` | `Academic/academic-paper-translator` | 英語論文を、段落構造を保ったまま省略なしで日本語に全文翻訳するスキル。 |
| `advisor-meeting-logger` | `Academic/advisor-meeting-logger` | ゼミ発表や個別指導(太田先生との面談など)で受けた指摘・コメントを、固定フォーマットの 日本語記録(Notion貼り付け用のプロパティ表+ページ本文)に変換し、TODOの対応状況を 蓄積・追跡するスキル。 |
| `literature-review-assistant` | `Academic/literature-review-assistant` | Turn academic papers, book chapters, reports, review articles, or NotebookLM summaries into a fixed-format Japanese literature-review note ready to paste into Notion (property table plus page body) for graduate thesis research. |
| `literature-scout` | `Academic/literature-scout` | 先生・ゼミから「〜についてまとめて」「〜を調べて」のような課題・コメントを 受けたときの動き方を案内し、読むべき本・論文のリストを設計して、論文は Web 検索で 収集(書誌・入手リンク)、本は大阪大学図書館(OPAC)の所蔵館・配架場所・請求記号まで 調べるスキル。 |
| `research-glossary` | `Academic/research-glossary` | 論文や授業で出会った知らない用語・概念を、意味の説明と同時に蓄積用エントリに 変換して貯めていく「知識の貯蔵庫」スキル。 |

### 🏗 work（仕事・道路設計）

| スキル | 場所 | 何をする |
|---|---|---|
| `cad-workflow-notes` | `work/cad-workflow-notes` | CAD・Civil 3D・AutoCAD の操作・設定・トラブル解決を「一度調べたら二度調べない」 ための手順書に変換・蓄積するスキル。 |
| `homepage-companion` | `work/homepage-companion` | ホームページ（HP・Webサイト）作りを、企画・構成の立案から、制作、公開、そして公開後の保守・メンテナンス・ページ追加まで、初心者に最後まで寄り添って伴走するスキル。 |
| `meeting-record-keeper` | `work/meeting-record-keeper` | 仕事(道路設計業務)の打合せ・協議・電話連絡の内容を、建設コンサル実務の形式 (協議記録・打合せ簿)で記録し、宿題事項の対応状況を追跡するスキル。 |
| `work-report-writer` | `work/work-report-writer` | 日々の走り書き・作業メモ・口頭の報告から、仕事(道路設計業務)の週報・月報・ 作業状況報告を定型フォーマットで生成するスキル。 |

### 🗂 personal（横断）

| スキル | 場所 | 何をする |
|---|---|---|
| `task-triage` | `personal/task-triage` | 仕事(道路設計業務)・大学院・私用のタスクを横断で整理するスキル。 |

### 🧩 other（その他）

| スキル | 場所 | 何をする |
|---|---|---|
| `dual-model-executor-advisor` | `other/dual-model-executor-advisor` | 実行役モデルと相談役モデルの 2 モデル体制で作業を進めるためのスキル。 |

### ⚙️ 管理用（Claude Code 上で使う）

| スキル | 場所 | 何をする |
|---|---|---|
| `skill-creator` | `.claude/skills/skill-creator` | このリポジトリで新しいスキルを作成したり、既存スキルを改善・修正したりするためのスキル。 |

<!-- SKILLS:END -->
