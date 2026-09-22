pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bhawanaraj05-commits/flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Deploy Flask') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
