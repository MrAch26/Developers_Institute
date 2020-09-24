
from flask import Flask, render_template
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/lesson')
def lesson():
    readme_file = open("templates/in-this-chapter.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions=["fenced_code", "codehilite"])

    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()

    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template


@app.route('/exe')
def exe():
    readme_file = open("templates/exercises.md", "r")
    md_template_string = markdown.markdown(readme_file.read(), extensions=["fenced_code", "codehilite"])

    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()

    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template

def main():
    print('hey siri')
    app.run(debug=True)


if __name__ == '__main__':
    main()