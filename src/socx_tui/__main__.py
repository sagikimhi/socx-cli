from .app import SoCX


app = SoCX()


def main() -> int:
    return app.run() or 0


if __name__ == "__main__":
    main()
