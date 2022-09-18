from flask import *
from pandas.tseries.holiday import USFederalHolidayCalendar

app = Flask(__name__, template_folder="templates")

blog1 = {"content": "This is amazing!", "title": "Clickbait", "ID":0}
blog2 = {"content": "How does he do it?", "title": "Franchy Cordero", "ID":1}
blog_list = [blog1, blog2]


@app.route("/")
def homePage():
    holidays = USFederalHolidayCalendar().rules
    events = [(holiday.name, holiday.month, holiday.day) for holiday in holidays]
    return render_template("home.html", events=events)


@app.route("/second")
def secondPage():
    return render_template("secondPage.html")


@app.route("/blog")
def blogPage():
    return render_template("blogPage.html", blogs=blog_list)


@app.route("/viewBlog/<blog_id>")
def viewBlog(blog_id):
    for blog in blog_list:
        if blog["ID"] == int(blog_id):
            return render_template("view_blog.html", blog=blog)

if __name__ == '__main__':
    app.debug = False
    app.run(host='127.0.0.1', port=4020)
