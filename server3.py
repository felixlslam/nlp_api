import connexion

app = connexion.App(__name__, specification_dir='swagger/', options={"swagger_ui": True})
app.add_api('api.yaml')
app.run(port=8080)
