from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.2aaoy6w.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
#'mongodb+srv://test:sparta@cluster0.8rxfxpr.mongodb.net/Cluster0?retryWrites=true&w=majority'

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/mskpost/", methods=["POST"])
def homework_post():
    nickname_receive = request.form['nickname_give']
    url_receive = request.form['url_give']
    area_receive = request.form['area_give']
    image_receive = request.form['image_give']
    place_receive = request.form['place_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    doc = {
        'nickname': nickname_receive,
        'url': url_receive,
        'area': area_receive,
        'image': image_receive,
        'place':place_receive,
        'star':star_receive,
        'comment': comment_receive
    }

    db.mypost.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route("/mskpost", methods=["GET"])
def mypost_get():
    mypost_list = list(db.mypost.find({},{'_id':False}))

    return jsonify({'myposts': mypost_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)