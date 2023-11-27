pipeline {
    agent any

    environment {
        ANSIBLE_HOSTS_FILE = 'customizedhosts.ini'
        ANSIBLE_PLAYBOOK = 'deploy-flaskapp.yml'
        VENV_PATH = 'venv'
        TEST_SCRIPT = 'test.py'
        EMAIL_RECIPIENT = 'your_email@example.com'  // Set your recipient email address here
        FLASK_APP = 'app.py'
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
                    // Checkout the code from your version control system (e.g., Git)
                    git branch: 'main', url: 'https://github.com/beaustar2/Flask-App.git'
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Set up a virtual environment
                    sh "python -m venv /home/ubuntu/Flask-App/flask_env"
                    sh "source /home/ubuntu/Flask-App/flask_env/bin/activate"
                    sh "pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests using pytest
                    sh "pytest test.py"
                }
            }
        }

        stage('Prepare Ansible Inventory') {
            steps {
                script {
                    // Create an Ansible inventory file with server details
                    writeFile file: ANSIBLE_HOSTS_FILE, text: '''
                        [webservers]
                        n1 ansible_host=172.31.2.80 ansible_user=ubuntu ansible_ssh_private_key_file=/home/ubuntu/kiki.pem ansible_ssh_common_args='-o StrictHostKeyChecking=no'
                        n2 ansible_host=172.31.14.165 ansible_user=ec2-user ansible_ssh_private_key_file=/home/ubuntu/kiki.pem ansible_ssh_common_args='-o StrictHostKeyChecking=no'
                    '''
                }
            }
        }

        stage('Deploy with gunicorn') {
            steps {
                script {
                    // Run the Ansible playbook to deploy the Flask app
                    sh "ansible-playbook -i customizedhosts.ini deploy-flaskapp.yaml"
                }
            }
        }
    }

    post {
        success {
            emailext subject: 'Flask App Tests Passed and Deployment Successful',
                      body: 'The Flask App tests passed, and the deployment was successful.',
                      recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                      to: EMAIL_RECIPIENT
        }

        failure {
            emailext subject: 'Flask App Tests Failed or Deployment Failed',
                      body: 'The Flask App tests failed, or the deployment failed. Please check the Jenkins build for details.',
                      recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                      to: EMAIL_RECIPIENT
        }

        always {
            // Clean up temporary Ansible inventory file
            deleteFile ANSIBLE_HOSTS_FILE

            // Deactivate the virtual environment
            sh "deactivate"
        }
    }
}
