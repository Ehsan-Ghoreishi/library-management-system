import pytest

from mylibrary import cli, storage


def run_with_inputs(path, *inputs):
    answers = iter(inputs)
    cli.run(path, prompt=lambda _: next(answers))


def test_add_and_borrow_persist(tmp_path, capsys):
    path = tmp_path / "library.json"
    run_with_inputs(path, "1", "Dune", "Frank Herbert", "5", "dune", "7")

    out = capsys.readouterr().out
    assert "'Dune' was added" in out
    assert "You borrowed 'Dune'" in out
    assert not storage.load(path).get_book("Dune").available


def test_errors_are_reported_not_raised(tmp_path, capsys):
    run_with_inputs(tmp_path / "library.json", "2", "Missing", "7")
    assert "Error: 'Missing' was not found" in capsys.readouterr().out


def test_invalid_choice(tmp_path, capsys):
    run_with_inputs(tmp_path / "library.json", "99", "7")
    assert "Invalid choice" in capsys.readouterr().out


def test_read_only_actions_do_not_create_file(tmp_path):
    path = tmp_path / "library.json"
    run_with_inputs(path, "4", "3", "x", "7")
    assert not path.exists()


def test_eof_exits_cleanly(tmp_path, capsys):
    def prompt(_):
        raise EOFError

    cli.run(tmp_path / "library.json", prompt=prompt)
    assert "Goodbye!" in capsys.readouterr().out


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc:
        cli.main(["--version"])
    assert exc.value.code == 0
    assert "mylibrary" in capsys.readouterr().out
