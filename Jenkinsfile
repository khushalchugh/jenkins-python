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
        }
    }
}