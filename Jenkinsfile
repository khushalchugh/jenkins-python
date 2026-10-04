pipeline {
    agent any

    stages {
        stage('Download Code'){
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t jenkins-app .'
            }
        stage('Run Container'){
            steps{
                sh "docker rm -f running-jenkins-app || true"
                sh "docker run -d -p 2000:5000 --name running-jenkins-app jenkins-app"
            }
        }
        }
    }
}