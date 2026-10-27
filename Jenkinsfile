pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Downloading project from GitHub'
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Grade Calculator') {
            steps {
                bat 'python grades.py'
            }
        }
    }
}
