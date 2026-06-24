pipeline {

    agent any

    environment {
        IMAGE = "YOUR_DOCKERHUB_USERNAME/devops-webapp"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'YOUR_GITHUB_REPO'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $IMAGE:latest ./backend'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {

                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push $IMAGE:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}