from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

languages = [
    {'id': 'js', 'name': 'JavaScript', 'details': 'JavaScript is a versatile language used for both client-side and server-side development.', 'image': 'https://static.vecteezy.com/system/resources/previews/027/127/463/original/javascript-logo-javascript-icon-transparent-free-png.png'},
    {'id': 'html', 'name': 'HTML', 'details': 'HTML is the standard markup language for creating web pages.', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/2048px-HTML5_logo_and_wordmark.svg.png'},
    {'id': 'css', 'name': 'CSS', 'details': 'CSS is used to style and layout web pages.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTO5ryTY9VShCV5uJWhoBXkcxxlFB8O5bbxGA&s'},
    {'id': 'python', 'name': 'Python', 'details': 'Python is widely used in data science for its simplicity and powerful libraries.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxe6IR3EKgALq0lEUvpW3GmPH8rpAv1cK0_w&s'},
    {'id': 'sql', 'name': 'SQL', 'details': 'SQL is used to manage and manipulate relational databases.', 'image': 'https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/sql/sql.png'},
    {'id': 'kotlin', 'name': 'Kotlin', 'details': 'Kotlin is a modern language that interoperates fully with Java and is used for Android development.', 'image': 'https://global.discourse-cdn.com/business5/uploads/kotlinlang/original/2X/f/f440c5115af253e7b8dfdd241a45ccb8e494e8a6.png'},
    {'id': 'swift', 'name': 'Swift', 'details': 'Swift is a powerful language for iOS and macOS app development.', 'image': 'https://logowik.com/content/uploads/images/558_swift_logo_icon.jpg'},
    {'id': 'java', 'name': 'Java', 'details': 'Java is a popular language for developing Android apps.', 'image': 'https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/181_Java_logo_logos-512.png'},
    {'id': 'cpp', 'name': 'C++', 'details': 'C++ is used for high-performance game development.', 'image': 'https://w7.pngwing.com/pngs/46/626/png-transparent-c-logo-the-c-programming-language-computer-icons-computer-programming-source-code-programming-miscellaneous-template-blue.png'},
    {'id': 'csharp', 'name': 'C#', 'details': 'C# is used with the Unity game engine for developing games.', 'image': 'https://w7.pngwing.com/pngs/498/19/png-transparent-csharp-original-logo-icon-thumbnail.png'},
    {'id': 'unity', 'name': 'Unity', 'details': 'Unity is a cross-platform game engine used to create games.', 'image': 'https://i.redd.it/tu3gt6ysfxq71.png'},
    {'id': 'go', 'name': 'Go', 'details': 'Go is used for building efficient and scalable software.', 'image': 'https://go.dev/blog/go-brand/Go-Logo/PNG/Go-Logo_Blue.png'},
    {'id': 'ruby', 'name': 'Ruby', 'details': 'Ruby is used for infrastructure automation and web development.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuuyAOtgff9NktWrFHcQPcnW_xKh6wQn8UaQ&s'}
]

field_preferences = {
    'Web Development': ['js', 'html', 'css'],
    'Data Science': ['python', 'sql'],
    'Mobile Development': ['kotlin', 'swift', 'java'],
    'Game Development': ['cpp', 'csharp', 'unity'],
    'DevOps': ['python', 'go', 'ruby']
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    learned_lang = request.form.get('learnedLang')
    field = request.form.get('field')
    preferred_lang_ids = field_preferences.get(field, []) # type: ignore
    preferred_langs = [lang for lang in languages if lang['id'] in preferred_lang_ids]
    other_langs = [lang for lang in languages if lang['id'] not in preferred_lang_ids]
    
    return render_template('recommendations.html', preferred_langs=preferred_langs, other_langs=other_langs)

@app.route('/details')
def details():
    name = request.args.get('name')
    details = request.args.get('details')
    image = request.args.get('image')
    return render_template('details.html', name=name, details=details, image=image)

if __name__ == '__main__':
    app.run(debug=True)
