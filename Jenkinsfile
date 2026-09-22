pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bhawanaraj05-commits/flask-app.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }

stage('Deploy Flask') {
    steps {
        sh 'nohup venv/bin/python app.py > flask.log 2>&1 &'
    }
}
    }
}
