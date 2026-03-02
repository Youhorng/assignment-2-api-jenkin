pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Youhorng/assignment-2-api-jenkin.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv /var/lib/jenkins/venv
                    /var/lib/jenkins/venv/bin/pip install --upgrade pip
                    /var/lib/jenkins/venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Old Server') {
            steps {
                sh '''
                    pkill -f "uvicorn main:app" || true
                    sleep 2
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    cd /var/lib/jenkins/workspace/jenkin-api
                    nohup /var/lib/jenkins/venv/bin/uvicorn main:app \
                        --host 0.0.0.0 \
                        --port 8000 \
                        > /var/lib/jenkins/app.log 2>&1 &
                    echo $! > /var/lib/jenkins/uvicorn.pid
                    sleep 3
                    echo "FastAPI is deployed!"
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