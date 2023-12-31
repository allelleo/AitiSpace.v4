import typer

from app import config

app = typer.Typer()


@app.command()
def run(host: str = config.HOST, port: int = config.PORT):
    import uvicorn
    from app import app
    uvicorn.run(app, host=host, port=port)


@app.command()
def test(): print('test!')


if __name__ == '__main__':
    app()
