pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Youhorng/assignment-2-api-jenkin.git'
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

        stage('Setup Python Environment') {
            steps {
                sh '''
                    # Create venv only if it does not exist
                    if [ ! -d /var/lib/jenkins/venv ]; then
                        echo "Creating new virtual environment..."
                        python3 -m venv /var/lib/jenkins/venv
                    else
                        echo "Virtual environment already exists, skipping creation..."
                    fi

                    # Always upgrade pip and install/update packages
                    /var/lib/jenkins/venv/bin/pip install --upgrade pip
                    /var/lib/jenkins/venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    cd $WORKSPACE
                    JENKINS_NODE_COOKIE=dontKillMe \
                    nohup /var/lib/jenkins/venv/bin/uvicorn main:app \
                        --host 0.0.0.0 \
                        --port 8000 \
                        > /tmp/app.log 2>&1 &
                    echo $! > /tmp/uvicorn.pid
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