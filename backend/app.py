from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

# 模拟数据库，这里使用一个简单的列表来存储文章
posts = []

# 文章的 ID 计数器
post_id_counter = 1

# 处理根路径请求，返回一个简单的欢迎信息
@app.route('/')
def index():
    return "Welcome to the Blog API!"

# 处理 favicon.ico 请求，返回一个默认的图标文件
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# 获取所有文章的 API
@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# 创建新文章的 API
@app.route('/api/posts', methods=['POST'])
def create_post():
    global post_id_counter
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content are required'}), 400
    new_post = {
        'id': post_id_counter,
        'title': data['title'],
        'content': data['content'],
        'created_at': '2025-02-23'  # 这里简单固定日期，实际应用中应使用动态日期
    }
    posts.append(new_post)
    post_id_counter += 1
    return jsonify(new_post), 201

# 更新文章的 API
@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Title and content are required'}), 400
    for post in posts:
        if post['id'] == post_id:
            post['title'] = data['title']
            post['content'] = data['content']
            return jsonify(post), 200
    return jsonify({'error': 'Post not found'}), 404

# 删除文章的 API
@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            del posts[index]
            return jsonify({'message': 'Post deleted successfully'}), 200
    return jsonify({'error': 'Post not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)