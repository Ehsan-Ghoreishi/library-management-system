import json

from mylibrary import Library, storage


def test_round_trip(tmp_path, library):
    library.borrow_book("Dune")
    path = tmp_path / "library.json"

    storage.save(library, path)
    loaded = storage.load(path)

    assert loaded.books == library.books


def test_load_missing_file_returns_empty_library(tmp_path):
    assert len(storage.load(tmp_path / "missing.json")) == 0


def test_save_writes_versioned_json(tmp_path, library):
    path = tmp_path / "library.json"
    storage.save(library, path)

    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["version"] == storage.FORMAT_VERSION
    assert [b["title"] for b in payload["books"]] == ["Dune", "The Hobbit"]


def test_save_creates_parent_dirs_and_leaves_no_temp_files(tmp_path, library):
    path = tmp_path / "nested" / "library.json"
    storage.save(library, path)
    assert [p.name for p in path.parent.iterdir()] == ["library.json"]


def test_save_preserves_unicode(tmp_path):
    lib = Library()
    lib.add_book("شاهنامه", "فردوسی")
    path = tmp_path / "library.json"
    storage.save(lib, path)

    assert "شاهنامه" in path.read_text(encoding="utf-8")
    assert storage.load(path).get_book("شاهنامه").author == "فردوسی"
