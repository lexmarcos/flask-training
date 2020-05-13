from database import Database
from models.blog import Blog
from models.menu import Menu
from models.post import Post

Database.initialize()

menu = Menu()

menu.run_menu()