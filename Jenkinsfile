pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\SHREYA PATIL\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" --version'
            }
        }

        stage('Run Grade Calculator') {
            steps {
                bat '"C:\\Users\\SHREYA PATIL\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" grades.py'
            }
        }
    }
}
