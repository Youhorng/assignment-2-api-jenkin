pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Youhorng/assignment-2-api-jenkin.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Stop Old Server') {
            steps {
                sh '''
                    pkill -f "uvicorn main:app" || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    nohup uvicorn main:app --host 0.0.0.0 --port 8000 \
                        > /home/ubuntu/app.log 2>&1 &
                    echo "FastAPI deployed!"
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}