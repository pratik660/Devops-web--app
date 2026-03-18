pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/<your-username>/<repo>.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up --build -d'
            }
        }

        stage('Test') {
            steps {
                sh 'curl http://localhost:5000'
            }
        }
    }
}