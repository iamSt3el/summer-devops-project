from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority')
    
    if title:
        tasks = load_tasks()
        new_task = {
            'id': len(tasks) + 1,
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'pending',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        tasks.append(new_task)
        save_tasks(tasks)
    
    return redirect(url_for('index'))

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = request.form.get('status', task['status'])
            break
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/api/tasks')
def api_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)