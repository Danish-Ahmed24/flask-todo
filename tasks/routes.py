from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector
from db import get_db_connection

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks')
def task_list():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template('tasks.html', tasks=tasks)

    except mysql.connector.Error:
        return render_template(
            'error.html',
            message='Could not load tasks. Please try again later.'
        ), 500


@tasks_bp.route('/tasks/create', methods=['POST'])
def create_task():
    title = request.form['title'].strip()

    if not title:
        flash('Task title cannot be empty.')
        return redirect(url_for('tasks.task_list'))

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))

        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error:
        flash('Could not save the task. Please try again later.')

    return redirect(url_for('tasks.task_list'))


@tasks_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))

        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error:
        flash('Could not delete the task. Please try again later.')

    return redirect(url_for('tasks.task_list'))