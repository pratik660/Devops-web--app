pipeline {
    agent any

    stages {
        stage('Build & Run') {
    steps {
        sh 'docker-compose down'
        sh 'docker-compose up --build -d'
    }
}

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }
    }
}