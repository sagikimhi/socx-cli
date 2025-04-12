from .app import SoCX

app = None


def main():
    global app

    if app is None:
        app = SoCX()

    app.run()


if __name__ == "__main__":
    main()
