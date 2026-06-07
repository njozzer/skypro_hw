import pytest

from src import decorators


def test_decorators(capsys: pytest.CaptureFixture[str]) -> None:
    @decorators.log()
    def test_func(x: float, y: float) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(12.0, 0.0)
    captured = capsys.readouterr()
    assert "test_func: Error" in captured.out


def test_decorators_1() -> None:
    @decorators.log(filename="logger.txt")
    def test_func(x: float, y: float) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(12.0, 0.0)
    with open("logger.txt", "r") as file:
        file_contents = file.read()
        assert "test_func: Error" in file_contents


def test_decorators_2() -> None:
    @decorators.log(filename="logger2.txt")
    def test_func(x: float, y: float) -> float:
        return x / y

    assert test_func(12.0, 3.0) == 4.0


def test_decorators_3() -> None:
    @decorators.log()
    def test_func(x: float, y: float) -> float:
        return x / y

    test_func(12.0, 3.0)
    assert test_func(12.0, 3.0) == 4.0
