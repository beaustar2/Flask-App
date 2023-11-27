from flask import Flask, render_template

app = Flask(__name__)

# Sample data for projects
projects_data = [
    {
        'name': 'CI/CD Pipeline Automation',
        'description': 'Implemented a robust CI/CD pipeline for automating software delivery, improving efficiency, and ensuring consistent deployments.'
    },
    {
        'name': 'Infrastructure as Code (IaC)',
        'description': 'Managed infrastructure using Terraform to achieve infrastructure as code, enabling version-controlled and repeatable infrastructure deployments.'
    }
    # Add more projects as needed
]

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the projects page
@app.route('/projects')
def projects():
    return render_template('projects.html', projects_data=projects_data)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
