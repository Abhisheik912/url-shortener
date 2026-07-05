pipeline {
    agent any

    tools {
        sonarQube 'SonarScanner'
    }

    environment {
        IMAGE_NAME = "abhisheik912/url-shortener"
        PYTHON = "C:\\Users\\Abhisheik\\AppData\\Local\\Python\\bin\\python.exe"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat "\"%PYTHON%\" -m pip install -r requirements.txt"
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat "\"%PYTHON%\" -m pytest"
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Local sonar') {
                    bat 'sonar-scanner'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:latest ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat """
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker push %IMAGE_NAME%:latest
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                bat """
                docker rm -f url-shortener
                docker run -d --name url-shortener -p 5000:5000 %IMAGE_NAME%:latest
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}