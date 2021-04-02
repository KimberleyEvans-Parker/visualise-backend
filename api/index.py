from app import app


def test(name: str) -> str:
    return f"Hello there, {name}!"


@app.route("/", methods=["GET"])
def index() -> str:
    return test("Obi-Wan Kenobi")