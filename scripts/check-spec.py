#!/usr/bin/env python3
"""Проверки спеки botik-docs (BOT-67). Запуск: python scripts/check-spec.py [--botik ПУТЬ_К_botik]
Код возврата 1 при ошибках пп. 1-5, иначе 0. Без внешних зависимостей."""
import argparse
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
SPEC = DOCS / "spec"
RULE_ROW = re.compile(r"^\|\s*(B\d+A?-\d+)\s*\|", re.M)
RULE_ID = re.compile(r"\bB\d+A?-\d+\b")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.M | re.S)
INLINE = re.compile(r"`[^`\n]*`")
SPEC_TAG = re.compile(r"spec:\s*((?:B\d+A?-\d+[\s,;]*)+)")

errors: list[str] = []
info: list[str] = []


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def find_botik(arg):
    for c in ([Path(arg)] if arg else []) + [DOCS.parent / "botik", Path("C:/Users/user/projects/botik")]:
        if (c / "version.py").exists():
            return c
    return None


def check_links():
    n = 0
    for f in sorted(SPEC.rglob("*.md")):
        if "_templates" in f.relative_to(SPEC).parts:
            continue
        text = INLINE.sub("", FENCE.sub("", read(f)))
        for target in LINK.findall(text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            n += 1
            path = target.split("#")[0]
            if path and not (f.parent / path).resolve().exists():
                errors.append(f"[ссылки] {f.relative_to(DOCS)}: нет файла {target}")
    return n


def check_rules():
    ids: dict[str, str] = {}
    for f in sorted((SPEC / "blocks").glob("*.md")):
        prefixes = set()
        for rid in RULE_ROW.findall(read(f)):
            if rid in ids:
                errors.append(f"[номера] {rid} повторяется ({ids[rid]} и {f.name})")
            ids[rid] = f.name
            prefixes.add(rid.split("-")[0])
        if len(prefixes) > 1:
            errors.append(f"[номера] {f.name}: разные префиксы {sorted(prefixes)}")
    return ids


def code_files(botik: Path):
    for p in botik.rglob("*.py"):
        if any(x in p.parts for x in ("venv", "__pycache__", ".git")):
            continue
        yield p


def check_code_refs(ids, botik):
    n = 0
    used_in_tests = set()
    for p in code_files(botik):
        in_tests = "tests" in p.relative_to(botik).parts
        for i, line in enumerate(read(p).splitlines(), 1):
            m = SPEC_TAG.search(line)
            if not m:
                continue
            for rid in RULE_ID.findall(m.group(1)):
                n += 1
                if rid not in ids:
                    errors.append(f"[код] {p.relative_to(botik)}:{i}: правила {rid} нет в блоках")
                elif in_tests:
                    used_in_tests.add(rid)
    return n, used_in_tests


def check_params_and_affects(ids):
    params = set(re.findall(r"\bP-[A-Z0-9]+(?:-[A-Z0-9]+)*", read(SPEC / "parameters.md")))
    for f in sorted((SPEC / "blocks").glob("*.md")) + [SPEC / "commands.md"]:
        for p in sorted(set(re.findall(r"\bP-[A-Z0-9]+(?:-[A-Z0-9]+)*", read(f)))):
            if p not in params:
                errors.append(f"[параметры] {f.name}: {p} нет в parameters.md")
    for f in sorted((SPEC / "decisions").glob("*.md")):
        for line in read(f).splitlines():
            if not line.startswith("affects:"):
                continue
            value = line[len("affects:"):]
            if "commands.md" in value:
                continue
            found = RULE_ID.findall(value)
            if not found:
                errors.append(f"[affects] {f.name}: нет номеров правил: {value.strip()}")
            for rid in found:
                if rid not in ids:
                    errors.append(f"[affects] {f.name}: правила {rid} нет в блоках")
    return len(params)


def check_release(botik):
    m = re.search(r'^VERSION\s*=\s*"([^"]+)"', read(botik / "version.py"), re.M)
    if not m:
        errors.append("[релиз] не найдена VERSION в version.py")
        return None
    note = botik / "release_notes" / f"v{m.group(1)}.md"
    if not note.exists():
        errors.append(f"[релиз] нет {note.relative_to(botik)} для версии {m.group(1)}")
    return m.group(1)


def check_forbidden(botik):
    g = read(SPEC / "glossary.md")
    m = re.search(r"^#{2,3}\s*(Запрещённые термины|Недопустимые формулировки)[^\n]*\n(.*?)(?=^#{2,3}\s|\Z)", g, re.M | re.S)
    if not m:
        info.append("п. 6 пропущен: в glossary.md нет раздела о недопустимых формулировках")
        return
    terms = [t.strip(" `«»\"") for t in re.findall(r"^\s*[-*|]\s*([^|\n]+)", m.group(2), re.M)]
    files = list((SPEC / "blocks").glob("*.md")) + [botik / "texts.py"]
    for t in filter(None, terms):
        for f in files:
            if t.lower() in read(f).lower():
                errors.append(f"[термины] «{t}» найдено в {f.name}")


def check_map():
    f = DOCS / "tasks" / "60-spec-restructure.md"
    if not f.exists():
        return
    for l in read(f).splitlines():
        m = re.match(r"^\|\s*\d+\s*\|(.*)\|\s*$", l)
        if m and not m.group(1).split("|")[-1].strip():
            errors.append(f"[карта] пустой статус: {l[:70]}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--botik")
    a = ap.parse_args()
    botik = find_botik(a.botik)
    if botik is None:
        print("Не найден репозиторий botik (--botik ПУТЬ)")
        return 1
    links = check_links()
    ids = check_rules()
    refs, tested = check_code_refs(ids, botik)
    params = check_params_and_affects(ids)
    ver = check_release(botik)
    check_forbidden(botik)
    check_map()
    print(f"check-spec: правил {len(ids)}, ссылок {links}, ссылок на правила в коде/тестах {refs}, "
          f"параметров {params}, версия {ver}; ошибок {len(errors)}")
    for e in errors:
        print("ОШИБКА", e)
    for i in info:
        print("INFO", i)
    untested = sorted(set(ids) - tested)
    print(f"INFO правил без упоминаний в тестах: {len(untested)} из {len(ids)}")
    if untested:
        print("  " + ", ".join(untested))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
