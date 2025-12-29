from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Set


def extract_username(obj: dict) -> str | None:
    """
    Instagram export objects sometimes put the username in:
      - obj["string_list_data"][0]["value"]   (followers_1.json)
      - obj["title"]                          (following.json)
    """
    # 1) Try the common followers format
    sld = obj.get("string_list_data")
    if isinstance(sld, list) and sld:
        v = sld[0].get("value")
        if isinstance(v, str) and v.strip():
            return v.strip()

    # 2) Fallback to title (common in following.json)
    t = obj.get("title")
    if isinstance(t, str) and t.strip():
        return t.strip()

    return None


def load_followers(path: Path) -> List[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    out: List[str] = []
    for item in data:
        u = extract_username(item)
        if u:
            out.append(u)
    return out


def load_following(path: Path) -> List[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rel = data.get("relationships_following", [])
    out: List[str] = []
    for item in rel:
        u = extract_username(item)
        if u:
            out.append(u)
    return out


def main() -> None:
    # Put the json files in the same folder as this script, or update these paths.
    base = Path("/Users/binhnguyen/Downloads/connections")
    
    followers_path = base / "followers_1.json"
    following_path = base / "following.json"

    followers = load_followers(followers_path)
    following = load_following(following_path)

    followers_set: Set[str] = set(followers)

    not_following_back = sorted({u for u in following if u not in followers_set})

    print(f"Followers: {len(followers)}")
    print(f"Following: {len(following)}")
    print(f"Not following back: {len(not_following_back)}\n")

    for u in not_following_back:
        print(u)


if __name__ == "__main__":
    main()
