from Backend.app import create_app

app = create_app(config='config.py')
app.run()
