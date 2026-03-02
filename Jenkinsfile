pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Youhorng/assignment-2-api-jenkin.git'
            }
        }

        stage('Setup Virtualenv & Install Dependencies') {
            steps {
                sh '''
                    # Install python3-venv if not present
                    sudo apt-get install -y python3-venv python3-pip

                    # Create venv if it doesn't exist
                    if [ ! -d /var/lib/jenkins/venv ]; then
                        python3 -m venv /var/lib/jenkins/venv
                    fi

                    # Always install/update dependencies
                    /var/lib/jenkins/venv/bin/pip install --upgrade pip
                    /var/lib/jenkins/venv/bin/pip install -r requirements.txt
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
                    cd /var/lib/jenkins/workspace/api-jenkin
                    nohup /var/lib/jenkins/venv/bin/uvicorn main:app \
                        --host 0.0.0.0 --port 8000 \
                        > /var/lib/jenkins/app.log 2>&1 &
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