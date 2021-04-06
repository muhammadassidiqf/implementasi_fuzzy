import streamlit
from main import Main
from apps import home, function, fuzzy

app = Main()

app.add_app("Home", home.app)
app.add_app("Fuzzy Logic", fuzzy.app)
app.add_app("Function", function.app)

app.run()