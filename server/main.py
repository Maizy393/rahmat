
from flask import Flask, jsonify

app = Flask(__name__)

companies = [
    {
        "id": 1,
        "name": "Яндекс",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://yandex.ru",
        "icon": "https://yastatic.net/q/logoaas/v2/Яндекс.svg"
    },
    {
        "id": 2,
        "name": "Google",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://google.com",
        "icon": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    },
    {
        "id": 3,
        "name": "Microsoft",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://microsoft.com",
        "icon": "https://cdn.worldvectorlogo.com/logos/microsoft-1.svg"
    },
    {
        "id": 4,
        "name": "Apple",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://apple.com",
        "icon": "https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png"
    },
    {
        "id": 5,
        "name": "Amazon",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://amazon.com",
        "icon": "https://www.amazon.com/favicon.ico"
    },
    {
        "id": 6,
        "name": "Tesla",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://tesla.com",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Tesla_logo.png"
    },
    {
        "id": 7,
        "name": "Meta (Facebook)",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://meta.com",
        "icon": "https://s.yimg.com/ny/api/res/1.2/Zsye8aWPagBxmZI9AObv3g--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD0xMjAw/https://media.zenfs.com/en/us.finance.gurufocus/54d02e123f2e903e8c3e4b08ecead8dd"
    },
    {
        "id": 8,
        "name": "Netflix",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://netflix.com",
        "icon": "https://avatars.mds.yandex.net/i?id=608a50e0b7b73068a924f29a6f29dc9ab4eda3e5-12941940-images-thumbs&n=13"
    },
    {
        "id": 9,
        "name": "Spotify",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://spotify.com",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1024px-Spotify_logo_without_text.svg.png"
    },
    {
        "id": 10,
        "name": "Twitter (X)",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://twitter.com",
        "icon": "https://abs.twimg.com/favicons/twitter.3.ico"
    },
    {
        "id": 11,
        "name": "GitHub",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://github.com",
        "icon": "https://github.githubassets.com/favicons/favicon-dark.png"
    },
    {
        "id": 12,
        "name": "LinkedIn",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://linkedin.com",
        "icon": "https://static.licdn.com/sc/h/akt4ae504epesldzj74dzred8"
    },
    {
        "id": 13,
        "name": "Adobe",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://adobe.com",
        "icon": "https://yt3.googleusercontent.com/rYlsxUeod34MzuD-oa12KKiwmd2HNLKwESS0ad4gbk46-vodHtTizyc-zD_tNmnaapvJVBvb=s900-c-k-c0x00ffffff-no-rj"
    },
    {
        "id": 14,
        "name": "Uber",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://uber.com",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Uber_logo_2018.svg/1200px-Uber_logo_2018.svg.png"
    },
    {
        "id": 15,
        "name": "Airbnb",
        "tags": ["работа", "ворк", "работа не волк", "работа ворк"],
        "ref": "https://airbnb.com",
        "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/1200px-Airbnb_Logo_B%C3%A9lo.svg.png"
    }
]

@app.route('/employers', methods=['GET'])
def get_employers():
    return jsonify(companies)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)