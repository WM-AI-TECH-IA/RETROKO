from datetime import datetime, timezone
from pathlib import Path
from tempfile import NamedTemporaryFile


def generate_log():
    directory = Path("logs/render")
    directory.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    with NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=directory,
        prefix=f"{timestamp}-", suffix=".log", delete=False,
    ) as output:
        output.write("==> RENDER  LOG SIMULED... ")
    return str(directory / Path(output.name).name)


if __name__ == "__main__":
    print(f"Fichier log structuré : {generate_log()}")
