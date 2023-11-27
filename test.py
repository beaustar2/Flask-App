import pytest
from flask import Flask, render_template
from flask.testing import FlaskClient

from app import app, projects_data

projects_data = [
    {"name": "Software Development Life Cycle (SDLC)", "description": "Description for SDLC project."},
    {"name": "Docker Containerization", "description": "Description for Docker Containerization project."},
    # Add more project data as needed
]

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_home_route(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Our DevOps Journey!' in response.data
    assert b'Projects' in response.data  # Check that the "Projects" link is present in the Bootstrap navigation
    assert b'navbar-toggler-icon' in response.data  # Check for the presence of the navbar toggle icon

def test_about_route(client: FlaskClient):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About' in response.data
    assert b'Projects' in response.data  # Check that the "Projects" link is present in the Bootstrap navigation for other routes
    assert b'Projects' not in response.data.decode('utf-8').split('Projects')[0].encode('utf-8')  # Check that the "Projects" link is not present in the current route
    assert b'navbar-toggler-icon' in response.data  # Check for the presence of the navbar toggle icon

def test_contact_route(client: FlaskClient):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact' in response.data
    assert b'Projects' in response.data  # Check that the "Projects" link is present in the Bootstrap navigation for other routes
    assert b'Projects' not in response.data.decode('utf-8').split('Projects')[0].encode('utf-8')  # Check that the "Projects" link is not present in the current route
    assert b'navbar-toggler-icon' in response.data  # Check for the presence of the navbar toggle icon

def test_nonexistent_route(client: FlaskClient):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'Not Found' in response.data
