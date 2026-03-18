pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/pratik660/Devops-web--app.git'
            }
        }

        stage('Build Containers') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose up --build -d'
            }
        }

        stage('Verify') {
            steps {
                bat 'docker ps'
            }
        }
    }
}