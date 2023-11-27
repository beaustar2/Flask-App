pipeline {
    agent any

    environment {
        ANSIBLE_HOSTS_FILE = 'customizedhosts.ini'
        ANSIBLE_PLAYBOOK = 'deploy-flaskapp.yml'
        VENV_PATH = 'venv'
        TEST_SCRIPT = 'test.py'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from your version control system (e.g., Git)
                    checkout scm
                }
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Set up a virtual environment
                    sh "python -m venv ${VENV_PATH}"
                    sh "source ${VENV_PATH}/bin/activate"
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

        stage('Deploy with Ansible') {
            steps {
                script {
                    // Run the Ansible playbook to deploy the Flask app
                    sh "ansible-playbook -i customizedhosts.ini deploy-flaskapp.yaml"
                }
            }
        }
    }

    post {
        always {
            // Clean up temporary Ansible inventory file
            deleteFile customizedhosts.ini

            // Deactivate the virtual environment
            sh "deactivate"
        }
    }
}
