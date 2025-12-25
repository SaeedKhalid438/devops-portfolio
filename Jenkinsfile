pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/SaeedKhalid438/devops-portfolio.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t portfolio-app .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 5000:5000 portfolio-app || true'
            }
        }
    }
}
