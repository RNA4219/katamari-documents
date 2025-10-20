"""Birdseye JSON を最新化するユーティリティ。"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, DefaultDict, Iterable, List, Sequence, Set, Tuple


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh Birdseye JSON metadata.")
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("docs/birdseye"),
        help="Birdseye JSON が存在するディレクトリ",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="変更点を表示するがファイルは更新しない",
    )
    return parser.parse_args(argv)


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _dump_json(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def _serialize(data: Any) -> str:
    return json.dumps(data, sort_keys=True, ensure_ascii=False)


def _current_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _build_edge_maps(edges: Iterable[Tuple[str, str]]) -> Tuple[DefaultDict[str, Set[str]], DefaultDict[str, Set[str]]]:
    outgoing: DefaultDict[str, Set[str]] = defaultdict(set)
    incoming: DefaultDict[str, Set[str]] = defaultdict(set)
    for source, target in edges:
        outgoing[source].add(target)
        incoming[target].add(source)
    return outgoing, incoming


def _normalize_edges(raw_edges: Iterable[Any]) -> List[Tuple[str, str]]:
    normalized: List[Tuple[str, str]] = []
    for item in raw_edges:
        if not isinstance(item, list | tuple) or len(item) != 2:
            continue
        source, target = item
        normalized.append((str(source), str(target)))
    return normalized


def _apply_if_changed(path: Path, before: str, data: Any, dry_run: bool, changed: List[Path]) -> None:
    after = _serialize(data)
    if before == after:
        return
    if dry_run:
        print(f"[DRY-RUN] {path}")
    else:
        _dump_json(path, data)
        print(f"Updated {path}")
    changed.append(path)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    docs_dir: Path = args.docs_dir
    dry_run: bool = args.dry_run

    timestamp = _current_timestamp()
    changed: List[Path] = []

    index_path = docs_dir / "index.json"
    index_data = _load_json(index_path)
    index_before = _serialize(index_data)
    edges = _normalize_edges(index_data.get("edges", []))
    index_data["generated_at"] = timestamp
    _apply_if_changed(index_path, index_before, index_data, dry_run, changed)

    outgoing, incoming = _build_edge_maps(edges)

    caps_dir = docs_dir / "caps"
    for cap_path in sorted(caps_dir.glob("*.json")):
        cap_data = _load_json(cap_path)
        cap_before = _serialize(cap_data)
        node_id = str(cap_data.get("id", ""))
        cap_data["generated_at"] = timestamp
        cap_data["deps_out"] = sorted(outgoing.get(node_id, set()))
        cap_data["deps_in"] = sorted(incoming.get(node_id, set()))
        _apply_if_changed(cap_path, cap_before, cap_data, dry_run, changed)

    hot_path = docs_dir / "hot.json"
    hot_data = _load_json(hot_path)
    hot_before = _serialize(hot_data)
    hot_data["generated_at"] = timestamp
    _apply_if_changed(hot_path, hot_before, hot_data, dry_run, changed)

    action = "would change" if dry_run else "updated"
    print(f"{len(changed)} file(s) {action}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
