#!/usr/bin/env python3
"""スキル一覧を README.md に自動生成するスクリプト。

リポジトリ内の全 SKILL.md を走査し、フロントマターの name / description から
スキル一覧テーブルを作って README.md の下記マーカー間を書き換える:

    <!-- SKILLS:START -->
    ... 自動生成 ...
    <!-- SKILLS:END -->

README.md やマーカーが無ければ、既定のひな形ごと作成する。
スキルを増やしたら `python3 scripts/gen_readme.py` を実行すれば一覧が更新される
(コミット時は .githooks/pre-commit が自動で実行する)。
"""

from __future__ import annotations

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
START = "<!-- SKILLS:START -->"
END = "<!-- SKILLS:END -->"

# 場所(トップ階層) → 表示見出し。列挙順がそのまま README の並び順になる。
CATEGORIES: list[tuple[str, str]] = [
    ("Academic", "📚 Academic（大学院・研究）"),
    ("work", "🏗 work（仕事・道路設計）"),
    ("personal", "🗂 personal（横断）"),
    ("other", "🧩 other（その他）"),
    (".claude/skills", "⚙️ 管理用（Claude Code 上で使う）"),
]

INTRO = """# skills-

自分専用スキル集の置き場（source of truth）。各スキルは `SKILL.md`＋`references/` で
構成され、claude.ai にアップロードして使う。修正・追加は Claude Code の
`skill-creator` 経由で行う。

- **claude.ai で発動** … claude.ai のスキル設定にアップロード＆有効化したものが、
  会話の内容に応じて自動発動する。
- **Claude Code で発動** … `.claude/skills/` に置いたスキルのみ自動ロードされる
  （`Academic/` `work/` `personal/` は保管用で、Claude Code の自動対象ではない）。

> 下の一覧は `scripts/gen_readme.py` が自動生成する。スキルを増やしたら
> 再生成される（コミット時に `.githooks/pre-commit` が実行）。手で書き換えないこと。
"""


def load_skill(skill_md: pathlib.Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        raise ValueError(f"フロントマターが見つからない: {skill_md}")
    meta = yaml.safe_load(m.group(1)) or {}
    if "name" not in meta or "description" not in meta:
        raise ValueError(f"name/description が無い: {skill_md}")
    return meta


def first_sentence(desc: str) -> str:
    """description の 1 文目を要約として抜き出す（日本語「。」/ 英語 ". " 対応）。"""
    desc = " ".join(str(desc).split())
    cut = len(desc)
    ja = desc.find("。")
    if ja != -1:
        cut = min(cut, ja + 1)
    en = desc.find(". ")
    if en != -1:
        cut = min(cut, en + 1)
    return desc[:cut].strip()


def category_of(rel: pathlib.PurePath) -> str:
    parts = rel.parts
    if len(parts) >= 2 and parts[0] == ".claude" and parts[1] == "skills":
        return ".claude/skills"
    return parts[0]


def collect() -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for skill_md in sorted(ROOT.rglob("SKILL.md")):
        if ".git" in skill_md.parts:
            continue
        rel = skill_md.relative_to(ROOT).parent
        meta = load_skill(skill_md)
        cat = category_of(rel)
        groups.setdefault(cat, []).append(
            {
                "name": meta["name"],
                "path": str(rel),
                "summary": first_sentence(meta["description"]),
            }
        )
    for items in groups.values():
        items.sort(key=lambda s: s["name"])
    return groups


def render(groups: dict[str, list[dict]]) -> str:
    total = sum(len(v) for v in groups.values())
    lines = [START, "", f"## スキル一覧（現在 **{total}** スキル）", ""]
    known = {key for key, _ in CATEGORIES}
    ordered = list(CATEGORIES) + [
        (k, k) for k in sorted(groups) if k not in known
    ]
    for key, heading in ordered:
        items = groups.get(key)
        if not items:
            continue
        lines.append(f"### {heading}")
        lines.append("")
        lines.append("| スキル | 場所 | 何をする |")
        lines.append("|---|---|---|")
        for s in items:
            lines.append(f"| `{s['name']}` | `{s['path']}` | {s['summary']} |")
        lines.append("")
    lines.append(END)
    return "\n".join(lines)


def main() -> int:
    groups = collect()
    block = render(groups)

    readme = ROOT / "README.md"
    if readme.exists():
        content = readme.read_text(encoding="utf-8")
    else:
        content = INTRO + "\n" + START + "\n" + END + "\n"

    if START in content and END in content:
        new = re.sub(
            re.escape(START) + r".*?" + re.escape(END),
            block,
            content,
            flags=re.DOTALL,
        )
    else:
        new = content.rstrip() + "\n\n" + block + "\n"

    if new != content:
        readme.write_text(new, encoding="utf-8")
        print(f"README.md 更新: {sum(len(v) for v in groups.values())} スキル")
    else:
        print("README.md 変更なし")
    return 0


if __name__ == "__main__":
    sys.exit(main())
